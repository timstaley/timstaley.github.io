#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from collections import OrderedDict
import os
from glob import glob

AUTHOR = u'Tim Staley'
SITENAME = u"Tim Staley"
SITEURL = 'http://www.timstaley.test'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = u'en'
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
THEME='/home/ts3e11/code/zf-site'
#THEME='notmyidea'
#THEME='/home/ts3e11/code/pelican-themes/notmyidea-cms'
#THEME='/home/ts3e11/code/pelican-themes/tuxlite_zf'
OUTPUT_PATH='/var/www/'

ARTICLE_URL='posts/{slug}'
ARTICLE_SAVE_AS='posts/{slug}/index.html'
PAGE_URL='{slug}'
PAGE_SAVE_AS='{slug}/index.html'

STATIC_PATHS= ['images', 'files']

#DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives',
                    #)
                    # 'blog')
INDEX_SAVE_AS = 'blog/index.html'
#BLOG_SAVE_AS = 'blog/index.html'
#Choose the pages/articles by slug to link to in the top-bar.
#NB there is a magic value, 'BLOG', which links to the blog index. 
#(See blog.html template.)
#(Site landing index.html is always linked in upper left.)
TOPBAR_PAGE_LINKS = OrderedDict((
                                 ('about','About'), 
                                 ('code','Code'),
                                 ('research' ,'Research'),
                                 ('links','Links'),
                                 ('BLOG','Tech Blog'),
                                 ))

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('Jinja2', 'http://jinja.pocoo.org/'),
#           ('You can modify those links in your config file', '#'),)
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

