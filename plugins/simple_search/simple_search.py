from codecs import open
from json import JSONEncoder, dumps
import logging
import os

from pelican import signals
from .text_processing import get_ingredient, get_words

logger = logging.getLogger(__name__)


class Recette:
    def __init__(self, ID, url, title) -> None:
        self.ID = ID
        self.url = url
        self.title = title

    def analyze(self, html_doc):
        text = get_ingredient(html_doc, self.title)
        return get_words(text)


class Index:
    def __init__(self):
        self.index = {}
        self.documents = []

    def index_document(self, document: Recette, content):
        self.documents.append(document)

        for token in document.analyze(content):
            if token not in self.index:
                self.index[token] = []
            self.index[token].append(document.ID)


class RecetteEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class SearchIndexGenerator:
    def __init__(self, context, settings, path, theme, output_path, *null):
        self.output_path = output_path
        self.context = context
        self.content = settings.get("PATH")
        self.tpages = settings.get("TEMPLATE_PAGES")
        self.theme = settings.get("THEME_STATIC_DIR")

    def generate_output(self, writer):
        template_path = os.path.join(self.output_path, self.theme)
        if not os.path.exists(template_path):
            os.mkdir(template_path)
        search_settings_path = os.path.join(template_path, "search.min.js")

        pages = self.context["articles"]

        index = Index()

        # Generate list of articles and pages to index
        i = 0
        for page in pages:
            recette = Recette(i, page.url, page.title)
            index.index_document(recette, page.content)
            i += 1

        # keywords = [x for x in keywords if x[-1] != "s" or x[:-1] not in keywords]
        # keywords = sorted(list(keywords))

        recettes = dumps(
            index.documents, cls=RecetteEncoder, ensure_ascii=False
        )
        search_index = dumps(
            index.index, cls=RecetteEncoder, ensure_ascii=False
        )

        # Write the search settings file to disk
        with open(search_settings_path, "w", encoding="utf-8") as fd:
            fd.write("recettes = " + recettes + ";\n")
            fd.write("search_index = " + search_index + ";\n")


def get_generators(generators):
    return SearchIndexGenerator


def register():
    signals.get_generators.connect(get_generators)
