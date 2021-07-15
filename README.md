[![Licence][licence-badge]][licence-link]
[![Online][online-badge]][online-link]

[licence-badge]: https://img.shields.io/github/license/so-cool/you-only-write-thrice.svg
[licence-link]: https://github.com/so-cool/you-only-write-thrice/blob/master/LICENCE
[online-badge]: https://img.shields.io/badge/read-online-green.svg
[online-link]: https://so-cool.github.io/you-only-write-thrice/

# You Only Write Thrice #

This repository holds the source of an exhibit accompanying the
["You Only Write Thrice"][openreview] paper published at
[Rethinking ML Papers -- ICLR 2021 Workshop][workshop].
The built book is hosted on *GitHub Pages* and is available under
<https://so-cool.github.io/you-only-write-thrice/>.
The online document is accompanied by [reveal.js] slides composed
from a [Markdown Notebook][mnb] that is also a source document
underlying a section of the online article.
A static snapshot of the slides is built with the `jupyter nbconvert`
conversion tool -- see the [`build_slides.sh`] script for more details.
The slides can also be launched with [RISE] -- from a Jupyter Notebook
through [MyBinder] -- to allow interactive and executable content.
Therefore, in our workflow a single source file may produce:

* computational notebooks;
* static and interactive slides; and
* sections of an online document/book.

## Building the Book ##

1. Pull the book repository
   ```bash
   git clone https://github.com/so-cool/you-only-write-thrice.git

   cd you-only-write-thrice
   ```
2. Install [*Jupyter Book*][jb-pypi] (`requirements-article.txt`) and
   slides execution requirements (`requirements-slides.txt`)
   ```bash
   pip install -r requirements-article.txt
   pip install -r requirements-slides.txt
   ```
3. Build the book
   ```bash
   jb build .
   ```
4. Build the slides
   ```bash
   ./build_slides.sh
   ```
5. Open the html build
   ```bash
   open _build/html/index.html
   ```
   or run it as a server (to get the embedded SlidesLive window to work)
   ```bash
   python -m http.server --directory _build/html
   open http://localhost:8000
   ```

[openreview]: https://openreview.net/forum?id=i4zpuNRiU4G
[workshop]: https://rethinkingmlpapers.github.io/
[reveal.js]: https://github.com/hakimel/reveal.js/
[mnb]: https://jupyterbook.org/file-types/myst-notebooks.html
[`build_slides.sh`]: https://github.com/so-cool/you-only-write-thrice/blob/master/build_slides.sh
[RISE]: https://rise.readthedocs.io/en/stable/
[MyBinder]: https://jupyterbook.org/interactive/launchbuttons.html#binder-buttons-for-your-pages
[jb-pypi]: https://pypi.org/project/jupyter-book/
