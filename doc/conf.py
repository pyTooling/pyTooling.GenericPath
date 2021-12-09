# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
from sys     import path as sys_path

#sys_path.insert(0, os.path.abspath('.'))
sys_path.insert(0, os.path.abspath('..'))
#sys_path.insert(0, os.path.abspath('../pyGenericPath'))
#sys_path.insert(0, os.path.abspath('_extensions'))
#sys_path.insert(0, os.path.abspath('_themes/sphinx_rtd_theme'))


# -- Project information -----------------------------------------------------

project = 'pyTooling.GenericPath'
copyright = '2017-2021, Patrick Lehmann'
author = 'Patrick Lehmann'

# The full version, including alpha/beta/rc tags
release = 'v0.2'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
# Sphinx theme
	"sphinx_rtd_theme",
# Standard Sphinx extensions
	"sphinx.ext.autodoc",
	'sphinx.ext.extlinks',
	'sphinx.ext.intersphinx',
	'sphinx.ext.inheritance_diagram',
	'sphinx.ext.todo',
	'sphinx.ext.graphviz',
	'sphinx.ext.mathjax',
	'sphinx.ext.ifconfig',
	'sphinx.ext.viewcode',
# SphinxContrib extensions

# Other extensions
#	'DocumentMember',
# local extensions (patched)

# local extensions
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
	"_build",
	"Thumbs.db",
	".DS_Store"
]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# ==============================================================================
# Sphinx.Ext.InterSphinx
# ==============================================================================
intersphinx_mapping = {
	'python':   ('https://docs.python.org/3', None),
#	'pyFlags':  ('http://pyFlags.readthedocs.io/en/latest', None),
}


# ==============================================================================
# Sphinx.Ext.AutoDoc
# ==============================================================================
# see: https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration
autodoc_member_order = "bysource"       # alphabetical, groupwise, bysource


# ==============================================================================
# Sphinx.Ext.ExtLinks
# ==============================================================================
extlinks = {
	"ghissue": ('https://GitHub.com/pyTooling/pyTooling.GenericPath/issues/%s', 'issue #'),
	"ghpull":  ('https://GitHub.com/pyTooling/pyTooling.GenericPath/pull/%s', 'pull request #'),
	"ghsrc":   ('https://GitHub.com/pyTooling/pyTooling.GenericPath/blob/main/pyTooling.GenericPath/%s?ts=2', None),
#	"test":  ('https://GitHub.com/pyTooling/pyTooling.GenericPath/blob/main/test/%s?ts=2', None)
}


# ==============================================================================
# Sphinx.Ext.Graphviz
# ==============================================================================
graphviz_output_format = "svg"
