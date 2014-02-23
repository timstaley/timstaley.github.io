#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tim Staley'
SITENAME = u"Tim Staley"
#SITEURL = 'http://timstaley.co.uk'
SITEURL = 'http://agrajag'
RELATIVE_URLS = False

TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
# Feed generation is usually not desired when developing
# FEED_ALL_ATOM = None
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

THEME='../pelican-bootstrap3'
BOOTSTRAP_THEME = "flatly"


DIRECT_TEMPLATES = ('blog_index', 'tags', 'archives',)
PAGINATED_DIRECT_TEMPLATES= ('blog_index',)
BLOG_INDEX_SAVE_AS = 'blog/index.html'
# 
ARCHIVES_URL = 'posts'
ARCHIVES_SAVE_AS = 'posts/index.html'
CATEGORIES_URL = 'categories'
CATEGORIES_SAVE_AS = 'categories/index.html'
CATEGORY_URL = 'posts/{slug}'
CATEGORY_SAVE_AS = 'posts/{slug}/index.html'
ARTICLE_URL='posts/{slug}'
ARTICLE_SAVE_AS='posts/{slug}/index.html'
TAGS_URL = 'tag'
TAGS_SAVE_AS = 'tag/index.html'
TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
PAGE_URL='{slug}'
PAGE_SAVE_AS='{slug}/index.html'
 
STATIC_PATHS= ['images', 'css']
DEFAULT_DATE = 'fs'
 
# DIRECT_TEMPLATES = ( 'index', 'tags', 'archives', 'articles')

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False
BLOG_URL = 'blog'
MENUITEMS = [
             ('Research', '/research'),
             ('Code', '/code'), 
#              ("About Me", '/about'),
             ]


DEFAULT_PAGINATION = 10
GOOGLE_ANALYTICS = 'UA-46485279-1'
USE_OPEN_GRAPH = False

