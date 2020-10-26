# Recettes

Source pour le site de recette, utilisant Pelican (Python) pour générer un site statique

Le theme utilisé est une version modifiée d'Alchemy:
- couleur verte
- traduite en français, avec 'recette' qui remplace 'article'
- ajouts d'icones (par ex. par catégories)
- ajout de la liste des catégories en haut de la page

## Installation

Installation des lib python (de préf. dans un venv):

`pip install -r requirements.txt`

Génération du site:

`pelican`

Test du site:

`pelican --listen`