#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from collections import namedtuple

AUTHOR = "Adam Li"
SITENAME = "Adam Li's blog"
SITEURL = "https://adam2392.github.io"
SITETITLE = "Adam J. Li"
COPYRIGHT_YEAR = 2022

PATH = "content"

# set favicon in the web browser
FAVICON = "images/brain.jpg"

# Photo blog settings | https://github.com/getpelican/pelican-plugins/tree/master/images
PHOTO_LIBRARY = "/Users/adam2392/Documents/adam2392.github.io/content/images/"
# For images in galleries, maximum width and height, plus JPEG quality
PHOTO_GALLERY = (4288, 2848, 100)
# For images associated with articles, maximum width, height, and quality
PHOTO_ARTICLE = (760, 506, 80)
# For thumbnails, maximum width, height, and quality
PHOTO_THUMB = (192, 144, 60)
PHOTO_RESIZE_JOBS = 5  # Number of parallel resize jobs to be run.
# Adds a watermark to all images in articles and pages. Defaults to using your site name.
PHOTO_WATERMARK = True
# Allow the user to change the watermark text or remove it completel
PHOTO_WATERMARK_TEXT = "ADAM LI"
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_REMOVE_GPS = True  # Removes any GPS information from t
PHOTO_EXIF_COPYRIGHT = "COPYRIGHT"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "Adam Li"

# for showing a lot of albums
ALBUM_PATH = PHOTO_LIBRARY

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_RSS = "feeds/all.rss.xml"
AUTHOR_FEED_RSS = "feeds/{slug}.rss.xml"
RSS_FEED_SUMMARY_ONLY = False
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None

# Handling Articles
INDEX_SAVE_AS = "blog.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}/index.html"
RELATED_POSTS_MAX = 5

# language/time settings
TIMEZONE = "America/New_York"
DEFAULT_LANG = "en"

# to run the theme | for now, pelican-bootstrap3
# THEME = "pelican-themes/Responsive-Pelican"
PLUGIN_PATHS = ["pelican-plugins"]
JINJA_ENVIRONMENT = {"extensions": ['jinja2.ext.i18n']}
PLUGINS = [
    "render_math",
    "related_posts",
    # "images",
    "pelican_javascript",
    "i18n_subsites",
    "pelican_albums",
]

# Enable Jinja2 i18n extension used to parse translations.
THEME = "pelican-themes/pelican-bootstrap3"

# Default theme language.
I18N_TEMPLATES_LANG = 'en'

# BROWSER_COLOR = '#333'
# ROBOTS = 'index, follow'

# Main page
MAIN_MENU = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (("Blog", "/categories.html"),
             #  ("Timeline", "/archives.html"),
             #  ("Tags", "/tags.html"),
             ("Curriculum Vitae", "/pdfs/Personal_CV.pdf"),
             # ("Gallery", "/album.html"),
             )

# MARKDOWN = {
#     'extension_configs': {
#         'markdown.extensions.toc': {
#             'marker': '[TOC]',
#             'title': 'Contents',
#             'anchorlink': True,
#             'permalink': True,
#             'baselevel': 2,
#         },
#     }
# }

# for latex and pelican-render-math plugin

""" SOCIAL MEDIA SECTION """
# Social widget
GITHUB_URL = "https://github.com/adam2392"
GITHUB_USER = "adam2392"
GITHUB_REPO_COUNT = 3
TWITTER_USERNAME = "adam2392"

# Links in the sidebar: this is not standard, it is for my own modified
# theme, as it has 3 entries per item:
# - The link title
# - The link itself
# - The icon name on http://fontawesome.io/icons/ after stripping 'fa-'
SOCIAL = (
    ('google scholar', "https://scholar.google.com/citations?user=KxY17KcAAAAJ&hl=en", 'graduation-cap'),
    ("twitter", "https://twitter.com/adam2392"),
    ("stack-overflow", "https://stackexchange.com/users/4494355/ajl123"),
    ("github", "https://github.com/adam2392"),
    ("linkedin", "https://www.linkedin.com/in/adam2392"),
)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Static content
STATIC_PATHS = ["pdfs", "files", "images"]

# Google Analytics Tag
GOOGLE_ANALYTICS = "UA-106551801-1"
