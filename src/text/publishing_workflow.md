# Publishing Workflow #

The academic publishing life-cycle consists of four distinct steps:
composing, reviewing, publishing and presenting. Researchers need to
write down their findings, get them reviewed and revised, formally
publish them adhering to bibliometric standards, and, finally, present
their work in different formats: as academic writing, conference talks,
poster sessions, promotional videos, blog posts, press releases and
public engagement events, among others. Each artefact produced in this
process constitutes a different entry point to the research outputs,
allowing a diverse audience to freely explore a wide range of its --
theoretical, computational and experimental -- aspects. However, despite
sharing a common origin, the current publishing workflow requires us to
craft each piece of this mosaic separately.

To address this issue, we propose a proof-of-concept pipeline for
composing academic articles, computational notebooks and presentations
from a single curated source, helping to document and disseminate
research in accessible, transparent and reproducible formats. To this
end, we harness modern web technologies, e.g., reveal.js, and
open-source software from the Jupyter ecosystem, in particular Jupyter
Book and Jupyter Notebook/Lab. Such an approach allows exploring and
interacting with research outputs directly in a web browser (including
mobile devices), thus alleviating technological and software barriers --
akin to what PDF did for electronic documents. Finally, we tackle the
review step by linking it to the document source, which permits a much
more structured and conversational process that feels more natural and
intuitive.

## Composing ##

The backbone of our workflow are documents written in MyST Markdown --
an extended markdown syntax that supports basic academic publishing
features such as tables, figures, mathematical typesetting and
bibliography management. Content written in this format is highly
interoperable and can be converted to LaTeX, HTML, PDF or EPUB outside
of the proposed system, thus serve as a source for, or a component of,
other authoring environments. The key to automatically composing a
variety of output formats is the syntactic sugar allowing to
superficially split the content into *fragments* and annotate them.
These *tags* prescribe how each piece of prose, figure or code should be
treated -- e.g., included, skipped or hidden -- when building different
target formats. Then, Jupyter Book can process selected fragments to
generate web documents and computational narratives, the latter of which
may be launched as Jupyter Notebooks with either MyBinder or Google
Colab. While this is already a step towards "reproducibility by design",
having content that depends on code implicitly encourages releasing it
as a software package that can be invoked whenever necessary, therefore
improving reproducibility even further. The aforementioned source
annotation can also specify a slide type and its content in a
presentation composed with reveal.js, streamlining yet another aspect of
the academic publishing workflow. While each of these artefacts is
destined for web publication, their trimmed version can also be exported
to formats such as PDF or EPUB.

## Reviewing ##

In the proposed workflow, we envisage storing the document source in a
version-controlled environment similar to `git`, which has two benefits.
First, it enables tracking changes in the document, versioning it and
monitoring its evolution through various workshops, conferences and
journals submissions. Secondly, such a setting supports peer review
inspired by code review in software engineering. In this model, the
reviewers could attach their comments to specific locations in the
paper, allowing other reviewers to chime in and the paper authors to
address very specific concerns explicitly linked to the submitted
document. Furthermore, this structure creates a discussion-like
experience, which should feel more natural to humans -- akin to comments
and discussions in shared document writing platforms such as Google
Docs, Microsoft Office Word and Overleaf. The entire process can be made
more structured and objective by providing the reviewers with general
checklists and a collection of tags to annotate each of their concerns
(e.g., typo, derivation error or incorrect citation). The rebuttal and
revision stage is also simplified in this framework since all of the
changes applied to the document are tracked and can be linked to
individual reviewer comments.

Such a formalisation of the review--rebut--revise cycle significantly
increases the transparency and provenance of the entire process. This
approach can be trialled through the *Pull Request* functionality of
commercial code sharing platforms, such as GitHub or Bitbucket, before
investing more time and resources into the development of a dedicated
(self-hosted and open-source) technology. While doing so would not allow
for anonymous peer-review, the process could start with implementing and
improving upon the aforementioned model operationalised by the the Open
Journals, helping to identify and prioritise features expected of the
dedicated platform. Similarly, displaying a reviewer's comments could be
delayed until the review is finalised to avoid bias, followed by merging
them with other comments placed in close proximity. Notably, adapting
the proposed review format would not require version-control or software
engineering skills since all of the complexities are abstracted away by
the user interface. Since the review could be permanently attached to
the submission, the implications of this approach would need to be
studied and understood before enforcing it. Alternatively, or in
addition to the above process, external services such as
*hypothesis*[^_8] or *utterances*[^_9] -- which are available as
(experimental) Jupyter Book plugins -- could be used to collaboratively
review, comment, discuss or annotate submissions.

## Publishing ##

Since the content source is stored in a version-controlled environment,
one can imagine submitting a document for review by specifying its
particular version (e.g., by tagging a selected `git` commit), with the
publication process following the same procedure. Such a versioning
approach would also demystify the journey of a paper through various
workshops, conferences and journals, and clarify the improvements made
after each rejection. In this setting, bibliometrics can be achieved by
automatically minting Digital Object Identifiers (DOI) upon publication,
for example, using *zenodo*[^_10], which is already integrated with
software versioning mechanisms provided by GitHub and Bitbucket. Another
bibliometrics strategy suitable for web technologies can be derived from
tools such as Google Analytics, which could be deployed to collect
fine-grained information about the readers and hyper-links pointing to
and from the publication, thus allowing to build a detailed network of
connected documents. While the format is intended for web publication,
it can also be stored on a personal computer or converted into
monolithic entities such as LaTeX, PDF or EPUB. This interoperability
allows to archive any or all variants of the document to ensure its
longevity and accessibility. Notably, by connecting the local copy to a
custom execution environment, the interactivity of the materials can be
preserved offline.

## Presenting ##

The proposed authoring framework alleviates the need to create separate
articles, computational narratives and slides by building them from a
single markdown source. Since these artefacts are intended for web
publication, they can take advantage of modern technologies that can
make them interactive, thus more engaging. For example, the RISE
extension of the Jupyter Notebook platform {cite}`rise` allows launching
reveal.js presentations with executable code boxes. By building bespoke
plugins, we can enable support of less prominent programming languages
(recall the aforementioned example of SWI Prolog) and create additional
output formats such as blog posts or academic posters. Since the
materials are delivered as web pages, technological barriers are lifted,
portability is guaranteed and sharing is made easy. Finally, the
proposed workflow can be deployed in education to prepare lectures,
courseworks, exercises, notes and (self-)study materials, therefore
supporting both synchronous and asynchronous learning -- see the online
release[^_11] of our interactive edition {cite}`flach2018simply` of the
*Simply Logical* textbook {cite}`flach1994simply` for an example.

[^_8]: <https://hypothes.is/>
[^_9]: <https://utteranc.es/>
[^_10]: <https://zenodo.org/>
[^_11]: <https://book.simply-logical.space/>
