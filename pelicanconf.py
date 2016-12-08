#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'yuya yano'
SITENAME = 'もくもくブログ'
SITEURL = 'http://blog.muuny-blue.info'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'jp'

DIRECT_TEMPLATES = ('index', 'tags', 'categories', 'archives', 'sitemap')
SITEMAP_SAVE_AS = 'sitemap.xml'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GOOGLE_ANALYTICS = "UA-67688469-1"

# About
DETAILS = (['プログラマの日記です。'])

CATEGORIES = (('Diary', 'book', '#0bd566'),
              ('Programming', 'console', '#555'),
              ('家', 'home', '#f48c39'))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom setting

DEFAULT_PAGINATION = 5

# SNS share
TWITTER_USERNAME = '_y_y_m_m_'
HATENA_SHARE = True
FACEBOOK_APPID = '387525661451951'
#GOOGLEPLUS_SHARE = True
#POCKET_SHARE = True
#TUMBLR_SHARE = True

SOCIAL = [('Twitter', 'https://twitter.com/_y_y_m_m_'),
          ('Github', 'https://github.com/yymm'),
          ('Bitbucket', 'https://bitbucket.org/yymm')]

SUMMARY_MAX_LENGTH = 10

DISQUS_SITENAME = "mokumoku"

MD_EXTENSIONS = ['extra', 'admonition', 'codehilite(css_class=highlight)',
                 'nl2br', 'sane_lists', 'toc', 'del_ins', 'embedly']

PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['always_modified', 'pelican_youtube']
ALWAYS_MODIFIED = True
GOOGLE_ADSENSE = True
