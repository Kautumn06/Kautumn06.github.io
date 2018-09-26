#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Kristen McIntyre'
SITENAME = "Kristen McIntyre's Development Blog"
SITETITLE = "Kristen McIntyre"
SITESUBTITLE = 'sic parvis magna'
SITEURL = 'http://Kautumn06.github.io'

PATH = 'content'

# Disable caching
LOAD_CONTENT_CACHE = False

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'
DATE_FORMATS = {
    'en': '%B %d, %Y'
}

# Theme Settings
THEME = 'theme/Flex'
FAVICON = '/images/favicon.png'
SITELOGO = '/images/lola.jpg'
#PYGMENTS_STYLE = 'monokai'

# Main Menu
MAIN_MENU = True
MENUITEMS = (
    ('Archives', '/archives.html'),
    ('Categories', '/categories.html'),
    ('Tags', '/tags.html'),
)

DEFAULT_PAGINATION = 10

# Default category to misc
DEFAULT_CATEGORY = 'misc'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Portfolio', 'http://getpelican.com/'),
#         ('Kaggle', 'https://kaggle.com/kautumn06'),)

# Social widget
SOCIAL = (
    ('twitter', 'https://twitter.com/kautumn06'),
    ('linkedin', 'https://linkedin.com/in/kristenmcintyre1'),
    ('github', 'https://github.com/Kautumn06'),)

GITHUB_URL = 'https://github.com/Kautumn06'
LINKEDIN_USERNAME = 'kristenmcintyre1'

# Adds Twitter sharing button to articles
TWITTER_USERNAME = 'Kautumn06'

# Static paths are copied without parsing their contents
STATIC_PATHS = ['extras', 'images']

# Path-specific metadata
EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
}

# Set all articles to draft by default
DEFAULT_METADATA = {
    'status': 'draft',
}

# Exclude Jupyter Notebook checkpoints
#PAGE_EXCLUDES = ['.ipynb_checkpoints']
#ARTICLE_EXCLUDES = ['.ipynb_checkpoints']

# Plugin Settings
#PLUGIN_PATHS = ['/home/kautumn06/pelican_plugins']
#MARKUP = ('md', 'ipynb')
#PLUGINS = [
#    'ipynb.markup',
#    'i18n_subsites',
#    'render_math',
#    'sitemap',
#    'tipue_search',
#]

# Sitemap settings
#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.6,
#        'indexes': 0.6,
#        'pages': 0.5,
#    },
#    'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly',
#    }
#}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

#COPYRIGHT_YEAR = 2018
