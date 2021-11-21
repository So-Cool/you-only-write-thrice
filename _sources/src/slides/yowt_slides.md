---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
rise:
  start_slideshow_at: beginning
  autolaunch: false
  theme: solarized
  transition: none
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

+++ {"slideshow": {"slide_type": "skip"}, "tags": ["purge-cell"], "jupyter": {"source_hidden": true, "outputs_hidden": true}, "collapsed": true}

(sec:slides)=
# Slides #

:::{admonition} Content format
:class: attention
This page is written in the [*Markdown Notebook*][mnb] format.
While it is intended to be rendered through [RISE] as [reveal.js] slides,
it can also be viewed as a Jupyter Book section or a Jupyter Notebook.
The code blocks embedded in this page can be executed through Jupyter Notebook
via [MyBinder] -- this option is available from the *Launch Menu* that appears
after hovering the mouse cursor over the {fa}`rocket` icon shown in the top
bar.
Alternatively, the code boxes can be executed directly on this page with
[Thebe] by activating {fa}`play`&nbsp;*Live Code* from the
{fa}`rocket`&nbsp;*Launch Menu*.

In addition to this article page and the corresponding Jupyter Notebook,
*static* and *interactive* [reveal.js] slides are built from the page source.
The static slides can be accessed with this button
[![View Slides][slides-badge]][slides-link].
To launch the interactive version of the slides (with executable code boxes),
first open this page as a Jupyter Notebook through Binder -- either via
the {fa}`rocket`&nbsp;*Launch Menu* or using this button
[![Open in Binder][binder-badge]][binder-link];
next execute all of the code cells (using the *Kernel &rarr; Restart & Run All*
Jupyter Notebook menu);
then open [RISE] by clicking the {fa}`chart-bar` button located in the top bar
of the Jupyter Notebook interface.
:::

:::{tip}
This page includes a number of Python cells holding setup code.
You can reveal the content of these cells by clicking the {fa}`plus-circle`
buttons, which appear towards the right edge of this page.
:::

[mnb]: https://jupyterbook.org/file-types/myst-notebooks.html
[RISE]: https://rise.readthedocs.io/en/stable/
[reveal.js]: https://github.com/hakimel/reveal.js/
[mybinder]: https://mybinder.org/
[Thebe]: https://jupyterbook.org/interactive/thebe.html
[binder-badge]: https://mybinder.org/badge_logo.svg
[binder-link]: https://mybinder.org/v2/gh/so-cool/you-only-write-thrice/master?urlpath=tree/src/slides/yowt_slides.md
[slides-badge]: https://img.shields.io/badge/view-slides-blue.svg
[slides-link]: https://so-cool.github.io/you-only-write-thrice/src/slides/yowt_slides.slides.html

+++ {"slideshow": {"slide_type": "skip"}, "tags": ["remove-cell"], "jupyter": {"source_hidden": false, "outputs_hidden": true}, "collapsed": false}

:::{note}
This Jupyter Notebook is also available as an [article page][bp2], which
explains how to launch this content as *static* and *interactive* slides.
:::

[bp2]: https://so-cool.github.io/you-only-write-thrice/src/slides/yowt_slides.html

+++ {"slideshow": {"slide_type": "slide"}}

<h1 style="text-align: center">You Only Write Thrice</h1>
<h2 style="text-align: center">Creating Documents, Computational Notebooks and Presentations From a Single Source</h2>
<br><br><br>
<img width="25%" style="vertical-align:bottom; float:left;" src="../img/slides/uob.svg">
<p style="vertical-align:bottom; float:right; font-size: 120%;"><b>Kacper Sokol</b><br/>and Peter Flach</p>

+++ {"slideshow": {"slide_type": "subslide"}, "tags": ["remove-cell"]}

<center>
These slides are also available as an
<a href="https://so-cool.github.io/you-only-write-thrice/src/slides/yowt_slides.html">article page</a>,
which explains how to launch them as a Jupyter Notebook or interactive slides.
</center>

+++ {"slideshow": {"slide_type": "skip"}}

<div style="margin-bottom: 3cm;"></div>

+++ {"slideshow": {"slide_type": "notes"}, "tags": ["remove-cell"]}

Hello Everybody,
I'm Kacper and in this talk I'll show you our idea for an end-to-end,
transparent publishing workflow, which makes the entire process easier for
academics.

