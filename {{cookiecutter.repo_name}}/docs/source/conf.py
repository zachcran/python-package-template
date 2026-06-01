import os
import shutil
import sys

sys.path.insert(0, os.path.abspath("../src"))

project = '{{cookiecutter.repo_name | replace("-", " ") | title}}'
copyright = "2024, {{cookiecutter.full_name}}"
author = "{{cookiecutter.full_name}}"
release = "{{cookiecutter.version}}"


# ---

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

current_directory = os.path.dirname(__file__)

# Autodoc extension needs to know where the modules are
sys.path.insert(0, os.path.join(current_directory, "../../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

__location__ = os.path.dirname(__file__)

project = '{{cookiecutter.repo_name | replace("-", " ") | title}}'
copyright = "2026, {{cookiecutter.full_name}}"
author = "{{cookiecutter.full_name}}"
release = "{{cookiecutter.version}}"

# -- Run sphinx-apidoc -------------------------------------------------------
# Avoids running sphinx-apidoc manually.
#
# Credit: Pyscaffold's sphinx_conf.template file, licensed under 0BSD, see
# https://github.com/pyscaffold/pyscaffold/blob/master/src/pyscaffold/templates/sphinx_conf.template#L23

try:  # for Sphinx >= 1.7
    from sphinx.ext import apidoc
except ImportError:
    from sphinx import apidoc

output_dir = os.path.join(__location__, "api")
module_dir = os.path.join(
    __location__, "../../src/{{cookiecutter.package_name}}"
)
try:
    shutil.rmtree(output_dir)
except FileNotFoundError:
    pass

try:
    import sphinx

    cmd_line = (
        f"sphinx-apidoc --implicit-namespaces -f -o {output_dir} {module_dir}"
    )

    args = cmd_line.split(" ")
    if tuple(sphinx.__version__.split(".")) >= ("1", "7"):
        # This is a rudimentary parse_version to avoid external dependencies
        args = args[1:]

    apidoc.main(args)
except Exception as e:
    print("Running `sphinx-apidoc` failed!\n{}".format(e))


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

templates_path = ["_templates"]
exclude_patterns = ["Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
