# Copyright (C) 2021
# Author: Kacper Sokol <kacper@xmlx.io>
# License: new BSD
"""
Implements the `iclr` BibTeX style for Jupyter Book and Sphinx
(`sphinxcontrib-bibtex`).
"""

__version__ = '0.2'

import pybtex.plugin
import sphinxcontrib.bibtex.plugin

from dataclasses import dataclass, field
from pybtex.style.formatting.alpha import Style
from pybtex.style.labels import BaseLabelStyle as LabelStyle
from sphinxcontrib.bibtex.style.referencing import BracketStyle
from sphinxcontrib.bibtex.style.referencing.author_year import AuthorYearReferenceStyle
from sphinxcontrib.bibtex.style.template import SphinxReferenceInfo

AYRS = AuthorYearReferenceStyle()
REF_INFO = SphinxReferenceInfo('', '', '', '', '')

class ICLR(Style):
    """Defines the `iclr` style for `sphinxcontrib-bibtex`."""
    default_label_style = 'iclr-label'

class ICLRlabel(LabelStyle):
    """Defines the `iclr-label` labelling style for `sphinxcontrib-bibtex`."""
    def format_labels(self, sorted_entries):
        for entry in sorted_entries:
            data = dict(
                entry=entry,
                reference_info=REF_INFO,
                style=AYRS
            )
            ref = str(AYRS.inner('p').format_data(data=data))
            yield ref

def bracket_style() -> BracketStyle:
    return BracketStyle(sep='; ')

@dataclass
class AuthorYearSemicolonReferenceStyle(AuthorYearReferenceStyle):
    bracket_parenthetical: BracketStyle = field(default_factory=bracket_style)
    bracket_textual: BracketStyle = field(default_factory=bracket_style)
    bracket_author: BracketStyle = field(default_factory=bracket_style)
    bracket_label: BracketStyle = field(default_factory=bracket_style)
    bracket_year: BracketStyle = field(default_factory=bracket_style)

def setup(app):
    """Sets up the `iclr` style for use with `sphinxcontrib-bibtex`."""
    if 'bibtex_reference_style' not in app.config.overrides:
        app.config.overrides['bibtex_reference_style'] = 'author_year_semicolon'
    sphinxcontrib.bibtex.plugin.register_plugin(
        'sphinxcontrib.bibtex.style.referencing',
        'author_year_semicolon',
        AuthorYearSemicolonReferenceStyle)
    pybtex.plugin.register_plugin(
        'pybtex.style.labels', 'iclr-label', ICLRlabel)
    pybtex.plugin.register_plugin(
        'pybtex.style.formatting', 'iclr', ICLR)
    return {'version': __version__}