```{code-cell} ipython3
---
tags: [hide-input, thebe-init]
slideshow:
  slide_type: skip
---
%matplotlib widget
import ipywidgets as widgets
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import IFrame

plt.style.use('seaborn')
```

```{code-cell} ipython3
---
tags: [hide-input, thebe-init]
slideshow:
  slide_type: skip
---
DISTILL = 'https://distill.pub/2019/activation-atlas/'
OPEN_REVIEW = 'https://openreview.net/forum?id=i4zpuNRiU4G'
YOU_ONLY_WRITE_THRICE = 'https://so-cool.github.io/you-only-write-thrice/'
SIMPLY_LOGICAL = 'https://too.simply-logical.space/src/text/2_part_ii/4.2.html'

def preview_url(url, height=600):
    return IFrame(url, width=800, height=height)  # 1200
```

```{code-cell} ipython3
---
tags: [hide-input, thebe-init]
slideshow:
  slide_type: skip
---
def interactive_plot():
    fig, ax = plt.subplots(figsize=(10, 4))
    fig.patch.set_alpha(0)
    ax.set_ylim([-4, 4])
    ax.grid(True)
    x = np.linspace(0, 2 * np.pi, 100)

    def my_sine(x, w, amp, phi):
        """Returns a sine for x with angular frequeny w and amplitude amp."""
        return amp * np.sin(w * (x - phi))

    @widgets.interact(w=(0, 10, 1),
                      amp=(0, 4, .1),
                      phi=(0, 2 * np.pi + 0.01, 0.01))
    def update(w=1.0, amp=1, phi=0):
        """Removes old lines from plot and plots new one."""
        [l.remove() for l in ax.lines]
        ax.plot(x, my_sine(x, w, amp, phi), color='C0')
```

+++ {"slideshow": {"slide_type": "slide"}}

<h2 style="text-align: center">Publishing Process</h2>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Stagnation</h3>

<div style="display: block; margin-left: auto; margin-right: auto; width: 100%;">
<div style="float: left; width: 45%;">
<img src="../img/slides/Origin_of_Species.jpg" style="width:100% margin-left: auto; margin-right: auto;">
</div>
<div style="float: right; width: 45%;">
<img src="../img/slides/kernels.jpg" style="width:100% margin-left: auto; margin-right: auto;">
</div>
</div>

+++ {"slideshow": {"slide_type": "skip"}}

<div style="margin-bottom: 17cm;"></div>

+++ {"slideshow": {"slide_type": "notes"}, "tags": ["remove-cell"]}

Can you spot a difference between these two publishing formats?
The one on the left is a photo of a manuscript -- a physical printout.
The one on the right is a screenshot of a PDF.
Not much of a difference after all.

PDFs are ubiquitous these days.
They are easier to distribute and copy,
but have the same limitations as paper printouts.

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Ideas: distill.pub</h3>

```{code-cell} ipython3
preview_url(DISTILL, height=500)
```

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Ideas: OpenReview</h3>
<img width="90%" align="middle" src="../img/slides/OPENREVIEW.png" alt="surrogate" style="display: block; margin-left: auto; margin-right: auto;">

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Ideas: The Open Journals (The Journal of Open Source Software)</h3>
<img width="90%" align="middle" src="../img/slides/JOSS_REVIEW.png" alt="surrogate" style="display: block; margin-left: auto; margin-right: auto;">

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Issues</h3>

* Standalone tools
    - Not integrated
    - Lack of a dedicated process
* Not covering the entire publishing process
    - Compose (write / revise)
    - Review (comment / rebut)
    - Publish (format / version)

+++ {"slideshow": {"slide_type": "slide"}}

<h2 style="text-align: center">Format Multiplicity</h2>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>(Conference) Publishing</h3>

<br>

<div class="row">
<div class="column">
<ul>
<li>Manuscripts</li>
<li>Presentations</li>
<li>Posters</li>
<li>Promotional videos</li>
<li>Press releases</li>
<li>Blog posts</li>
<li>Source code</li>
<li>Computational examples</li>
<li>...</li>
</ul>
</div>
<div class="column fragment">
<ul>
<li>Reviews</li>
<li>Revisions</li>
<li>Versions</li>
</ul>
</div>
</div>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Source Formats</h3>

