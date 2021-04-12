# ---
# jupyter:
#   jupytext:
#     formats: md:myst
#     text_representation:
#       extension: .py
#       format_name: percent
#   rise:
#     start_slideshow_at: beginning
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] slideshow={"slide_type": "skip"} tags=["purge-cell"] jupyter={"source_hidden": true, "outputs_hidden": true}
# (sec:problog:py)=

# %% [markdown] slideshow={"slide_type": "slide"}
# # Bayesian Networks (Percent NB) #

# %% [markdown] slideshow={"slide_type": "skip"}
# :::{note}
# This page is based on the [*Bayesian networks*] ProbLog tutorial, which
# is executed from within Python using the [*ProbLog library*].
# :::
#
# [*Bayesian networks*]: https://dtai.cs.kuleuven.be/problog/tutorial/basic/02_bayes.html
# [*ProbLog library*]: https://dtai.cs.kuleuven.be/problog/tutorial/advanced/01_python_interface.html

# %% [markdown] slideshow={"slide_type": "skip"} tags=["purge-cell"] jupyter={"source_hidden": true, "outputs_hidden": true}
# :::{admonition} Content format
# :class: attention
# This page is written in the [*Percent Notebook*] format.
# The ProbLog content is displayed through [iPython cell magic][magic].
# Alternatively, see the [Markdown Notebook version][markdown] of the
# *Bayesian Networks* tutorial for an example of executing ProbLog code
# with [`ipywidgets`], or the [Jupyter Notebook version][notebook] to see
# how ProbLog code can be executed directly from Python.
#
# You can execute the code blocks enclosed below by launching this page as a
# Jupyter Notebook with MyBinder -- this option is available from the
# *Launch Menu* that appears after hovering the mouse cursor over the
# {fa}`rocket` icon shown in the top bar.
# Note that Google Colab execution environment is not available for pages
# written in the [*Percent Notebook*] format.
# You can also **enable the widgets** to work directly on this page with
# [Thebe] by activating {fa}`play`&nbsp;*Live Code* from the
# {fa}`rocket`&nbsp;*Launch Menu*.
#
# In addition to this book page and the corresponding Jupyter Notebook,
# *interactive* [reveal.js] slides are built from the page source.
# To launch the interactive version of the slides (with executable code boxes),
# you need to open this page as a Jupyter Notebook in Binder -- either via
# the {fa}`rocket`&nbsp;*Launch Menu* or using this button
# [![Open in Binder][binder-badge]][binder-link];
# then open [RISE] by clicking the {fa}`chart-bar` button located in the top bar
# of the Jupyter Notebook interface.
# :::
#
# [*Percent Notebook*]: https://jupyterbook.org/file-types/jupytext.html
# [`ipywidgets`]: https://ipywidgets.readthedocs.io/
# [notebook]: bayesian_networks-jnb
# [markdown]: bayesian_networks-mnb
# [magic]: https://ipython.readthedocs.io/en/stable/interactive/magics.html#cell-magics
# [Thebe]: https://jupyterbook.org/interactive/launchbuttons.html#live-interactive-pages-with-thebelab
# [reveal.js]: https://github.com/hakimel/reveal.js/
# [binder-badge]: https://mybinder.org/badge_logo.svg
# [binder-link]: https://mybinder.org/v2/gh/so-cool/you-only-write-thrice/master?urlpath=tree/src/text/bayesian_networks-pnb.py
# [RISE]: https://rise.readthedocs.io/en/stable/

# %% [markdown] slideshow={"slide_type": "skip"} tags=["remove-cell"] jupyter={"source_hidden": true, "outputs_hidden": true}
# :::{note}
# This Jupyter Notebook is also available as a [book page][bp2], which explains
# how to launch this content as *interactive* slides.
# :::
#
# [bp2]: .

# %% [markdown] slideshow={"slide_type": "skip"} tags=["purge-cell"] jupyter={"source_hidden": true, "outputs_hidden": true}
# :::{tip}
# This page includes a number of Python cells holding code needed to set up
# ProbLog ipywidgets.
# You can reveal their content by clicking the {fa}`plus-circle` buttons, which
# appear towards the right edge of this page.
# :::

# %% tags=["hide-input", "thebe-init"] slideshow={"slide_type": "skip"}
import problog

%load_ext problog.magic


# %% [markdown] slideshow={"slide_type": "subslide"}
# We illustrate the use of Bayesian networks in ProbLog using the famous [Earthquake] example.
#
# [Earthquake]: http://www.bnlearn.com/bnrepository/#earthquake

