from recommonmark.parser import CommonMarkParser

source_parsers = {
    '.md': CommonMarkParser,
}

source_suffix = ['.rst', '.md']

master_doc = 'index'
project = u'markdown-publishing-guide'

html_theme_options = {
    'collapse_navigation': True
}
