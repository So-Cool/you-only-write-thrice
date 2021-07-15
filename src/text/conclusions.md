# Conclusions #

In this paper we proposed a novel publication workflow built around
Jupyter Book, Jupyter Notebook and reveal.js. Our exhibit demonstrates
how to create narrative-driven documents (peppered with executable code
examples), computational notebooks and interactive slides, all from a
single markdown source. Furthermore, we outlined a strategy for hosting
and disseminating such materials through version-controlled environments
similar to code sharing repositories. Such a platform facilitates an
intuitive review mechanism inspired by software engineering practice,
thus endowing provenance and transparency to the scientific publication
process. While our exhibit is currently a bare-bones proof-of-concept
built from open-source tools, it shows the potential for transforming
the current PDF workflow into an environment focused on content creators
and reviewers. One can even imagine automating parts of this process
with "bots" validating submissions based on predefined criteria, and
partially pre-populating a review form to streamline the entire
publication life-cycle (akin to continuous integration and deployment
pipelines in software engineering).

While addressing some of the main issues with current publishing
practice, the proposed workflow is not (yet) a silver bullet and the
underlying technology needs further development to mature into reliable
software. We envisage that engagement of the scientific community and
open discussion are needed to steer the development and foster broader
adoption of such tools, for example, workshops encouraging submission
and review in such a format. Interactivity is a great advantage of
Jupyter Book publications, but the compute resources employed to execute
the underlying code have to be accounted for and provisioned since
relying upon free code-execution environments (such as Google Colab and
MyBinder) is not sustainable in the long term. Given that the main
output of the proposed workflow is a collection of web pages, they
either need to be accessed online or downloaded and browsed locally to
take full advantage of their format; generating PDFs and EPUBs is also
possible, however they lack interactivity and may not be visually
appealing since they only play a secondary role. Notably, the proposed
framework is not as powerful as LaTeX, which benefits from decades of
development and a rich ecosystem of packages, therefore any
customisation or automation will require a bespoke plugin that may be
slow to create and buggy at first. Nonetheless, without making the first
step -- and addressing the disadvantages associated with it -- the
publishing process will not benefit from the technology that we
developed to make our research possible in the first place.
