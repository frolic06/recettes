from bs4 import BeautifulSoup
from stop_words import get_stop_words
from string import punctuation
import re

stop_words = get_stop_words('french')
stop_words += ['kg', 'max', 'cl', 'cm', 'dl', 'ml', 'litre', 'mm', 'mn', 'qq', 'éventuellement']
stemmings_words_1 = ["maquereaux", "morceaux", "poireaux", "rouleaux"]
stemmings_words_1 += ["alsaciennes", "amandes", "avocats", "bananes", "belles", "bergamotes", "betteraves", "biscuits", "blancs", "boites",
                      "bouquets", "branches", "bricks", "brins", "brocolis", "cacahuètes", "carottes", "chiches", "ciselées", "citrons",
                      "classiques", "clémentines", "concassées", "confites", "coupées", "coupés", "courgettes", "crues", "crus",
                      "cubes", "cuillères", "cuits", "douces", "endives", "entiers", "entières", "faciles", "feuilles", "feuilletées", 
                      "filets", "fines", "fleurs", "foies", "framboises", "fraîches", "galettes", "gousses", "grains", "grands", "gratins", "grillés",
                      "groseilles", "grosses", "hachées", "haricots", "indiens", "jaunes", "lasagnes", "légumes", "meringues", "moules", "moulues",
                      "moyennes", "muffins", "navets", "noirs", "noisettes", "oeufs", "oignons", "olives", "oranges", "pains", "patates", "petites", "petits",
                      "piments", "pincées", "plats", "poivrons", "pommes", "pots", "poulets", "pâtes", "quantités", "raisins", "ramequins", 
                      "recettes", "rondelles", "rouges", "râpées", "sablés", "sachets", "samoussas", "saucisses", "secs", "sucrés", "sucrée", "sèches",
                      "tailles", "tartes", "tasses", "tomates", "tourtes", "tranches", "vertes", "verts", "volailles", "yaourts", "zestes", "échalotes",
                      "écrasées", "écrasée", "émincées", "émincés", "épinards", "abricots", "abats", "aubergines", "froide", "verte", "petite"]

def basic_stemming(word):
    if word in stemmings_words_1:
        return word[:-1]
    else:
        return word

def get_ingredient(html_doc: str, title: str) -> str:
    soup = BeautifulSoup(html_doc, 'html.parser')
    text = title
    for sibling in soup.find(name="h2").next_siblings:
        if sibling.text == 'Préparation':
            break
        text += f" {sibling.get_text()}"
    return text

def get_words(text: str):
    res = set()
    text = text.replace("'", ' ')
    text = text.replace("’", ' ')
    text = text.replace("°", ' ')
    text = text.replace("-", ' ')
    text = text.replace("“", '')
    text = text.replace("”", '')
    text = text.replace("🦈", '')
    text = text.replace("🐡", '')
    text = text.replace("œ", 'oe')
    for word in text.lower().split():
        word = word.translate(str.maketrans('', '', punctuation))
        word = re.sub(r'[0-9]', '', word)
        if len(word) > 1 and word not in stop_words:
            res.add(basic_stemming(word))
    return list(res)