# %% [markdown] slideshow={"slide_type": "fragment"}
# Suppose there is a burglary in our house with probability 0.7 and an earthquake with probability 0.2. Whether our alarm will ring depends on both burglary and earthquake:
# * if there is a burglary and an earthquake, the alarm rings with probability 0.9;
# * if there is only a burglary, it rings with probability 0.8;
# * if there is only an earthquake, it rings with probability 0.1;
# * if there is neither a burglary nor an earthquake, the alarm doesn't ring.

# %% [markdown] slideshow={"slide_type": "subslide"}
# To model this as a Bayesian network, one would use three random variables, *burglary*, *earthquake* and *alarm*, with *burglary* and *earthquake* being parents of *alarm*. To model this in ProbLog, there are two possible solutions: using 'plain' ProbLog or using some synthactic sugar called probabilistic clauses and annotated disjunctions. We now explain both solutions.
#
# digraph alarm1 { burglary -> alarm; earthquake -> alarm; }
# [ProbLog syntax documentation]
#
# [ProbLog syntax documentation]: https://problog.readthedocs.io/en/latest/modeling_basic.html#problog

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Probabilistic facts ##

# %% [markdown] slideshow={"slide_type": "subslide"}
# In 'plain' ProbLog, we can encode the Bayesian network as follows.
#
# * Since *burglary* and *earthquake* are random variable without parents, we can simply encode them as probabilistic facts, with the proper probability.
# * To express the dependence of the random variable *alarm* on its parents *burglary* and *earthquake*, we use one Prolog rule for every possible state of the parents.
#   - The first rule covers the case in which *burglary* and *earthquake* are both true. The required rule is `alarm :- burglary, earthquake, p_alarm1`, with `p_alarm1` an auxiliary atom defined by means of the probabilistic fact `0.9::p_alarm1`. The point of adding this atom is to ensure that the probability of *alarm* in this case will be 0.9 as required.
#   - The second rule covers the case that *burglary* is true but *earthquake* is false. Note that *earthquake* being false is encoded using the "\+" symbol for negation (as in regular Prolog).
#   - The third rule covers the case that *burglary* is false and *earthquake* is true.
#   - The fourth case (*burglary* and *earthquake* are both false) does not require a rule. This is because, according to our Bayesian network, the probability of *alarm* is 0 in this case.

# %% [markdown] slideshow={"slide_type": "subslide"}
# We obtain the following ProbLog program.

# %% tags=["thebe-init"] slideshow={"slide_type": ""}
%%problog

0.7::burglary.
0.2::earthquake.
0.9::p_alarm1.
0.8::p_alarm2.
0.1::p_alarm3.

alarm :- burglary, earthquake, p_alarm1.
alarm :- burglary, \+earthquake, p_alarm2.
alarm :- \+burglary, earthquake, p_alarm3.

evidence(alarm,true).

query(burglary).
query(earthquake).

# %% [markdown] slideshow={"slide_type": ""}
# When pressing 'Evaluate', ProbLog2 calculates the probability of there being a *burglary* or an *earthquake*, given the evidence that the *alarm* rang. The resulting marginals are: $P(burglary)=0.9896$ and $P(earthquake)=0.2275$.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Probabilistic clauses ##

# %% [markdown] slideshow={"slide_type": "subslide"}
# While the above is a correct encoding of the given Bayesian network, it is perhaps not very intuitive due to the auxiliary atoms. Fortunately, ProbLog2 offers some syntactic sugar called **probabilistic clauses** to encode this in a more readable way. Above, we encoded the information that the conditional probability of an *alarm* given a *burglary* and an *earthquake* equals 0.9 using the rule `alarm :- burglary, earthquake, p_alarm1`, plus the probabilistic fact `0.9::p_alarm1`. We can replace both with a single probabilistic clause of the form `0.9::alarm :- burglary, earthquake`. This should be read as: if *burglary* and *earthquake* are true, this causes *alarm* to become true with probability 0.9 if there is a *burglary* and an *earthquake*. As this example illustrates, a probabilistic clause has a body, just like regular ProbLog rules, and a head. The difference is that now, the head is annotated with a probability. By also using probabilistic clauses for the other rules in the ProbLog encoding of the Bayesian network, we get the following program.

# %% tags=["thebe-init"] slideshow={"slide_type": "subslide"}
%%problog

0.7::burglary.
0.2::earthquake.

