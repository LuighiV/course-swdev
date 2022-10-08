# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.append(os.path.abspath("./_ext"))


# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Software development tools'
copyright = '2022, Luighi Viton'
author = 'Luighi Viton'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autosectionlabel',
    'google_analytics',
    "sphinxext.opengraph",
]

autosectionlabel_prefix_document = True

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_show_sourcelink = False
html_static_path = ['_static']

html_extra_path = ['CNAME', 'robots.txt']

# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Add GA tag
google_analytics_id = os.environ.get('CI_GOOGLE_ANALYTICS_ID', None)

# Add OG metatags
ogp_site_url = "http://swdev.courses.luighiviton.com/"
ogp_image = "http://swdev.courses.luighiviton.com/_static/banner-es.png"
ogp_description_length = 300
ogp_type = "article"

# Format date
today_fmt = '%Y-%m-%d'
