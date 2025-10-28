# Configuration file for the Sphinx documentation builder.

# -- Project information --------------------------

project = "ezmsg"
copyright = "2022, JHU/APL"
author = "JHU/APL"

release = "1.0.0"
version = "1.0.0"

# -- General configuration --------------------------

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.graphviz",
    "sphinx.ext.intersphinx",
    "sphinxext.rediraffe",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]

source_suffix = [".rst", ".md"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The toctree master document
master_doc = "index"

# When set to True, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Intersphinx configuration --------------------------

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "ezmsg-core": ("https://ezmsg.org/ezmsg/", None),
    "ezmsg-sigproc": ("https://ezmsg.org/ezmsg-sigproc/", None),
    "ezmsg-learn": ("https://ezmsg.org/ezmsg-learn/", None),
    "ezmsg-lsl": ("https://ezmsg.org/ezmsg-lsl/", None),
}
intersphinx_disabled_domains = ["std"]

# -- Options for HTML output -----------------------------

html_theme = "pydata_sphinx_theme"
html_logo = "_static/_images/ezmsg_logo.png"
html_favicon = "_static/_images/ezmsg_logo.png"

html_static_path = ["_static"]

# Redirects for pages that are unavailable or moved
rediraffe_redirects = {
    "about.rst": "explanations/content-explanations.rst",
    "getting-started.rst": "tutorials/start.rst",
}

# Timestamp is inserted at every page bottom in this strftime format.
html_last_updated_fmt = '%Y-%m-%d'

# -- Options for EPUB output --------------------------
epub_show_urls = "footnote"

add_module_names = False

# -- Options for graphviz -----------------------------
graphviz_output_format = "svg"

def setup(app):
    app.add_css_file("custom.css")