0.9::alarm :- burglary, earthquake.
0.8::alarm :- burglary, \+earthquake.
0.1::alarm :- \+burglary, earthquake.

evidence(alarm,true).
query(burglary).
query(earthquake).

# %% [markdown] slideshow={"slide_type": ""}
# As you can verify by pressing 'Evaluate', this returns the same marginals as the 'plain' ProbLog encoding: $P(burglary)=0.9896$ and $P(earthquake)=0.2275$. This is not a coincidence: the two programs are equivalent (but the program with probabilistic clauses has the advantage of not needing any auxiliary atoms).
#
# [Probabilistic clauses documentation]
#
# [Probabilistic clauses documentation]: https://problog.readthedocs.io/en/latest/modeling_basic.html#probabilistic-clauses

# %% [markdown] slideshow={"slide_type": "slide"}
# ## First-order ##

# %% [markdown] slideshow={"slide_type": "subslide"}
# To illustrate the use of *first-order* ProbLog programs, we show below a first-order extension of the *Alarm* example.
#
# digraph alarm2 { burglary -> alarm; earthquake -> alarm; alarm -> "calls(john)"; alarm -> "calls(...)"; alarm -> "calls(mary)"; }
# Suppose there are $N$ people and each person independently *calls* the police with a certain probability, depending on the *alarm* ringing or not: if the *alarm* rings, the probability of *calling* is 0.8, otherwise it is 0.1. This can be modelled as follows. We again use probabilistic clauses and show the case $N=2$ (two people).

# %% tags=["thebe-init"] slideshow={"slide_type": "subslide"}
%%problog

person(john).
person(mary).

0.7::burglary.
0.2::earthquake.

0.9::alarm :- burglary, earthquake.
0.8::alarm :- burglary, \+earthquake.
0.1::alarm :- \+burglary, earthquake.

0.8::calls(X) :- alarm, person(X).
0.1::calls(X) :- \+alarm, person(X).

evidence(calls(john),true).
evidence(calls(mary),true).

query(burglary).
query(earthquake).

# %% [markdown] slideshow={"slide_type": ""}
# When pressing 'Evaluate', ProbLog2 calculates the probability of there being a *burglary* or an *earthquake*, given the evidence that both *john* and *mary* *called*. We obtain $P(burglary)=0.981939$ and $P(earthquake)=0.226851$.

# %% [markdown] slideshow={"slide_type": "subslide"}
# In general, any Boolean Bayesian network can be modeled in ProbLog using the above methodology. This can also be extended to non-Boolean Bayesian networks (in which some variables can take more than two possible values), by using annotated disjunctions with multiple atoms in the head.

# %% [markdown] slideshow={"slide_type": "slide"}
# ## Annotated disjunctions: Dealing with multi-valued variables ##

# %% [markdown] slideshow={"slide_type": "subslide"}
# Since the random variables in the Bayesian network are all Boolean, we only need a single literal in the head of the rules. We can extend the Bayesian network to have a multi-valued variable by indicating the severity of the *earthquake*. The literal `earthquake` now has three possible values `none`, `mild`, `heavy` instead of previously two (no or yes). The probabilities of each value is denoted by the **annotated disjunction** in `0.01::earthquake(heavy); 0.19::earthquake(mild); 0.8::earthquake(none)`. An annotated disjunction is similar to a probabilistic disjunction, but with a different head. Instead of it being one atom annotated with a probability, it is now a disjunction of atoms each annotated with a probability.

# %% tags=["thebe-init"] slideshow={"slide_type": "subslide"}
%%problog

person(john).
person(mary).

0.7::burglary.
0.01::earthquake(heavy); 0.19::earthquake(mild); 0.8::earthquake(none).

0.90::alarm :-   burglary, earthquake(heavy).
0.85::alarm :-   burglary, earthquake(mild).
0.80::alarm :-   burglary, earthquake(none).
0.10::alarm :- \+burglary, earthquake(mild).
0.30::alarm :- \+burglary, earthquake(heavy).

0.8::calls(X) :- alarm, person(X).
0.1::calls(X) :- \+alarm, person(X).

evidence(calls(john),true).
evidence(calls(mary),true).

query(burglary).
query(earthquake(_)).

# %% [markdown] slideshow={"slide_type": "subslide"}
# [Annotated disjunctions documentation]
#
# [Annotated disjunctions documentation]: https://problog.readthedocs.io/en/latest/modeling_basic.html#annotated-disjunctions
