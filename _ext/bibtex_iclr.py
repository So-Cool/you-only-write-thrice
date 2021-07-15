# Copyright (C) 2021
# Author: Kacper Sokol <ks1591@my.bristol.ac.uk>
# License: new BSD
"""
Implements the `iclr` BibTeX style for Jupyter Book and Sphinx
(`sphinxcontrib-bibtex`).
"""

import pybtex.plugin
from pybtex.style.formatting.alpha import Style
from pybtex.style.labels import BaseLabelStyle as LabelStyle
from sphinxcontrib.bibtex.style.referencing.author_year import AuthorYearReferenceStyle
from sphinxcontrib.bibtex.style.referencing import BaseReferenceText

AYRS = AuthorYearReferenceStyle()

class ICLR(Style):
    """Defines the `iclr` style for `sphinxcontrib-bibtex`."""
    default_label_style = 'iclr-label'

class ICLRlabel(LabelStyle):
    """Defines the `iclr-label` labelling style for `sphinxcontrib-bibtex`."""
    def format_labels(self, sorted_entries):
        for entry in sorted_entries:
            ref = AYRS.inner('p').format_data(
                data=dict(
                    entry=entry,
                    reference_info='',
                    reference_text_class=BaseReferenceText,
                    style=AYRS)
            ).render_as('text')
            yield ref

def setup(app):
    """Sets up the `iclr` style for use with `sphinxcontrib-bibtex`."""
    if 'bibtex_reference_style' not in app.config.overrides:
        app.config.overrides['bibtex_reference_style'] = 'author_year'
    pybtex.plugin.register_plugin(
        'pybtex.style.labels', 'iclr-label', ICLRlabel)
    pybtex.plugin.register_plugin(
        'pybtex.style.formatting', 'iclr', ICLR)
    return {'version': '0.1'}
