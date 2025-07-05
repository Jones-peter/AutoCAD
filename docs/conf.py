import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # so Sphinx can find AutoCAD/

project = 'AutoCAD'
author = 'Jones Peter'
release = '0.1.6'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',       # for Google/Numpy docstrings
    'sphinx.ext.viewcode',
]

autodoc_mock_imports = ["pywin32"]
html_theme = 'furo'  # or sphinx_rtd_theme
