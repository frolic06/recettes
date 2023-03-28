from bs4 import BeautifulSoup
from stop_words import get_stop_words
from string import punctuation
import re

stop_words = get_stop_words('french')
stop_words += ['kg', 'max', 'cl', 'cm', 'dl', 'ml', 'litre', 'mm', 'mn', 'qq']

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
            res.add(word)
    return list(res)