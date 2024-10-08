#!/usr/bin/env python3
#
# Kedro documentation build configuration file, created by
# sphinx-quickstart on Mon Dec 18 11:31:24 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
from __future__ import annotations

import importlib
import re
import sys
from inspect import getmembers, isclass, isfunction
from pathlib import Path

from click import secho, style

from kedro import __version__ as release

# -- Project information -----------------------------------------------------

project = "kedro"
author = "kedro"

# The short X.Y version.
version = re.match(r"^([0-9]+\.[0-9]+).*", release).group(1)


# -- General configuration ---------------------------------------------------
# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx.ext.doctest",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    "myst_parser",
    "notfound.extension",
    "sphinxcontrib.jquery",
    "sphinx.ext.intersphinx",
    "sphinx_last_updated_by_git",
    "sphinx_favicon",
    "sphinxcontrib.youtube",
]

# enable autosummary plugin  (table of contents for modules/classes/class
# methods)
autosummary_generate = True
autosummary_generate_overwrite = False
napoleon_include_init_with_doc = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

intersphinx_mapping = {
    "kedro-viz": ("https://docs.kedro.org/projects/kedro-viz/en/v6.6.1/", None),
    "kedro-datasets": ("https://docs.kedro.org/projects/kedro-datasets/en/kedro-datasets-2.0.0/", None),
    "cpython": ("https://docs.python.org/3.9/", None),
    "ipython": ("https://ipython.readthedocs.io/en/8.21.0/", None),
    "mlflow": ("https://www.mlflow.org/docs/2.12.1/", None),
    "kedro-mlflow": ("https://kedro-mlflow.readthedocs.io/en/0.12.2/", None),
}

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {".rst": "restructuredtext", ".md": "markdown"}

# The master toctree document.
master_doc = "index"

favicons = [
    "https://kedro.org/images/favicon.ico",
]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = [
    "**.ipynb_checkpoints",
    "_templates",
    "modules.rst",
    "source",
    "kedro_docs_style_guide.md",
]

type_targets = {
    "py:class": (
        "object",
        "bool",
        "int",
        "float",
        "str",
        "tuple",
        "Any",
        "Dict",
        "dict",
        "list",
        "set",
        "typing.Dict",
        "typing.Iterable",
        "typing.List",
        "typing.Tuple",
        "typing.Type",
        "typing.Set",
        "kedro.config.config.ConfigLoader",
        "kedro.io.catalog_config_resolver.CatalogConfigResolver",
        "kedro.io.core.AbstractDataset",
        "kedro.io.core.AbstractVersionedDataset",
        "kedro.io.core.CatalogProtocol",
        "kedro.io.core.DatasetError",
        "kedro.io.core.Version",
        "kedro.io.data_catalog.DataCatalog",
        "kedro.io.kedro_data_catalog.KedroDataCatalog",
        "kedro.io.memory_dataset.MemoryDataset",
        "kedro.io.partitioned_dataset.PartitionedDataset",
        "kedro.pipeline.pipeline.Pipeline",
        "kedro.runner.runner.AbstractRunner",
        "kedro.framework.context.context.KedroContext",
        "kedro.framework.startup.ProjectMetadata",
        "abc.ABC",
        "Path",
        "pathlib.Path",
        "PurePosixPath",
        "pathlib.PurePosixPath",
        "requests.auth.AuthBase",
        "google.oauth2.credentials.Credentials",
        "Exception",
        "CONF_SOURCE",
        "integer -- return number of occurrences of value",
        "integer -- return first index of value.",
        "kedro_datasets.pandas.json_dataset.JSONDataset",
        "pluggy._manager.PluginManager",
        "PluginManager",
        "_DI",
        "_DO",
        "deltalake.table.Metadata",
        # The statements below were added after subclassing UserDict in AbstractConfigLoader.
        "None.  Remove all items from D.",
        "a shallow copy of D",
        "a set-like object providing a view on D's items",
        "a set-like object providing a view on D's keys",
        "v, remove specified key and return the corresponding value.",
        "None.  Update D from dict/iterable E and F.",
        "an object providing a view on D's values",
        "(k, v), remove and return some (key, value) pair",
        "D.get(k,d), also set D[k]=d if k not in D",
        "D[k] if k in D, else d.  d defaults to None.",
        "None.  Update D from mapping/iterable E and F.",
        "Patterns",
        "CatalogConfigResolver",
        "CatalogProtocol",
        "KedroDataCatalog",
    ),
    "py:data": (
        "typing.Any",
        "typing.Callable",
        "typing.Union",
        "typing.Optional",
        "typing.Tuple",
    ),
    "py:exc": (
        "ValueError",
        "BadConfigException",
        "MissingConfigException",
        "DatasetError",
        "ImportError",
        "KedroCliError",
        "Exception",
        "TypeError",
        "SyntaxError",
        "CircularDependencyError",
        "OutputNotUniqueError",
        "ConfirmNotUniqueError",
        "ParserError",
    ),
}
# https://stackoverflow.com/questions/61770698/sphinx-nit-picky-mode-but-only-for-links-i-explicitly-wrote
nitpick_ignore = [(key, value) for key in type_targets for value in type_targets[key]]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "kedro-sphinx-theme"
here = Path(__file__).parent.absolute()

