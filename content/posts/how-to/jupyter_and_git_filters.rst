##########################################
Making Git and Jupyter Notebooks play nice
##########################################

:date: 2017-02-19
:tags: git, jupyter, ipython, notebooks, jq, JSON, best practices


**tl;dr:** `jq`_ rocks for JSON mangling. Use it to make powerful git clean
filters, e.g. when stripping out unwanted cached-data from Jupyter notebooks.

For a year or so now I've been using Jupter_ notebooks as a means to produce
tutorials and other documentation (see e.g. the `voeventdb.remote`_ tutorial_).
It's a powerful medium, providing
a good compromise between ease-of-editing and the capability to
interleave text, code, intermediate results, plots, and even nicely-typeset
LaTeX-encoded equations. I've even gone to far as to urge its adoption in
recent `conference talks`_.

However, this powerful interface inherits the age-old curse
of WYSIWYG_ editors - the document-files tend to contain more than just
plain-text, and therefore are not-so-easy to handle with standard version-control
tools. In the case of Jupyter, the format doesn't stray too far from our
comfortable plain-text territory - the *ipynb* format is just a custom JSON
data-structure, with the occasional base-64 encoded blob for images and other
binary data. Which means version-control systems such as Git *can* handle it
quite well, but diff-comparing different versions of a complex notebook
quickly becomes a chore as you scroll past long blocks of unintelligible base-64
gibberish.

.. _conference talks: https://github.com/timstaley/sustainable-software-in-astro/blob/master/README.md
.. _Jupter: https://jupyter.readthedocs.io/en/latest/tryjupyter.html
.. _jq: https://stedolan.github.io/jq/
.. _tutorial: http://voeventdbremote.readthedocs.io/en/latest/tutorial/quickstart.html
.. _voeventdb.remote: http://voeventdbremote.readthedocs.io
.. _WYSIWYG: https://en.wikipedia.org/wiki/WYSIWYG