#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Matt'
SITENAME = 'Recettes de cuisine par Matt'
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
SITEIMAGE = "images/profile.png"

THEME = "theme/flex"

ROBOTS = "index, follow"
DISPLAY_PAGES_ON_MENU = False
##################################
MAIN_MENU = True
HOME_HIDE_TAGS = False

SITETITLE=SITENAME
MENUITEMS = (
    ("Auteurs", "/authors.html"),
    ("Archives", "/archives.html"),
    ("Catégories", "/categories.html"),
    ("Labels", "/tags.html"),
)
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = False
CUSTOM_CSS = 'theme/theme.css'
DISABLE_URL_HASH = True
LINKS_IN_NEW_TAB = "external"
##################################

DISPLAY_SEARCH_FORM = False
DISPLAY_CATEGORIES_ON_SUBMENU = False
DISPLAY_CATEGORIES_ON_POSTINFO = True

# Blogroll
LINKS = (
    # ("Marmiton", "http://marmiton.org/"),
    # ("Je vais vous cuisiner", "https://jevaisvouscuisiner.com/"),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 20

# Dates of articles from the file modification
DEFAULT_DATE = "fs"

DEFAULT_DATE_FORMAT = "%d %b %Y"

USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "Recette"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DESCRIPTION = "Mes recettes préférées à portée de main"
WELCOME_MESSAGE = SIDEBAR_DIGEST = SITESUBTITLE = DESCRIPTION

# ARTICLE_ORDER_BY = 'Title'
# PAGE_ORDER_BY = 'Title'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['subcategory']