#!/usr/bin/env python3
# pylint: disable=C0103,W0622
"""Configuration file for the Sphinx documentation builder.

# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
"""
import pathlib
import sys
cur_dir = pathlib.Path(__file__).resolve
sys.path.insert(0, str(cur_dir))

# -- Project information ----------------------------------------------------
# The full version, including alpha/beta/rc tags
author = 'Xander Harris'
copyright = '2021, Xander Harris'

###
# ```{rubric} General configuration
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [".venv/*"]

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'myst_parser',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_git',
    'sphinx_last_updated_by_git',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.duration',
    'sphinx.ext.githubpages',
    'sphinx.ext.graphviz',
    'sphinx.ext.intersphinx',
    'sphinx.ext.linkcode',
    'sphinx.ext.todo',
    'sphinxcontrib.autoyaml',
]
# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'renku'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}
# Add any paths that contain templates here, relative to this directory.
myst_enable_extensions = [
    "amsmath",
    "attrs_block",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]
myst_footnote_transition = True
myst_title_to_header = True
project = 'Panegyric'
release = 'v0.1.1'
show_authors = True
source_suffix = {
    '.md': 'markdown'
}
templates_path = ['_templates']

def linkcode_resolve(domain, info):
    """Resolve link code links."""
    if domain != 'py':
        return None
    if not info['module']:
        return None
    filename = info['module'].replace('.', '/')

    path = 'github.com/edwardtheharris/panegyric/blob/main'
    url = f'https://{path}/{filename}.py'
    return url