# Theme options are theme-specific and customise the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {"collapse_navigation": False, "style_external_links": True}

# html_extra_path used to define a path to robots.txt which is used by webcrawlers
# to ignore or allow certain links.
# We've decided to rely on RTD's default robots.txt, so we no longer need to specify a custom one,
# see discussion at https://github.com/kedro-org/kedro/issues/3741
# html_extra_path = [str(here / "robots.txt")]

# Removes, from all docs, the copyright footer.
html_show_copyright = False

# some of these complain that the sections don't exist (which is not true),
# too many requests, or forbidden URL
linkcheck_ignore = [
    "http://127.0.0.1:8787/status",  # Dask's diagnostics dashboard
    "https://datacamp.com/community/tutorials/docstrings-python",  # "forbidden" url
    "https://github.com/argoproj/argo/blob/master/README.md#quickstart",
    "https://console.aws.amazon.com/batch/home#/jobs",
    "https://github.com/EbookFoundation/free-programming-books/blob/master/books/free-programming-books-langs.md#python",
    "https://github.com/jazzband/pip-tools#example-usage-for-pip-compile",
    "https://www.astronomer.io/docs/cloud/stable/get-started/quickstart#",
    "https://eternallybored.org/misc/wget/",
    "https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table.from_pandas",
    "https://www.oracle.com/java/technologies/javase-downloads.html",  # "forbidden" url
    "https://www.java.com/en/download/help/download_options.html",  # "403 Client Error: Forbidden for url"
    # "anchor not found" but it's a valid selector for code examples
    "https://docs.delta.io/latest/delta-update.html#language-python",
    "https://github.com/kedro-org/kedro/blob/main/kedro/framework/project/default_logging.yml",
    "https://github.com/kedro-org/kedro/blob/main/kedro/framework/project/rich_logging.yml",
    "https://github.com/kedro-org/kedro/blob/main/README.md#the-humans-behind-kedro",  # "anchor not found" but is valid
    "https://opensource.org/license/apache2-0-php/",
    "https://docs.github.com/en/rest/overview/other-authentication-methods#via-username-and-password",
    "https://www.educative.io/blog/advanced-yaml-syntax-cheatsheet#anchors",
    "https://www.quora.com/What-is-thread-safety-in-Python",  # "403 Client Error: Forbidden for url"
]

# Comment out settings to fix Client Rate Limit Error 429
linkcheck_retries = 3
# linkcheck_rate_limit_timeout = 2.0

html_context = {
    "display_github": True,
    "github_url": "https://github.com/kedro-org/kedro/tree/main/docs/source",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}

html_show_sourcelink = False

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "Kedrodoc"

# -- Options for LaTeX output ------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [(master_doc, "Kedro.tex", "Kedro Documentation", "Kedro", "manual")]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "kedro", "Kedro Documentation", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "Kedro",
        "Kedro Documentation",
        author,
        "Kedro",
        "Kedro is a Python framework for creating reproducible, maintainable and modular data science code.",
        "Data-Science",
    )
]

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Kedro specific configuration -----------------------------------------
KEDRO_MODULES = [
    "kedro.io",
    "kedro.pipeline",
    "kedro.runner",
    "kedro.config",
    "kedro_datasets",
]


def get_classes(module):
    importlib.import_module(module)
    return [obj[0] for obj in getmembers(sys.modules[module], lambda obj: isclass(obj))]


def get_functions(module):
    importlib.import_module(module)
    return [
        obj[0] for obj in getmembers(sys.modules[module], lambda obj: isfunction(obj))
    ]


def remove_arrows_in_examples(lines):
    for i, line in enumerate(lines):
        lines[i] = line.replace(">>>", "")


