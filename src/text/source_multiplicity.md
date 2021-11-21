# Source Multiplicity #

Despite immense technological advances permeating into our everyday life
and work, scientific publishing has seen much less evolution. While
moving on from hand- or type-written manuscripts to electronic documents
allowed for faster and more convenient editing, dissemination and
review, the (now obsolete and unnatural) limitations of the "movable
type" publication format persist. Among others, this glass wall poses
significant challenges to effective communication of scientific findings
with their ever-increasing volume, velocity and complexity. To overcome
these difficulties we may need to depart from the, de facto standard,
*Portable Document Format* (PDF) and set our sight on something more
flexible and universal. In the past three decades the World Wide Web has
organically evolved from a collection of hyper-linked text documents
into a treasure trove of diverse and interactive resources -- a process
that should inspire an evolution of the scientific publishing workflow.

A physical, printed and bound, copy of a research paper may have been
mostly replaced by a PDF document viewable on a wide array of electronic
devices, but both formats effectively share the same limitations. These
constraints have recently become even more prominent with research
venues requiring to publish supplementary materials that fall outside of
the textual spectrum. Releasing *source code* is advised to ensure
reproducibility; *computational notebooks* highlight individual methods,
experiments and results; recording a short *promotional video* helps to
advertise one's research; *slides* and *oral presentations* (often
pre-recorded nowadays) disseminate findings and foster discussions; and
*posters* graphically summarise research contributions. Notably, these
artefacts are usually created independently and are distributed
separately from the underlying paper -- nonetheless while disparate in
appearance, form and function, they all share a common origin.

```{figure} ../img/article/yowt_fig.svg
---
width: 50%
name: fig:uowt
---
Generating multiple conference artefacts such as documents (papers),
presentations (slides) and computational notebooks from a single source
repository can streamline the academic publishing workflow.
```

Without a designated place for each research output and a dedicated
workflow to create and distribute them, they may end up scattered
through the Internet. Code may be published on GitHub, computational
notebooks distributed via Google Colab or MyBinder, and videos posted on
YouTube. Slides and posters, on the other hand, tend to accompany the
paper -- which itself is placed in proceedings -- sparingly with an
often outdated version of the article available through arXiv. While
organising, distributing and linking all of these resources is a goal in
itself, we shall first reconsider the authoring process responsible for
their creation. Since delivering each format appears to be an
independent task that requires a dedicated effort, having as many of
these resources as possible generated from a single source could
streamline the process and create a coherent narrative hosted in a
single place. While as a community we created technology powerful enough
to train vision models in a web browser[^_1], we find it somewhat
difficult to see beyond the restrictive PDF format and hence
increasingly lack publishing tools necessary to carry out our work
effectively.

To streamline the process of creating academic content we propose to
generate conference artefacts -- such as documents (papers),
presentations (slides) and computational notebooks -- from a single
source as depicted in {numref}`fig:uowt`.
By storing all the information in a
version-controlled environment (e.g., `git`) we can also track article
evolution and revision, and facilitate a review process similar to the
one deployed in software engineering and closely resembling the
OpenReview workflow. Combining together research outputs as well as
their reviews and revisions could improve credibility and provenance of
scientific finding, thus simplifying re-submission procedures and taking
the pressure off overworked reviewers. Additionally, including
*interactive* materials -- such as code boxes and computational
notebooks -- in the published resources encourages releasing *working*
and accessible code.

The envisaged workflow generalises beyond academic publishing and may
well be adopted for teaching, for example, producing lecture notes,
slides and (computational) exercise sheets. Our proof of concept
consists of:
- documents based on *Jupyter Book* {cite}`jupyterbook`;
- computational narratives presented as *Jupyter
  Notebooks* {cite}`jupyter`; and
- presentations (decks of slides) created with
  *reveal.js* {cite}`revealjs`.

A self-contained example of generating these three artefacts from a
single source document is published with GitHub Pages and accessible at
<https://so-cool.github.io/you-only-write-thrice/>.
The text is written in extended markdown syntax (MyST flavour), and the
code is executed in Python, however any programming language supported
by the Jupyter ecosystem can be used. These sources are hosted on GitHub
and can be inspected at
<https://github.com/so-cool/you-only-write-thrice/>.
Publishing these diverse materials as interactive web resources
democratises access to cutting-edge research since they can be explored
directly in the browser without installing any software dependencies.
While the main output of the proposed workflow is a collection of HTML
pages, it can also produce static formats such as PDF or EPUB, albeit
forfeiting all of the discussed advantages.

As it stands, our workflow consists of open-source tools, but it relies
on free tiers of commercial services. To ensure longevity and
sustainability, we need community-driven software and infrastructure for
hosting, reviewing and publishing resources in the proposed formats, for
example, taking inspiration from the OpenReview model. Being able to
influence its development, we could prioritise features needed for a
wider adoption of this bespoke platform, e.g., by implementing anonymous
submission and review protocols, which are not available in commercial
solutions such as GitHub or Bitbucket. At the content-generation end,
our workflow relies heavily on the Jupyter ecosystem. Jupyter Book and
MyST Markdown provide basic text formatting and implement academic
publishing features such as mathematical typesetting (with LaTeX syntax)
and bibliography management (with BibTeX). The platform is
still in early development and exhibits certain limitations, e.g.,
fine-grained layout customisation may be difficult, which is
particularly noticeable with reveal.js slides. However, the Jupyter Book
environment can be extended with custom plugins, which in the long term
may be as plentiful as LaTeX packages; for example, we built support for
non-mainstream programming languages such as SWI Prolog[^_2], cplint[^_3]
and ProbLog[^_4] that are not natively supported by Jupyter. While the
openness and transparency of the proposed workflow can be considered its
forte, the same qualities may also pose challenges for academic
publishing, which need to be explored further before pursuing this
avenue.

A part of our workflow derives from the *computational narrative*
concept, which interweaves prose with executable code, thus improving
reproducibility and accessibility of scientific findings. The most
prominent example of this technology are Jupyter Notebooks delivered to
the audience through MyBinder or Google Colab. Content that is more
narrative-driven, on the other hand, can be published with
Bookdown {cite}`bookdown` -- a toolkit comparable to Jupyter Book but
stemming from the R language ecosystem. A similar publication platform,
dedicated to research papers, is Distill[^_5], however its wider adoption
is hindered by the degree of familiarity with web technologies required
of authors. Additionally, the proposed workflow borrows from software
engineering; in particular, code versioning and review. The former is
not widely adopted by the scientific community, partially contributing
to scientific papers lacking evolution traces and provenance that could
shine a light on their journey through rejection and acceptance at
various workshops, conferences and journals. On the other hand, the
software-like review process of academic writing has been adopted by The
Open Journals[^_6], for example, the Journal of Open Source Software[^_7],
further improving on the model operationalised by OpenReview.

[^_1]: <https://teachablemachine.withgoogle.com/>
[^_2]: <https://book-template.simply-logical.space/>
[^_3]: <http://cplint-template.simply-logical.space/>
[^_4]: <https://problog-template.simply-logical.space/>. ProbLog is
       unique in this aspect as it can either be executed directly from
       Python (through a custom interpreter, thus not requiring a dedicated
       plugin) or with bespoke code boxes (as is the case with SWI Prolog
       and cplint).
[^_5]: <https://distill.pub/>
[^_6]: <https://www.theoj.org/>
[^_7]: <https://joss.theoj.org/>. The submission and review process is
       outlined in the journal's documentation published at
       <https://joss.readthedocs.io/>.
