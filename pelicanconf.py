#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Matt'
SITENAME = 'Recettes de cuisine - par Matt'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

LOCALE = ('fr_FR')

THEME = "theme/alchemy"

# THEME = "./theme/blueidea"
DISPLAY_SEARCH_FORM = False
DISPLAY_CATEGORIES_ON_SUBMENU = False
DISPLAY_CATEGORIES_ON_POSTINFO = True

# Blogroll
LINKS = (
    ("Marmiton", "http://marmiton.org/"),
    ("Je vais vous cuisiner", "https://jevaisvouscuisiner.com/"),
)

# Social widget
SOCIAL = ()
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Dates of articles from the file modification
DEFAULT_DATE = "fs"

DEFAULT_DATE_FORMAT = "%d %b %Y"

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Recette"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DESCRIPTION = "Mes recettes préférées à portée de main"
WELCOME_MESSAGE = SIDEBAR_DIGEST = SITESUBTITLE = DESCRIPTION