def autolink_replacements(what: str) -> list[tuple[str, str, str]]:
    """
    Create a list containing replacement tuples of the form:
    (``regex``, ``replacement``, ``obj``) for all classes and methods which are
    imported in ``KEDRO_MODULES`` ``__init__.py`` files. The ``replacement``
    is a reStructuredText link to their documentation.

    For example, if the docstring reads:
        This LambdaDataset loads and saves ...

    Then the word ``LambdaDataset``, will be replaced by
    :class:`~kedro.io.LambdaDataset`

    Works for plural as well, e.g:
        These ``LambdaDataset``s load and save

    Will convert to:
        These :class:`kedro.io.LambdaDataset` load and save

    Args:
        what: The objects to create replacement tuples for. Possible values
            ["class", "func"].

    Returns:
        A list of tuples: (regex, replacement, obj), for all "what" objects
        imported in __init__.py files of ``KEDRO_MODULES``.

    """
    replacements = []
    suggestions = []
    for module in KEDRO_MODULES:
        if what == "class":
            objects = get_classes(module)
        elif what == "func":
            objects = get_functions(module)

        # Look for recognised class names/function names which are
        # surrounded by double back-ticks
        if what == "class":
            # first do plural only for classes
            replacements += [
                (
                    rf"``{obj}``s",
                    f":{what}:`~{module}.{obj}`\\\\s",
                    obj,
                )
                for obj in objects
            ]

        # singular
        replacements += [
            (rf"``{obj}``", f":{what}:`~{module}.{obj}`", obj) for obj in objects
        ]

        # Look for recognised class names/function names which are NOT
        # surrounded by double back-ticks, so that we can log these in the
        # terminal
        if what == "class":
            # first do plural only for classes
            suggestions += [
                (rf"(?<!\w|`){obj}s(?!\w|`{{2}})", f"``{obj}``s", obj)
                for obj in objects
            ]

        # then singular
        suggestions += [
            (rf"(?<!\w|`){obj}(?!\w|`{{2}})", f"``{obj}``", obj) for obj in objects
        ]

    return replacements, suggestions


def log_suggestions(lines: list[str], name: str):
    """Use the ``suggestions`` list to log in the terminal places where the
    developer has forgotten to surround with double back-ticks class
    name/function name references.

    Args:
        lines: The docstring lines.
        name: The name of the object whose docstring is contained in lines.
    """
    title_printed = False

    for i in range(len(lines)):
        if ">>>" in lines[i]:
            continue

        for existing, replacement, obj in suggestions:
            new = re.sub(existing, rf"{replacement}", lines[i])
            if new == lines[i]:
                continue
            if ":rtype:" in lines[i] or ":type " in lines[i]:
                continue

            if not title_printed:
                secho("-" * 50 + "\n" + name + ":\n" + "-" * 50, fg="blue")
                title_printed = True

            print(
                "["
                + str(i)
                + "] "
                + re.sub(existing, rf"{style(obj, fg='magenta')}", lines[i])
            )
            print(
                "["
                + str(i)
                + "] "
                + re.sub(existing, rf"``{style(obj, fg='green')}``", lines[i])
            )

    if title_printed:
        print("\n")


def autolink_classes_and_methods(lines):
    for i in range(len(lines)):
        if ">>>" in lines[i]:
            continue

        for existing, replacement, obj in replacements:
            lines[i] = re.sub(existing, rf"{replacement}", lines[i])


def autodoc_process_docstring(app, what, name, obj, options, lines):
    try:
        # guarded method to make sure build never fails
        log_suggestions(lines, name)
        autolink_classes_and_methods(lines)
    except Exception as e:
        print(
            style(
                "Failed to check for class name mentions that can be "
                f"converted to reStructuredText links in docstring of {name}. "
                f"Error is: \n{e!s}",
                fg="red",
            )
        )

    remove_arrows_in_examples(lines)


def setup(app):
    app.connect("autodoc-process-docstring", autodoc_process_docstring)


# (regex, restructuredText link replacement, object) list
replacements = []

# (regex, class/function name surrounded with back-ticks, object) list
suggestions = []

try:
    # guarded code to make sure build never fails
    replacements_f, suggestions_f = autolink_replacements("func")
    replacements_c, suggestions_c = autolink_replacements("class")
    replacements = replacements_f + replacements_c
    suggestions = suggestions_f + suggestions_c
except Exception as e:
    print(
        style(
            "Failed to create list of (regex, reStructuredText link "
            "replacement) for class names and method names in docstrings. "
            f"Error is: \n{e!s}",
            fg="red",
        )
    )

user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:99.0) Gecko/20100101 Firefox/99.0"

myst_heading_anchors = 5
myst_enable_extensions = ["colon_fence"]