* $\LaTeX$ documents and Beamer slides
* Microsoft Word / OpenOffice Writer / Google Docs
* Microsoft PowerPoint / OpenOffice Impress / Google Slides
* Markdown / HTML (and other web technologies such as JavaScript)
* Code hosted on Dropbox / GitHub / BitBucket
* Jupyter Notebooks / CodaLab documents

+++ {"slideshow": {"slide_type": "fragment"}}

---

<center>
    <b>Multiple (out-of-sync) copies of the same content in different formats</b>
</center>

+++ {"slideshow": {"slide_type": "slide"}}

<h3>Lowest Common Denominator: Static Outputs and Artefacts</h3>

Artefacts *reusability*:
* visualisations / figures
* tables
* code snippets
* mathematical typesetting

enforces their simplest – often static – type

+++ {"slideshow": {"slide_type": "slide"}}

<h2 style="text-align: center">Towards Online and Interactive Research Outputs</h2>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Authoring</h3>

<div class="row">
<div class="column">
<h4>Multiple Entry Points – Single Source</h4>
<p>MyST Markdown →</p>
<ul>
<li><b>Jupyter Notebook</b> – computational narrative</li>
<ul>
<li>Google Colab</li>
<li>MyBinder</li>
</ul>
<li><b>Reveal.JS</b> – interactive slides</li>
<li><b>Jupyter Book</b> – interactive report/document/book</li>
</ul>
</div>
<div class="column fragment">
<h4>Version-controlled Environment</h4>
<ul>
<li>Source versioning and history tracking</li>
<li>E.g., <tt>git</tt> or <tt>mercurial</tt></li>
</ul>
</div>
</div>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Reviewing</h3>

<div class="row">
<div class="column">
<ul>
<li><b>Akin to source code review</b>, e.g., through <em>Issues</em> and <em>Pull Requests</em> infrastructure</li>
<li><b>Permanently attached</b> to the document source</li>
<ul>
<li>Provenance record</li>
<li>Resubmission history</li>
</ul>
<li><b>Conversational</b> review with inline comments and discussions</li>
</ul>
</div>
<div class="column">
<img width="90%" align="middle" src="../img/slides/review.png" alt="surrogate" style="display: block; margin-left: auto; margin-right: auto;">
</div>
</div>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Publishing</h3>

* Tag a version
* Release to an archiving platform

+++ {"slideshow": {"slide_type": "fragment"}}

---

**Bibliometrics**
* DOI minting (e.g., Zenodo) to support citations
* Google Analytics-like dissemination tracking

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Presenting</h3>

* **Three formats**: documents, slides and computational notebooks
* Native *interactivity* support
* Improved accessibility
    - Execute directly **in the browser** – no need to install stuff
    - Support for web-enabled **assistive technologies**
* Web technologies are the limit

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
interactive_plot()
```

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>The Way Forward</h3>

* Extend the Jupyter Book / Sphinx **plugin ecosystem**
  - Support non-mainstream programming languages (SWI Prolog, ProbLog and cplint)
  - Linked exercise and solution blocks
  - Custom code syntax highlighting
* **Bespoke publishing lifecycle platform** (instead of GitHub or BitBucket)
* **Compute resources** suitable for hosting and executing the (interactive) content

---

<img width="15%" style="vertical-align:bottom; float:left;" src="../img/slides/tailor.png">

Horizon 2020 ICT-48 European AI excellence centre exploring **new ways of working** and **AI-powered research and collaboration tools**.

+++ {"slideshow": {"slide_type": "slide"}}

<h2 style="text-align: center">Exhibit</h2>

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Source</h3>

> <https://github.com/so-cool/you-only-write-thrice/>

<img width="90%" align="middle" src="../img/slides/source_code.png" alt="surrogate" style="display: block; margin-left: auto; margin-right: auto;">

+++ {"slideshow": {"slide_type": "subslide"}}

<h3>Preview</h3>

> <https://so-cool.github.io/you-only-write-thrice/>

```{code-cell} ipython3
---
slideshow:
  slide_type: '-'
---
preview_url(YOU_ONLY_WRITE_THRICE, height=500)
```

+++ {"slideshow": {"slide_type": "subslide"}}

<h2 style="text-align: center; vertical-align: center;">Thank You!</h2>
<br><br><br>
<p style="text-align: right; vertical-align:bottom; float:right; font-size: 100%;"><a href="K.Sokol@bristol.ac.uk">K.Sokol@bristol.ac.uk</a></p>

+++ {"slideshow": {"slide_type": "skip"}}
