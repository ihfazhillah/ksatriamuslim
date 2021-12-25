AUTHOR = 'ihfazhillah'
SITENAME = 'Ksatria Muslim'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Jakarta'

DEFAULT_LANG = 'id'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)
#
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 15

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# PLUGINS
PLUGIN_PATHS = ['plugins']
PLUGINS = ['sitemap', 'category_order', 'w3c_validate', 'optimize_images', 'gzip_cache', 'json_list']

## SITEMAP PLUGIN
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': .99,
        'pages': .75,
        'indexes': .5
    },
    'changefreqs': {
        'articles': 'daily',
        'pages': 'daily',
        'indexes': 'daily'
    },
}
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}/index.html'
CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
PAGINATION_PATTERNS = (
    (1, '{base_name}/', '{base_name}/index.html'),
    (2, '{base_name}/{number}/', '{base_name}/{number}/index.html'),
)

TEMPLATE_PAGES = {
    'wakeup/index.html': 'wakeup/index.html'
}

JSON_LIST_PATHS = [
        "ksatriamuslim_backgrounds",
        "ksatriamuslim_books",
        "ksatriamuslim_audios"
]

STATIC_PATHS = ['uploads', 'wakeup',]
STATIC_PATHS += JSON_LIST_PATHS




# Theme Settings
THEME = 'themes/brutalist'

GOOGLE_ANALYTICS = 'G-EEZ521Z3B8'
FB_PIXEL = '227923979366433'
