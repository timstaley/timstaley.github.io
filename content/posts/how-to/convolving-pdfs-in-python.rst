#########################
Convolving PDFs in Python
#########################
:date: 2014-06-06
:tags: how to, Python, probabilistic programming, notebook, convolution,
    probability distribution function

.. image:: {filename}/images/scipy_sum_pdfs_example.png
   :alt: Convolving PDFs: An example with a tophat and a Gaussian kernel.
   :align: center
   :target: {filename}/images/scipy_sum_pdfs_example.png
   :height: 400px

`Show me the code already! (Link to online IPython Notebook.) <notebook_>`_

Recently I've been working on a project involving a bit of decision theory,
which I hope to get finished up and published soon. In the process of figuring
out how to calculate exactly what I need, I've also been exploring the landscape
of probabilistic programming within Python. There are a lot of potentially
relevant tools out there, with packages like Statsmodels_, `scikit-learn`_,
and PyMC_ all reaching maturity, with large feature-sets and
pretty good documentation.
Unfortunately, nothing did *quite* what I wanted, so I've ended up rolling
my own for much of it, learning to use pandas_ as a building
block along the way (which is awesome).
I explored a couple of problems that fit nicely into a single
notebook / post. So,
`here's my take on how to convolve PDFs in Python. <notebook_>`_,
and you can find the source `here <notebook-repo_>`_.

The short version is that I'd recommend two possible approaches - if your
PDFs are one-dimensional and your transform is well behaved, roll your own
SumRv (summed random variate) class using scipy.
Otherwise, you'll probably want to run importance
sampling and KDE-smoothing, using a weighted-KDE code like that in statsmodels.
In my (highly un-scientific) benchmarking, the latter approach is about 5 times
slower for a basic 1D PDF, so you could just adopt that approach anyway and keep
things simple.

Finally, I should note that this was very much a learning exercise - I'm no
expert in the above packages, so if you know a better way, please let me know!


.. _Statsmodels: http://statsmodels.sourceforge.net/
.. _scikit-learn: http://scikit-learn.org/stable/
.. _PyMC: http://pymc-devs.github.io/pymc/
.. _pandas: http://pandas.pydata.org/

.. _notebook: http://nbviewer.ipython.org/github/timstaley/ipython-notebooks/blob/compiled/probabilistic_programming/convolving_distributions_illustration.ipynb
.. _notebook-repo: https://github.com/timstaley/ipython-notebooks/blob/master/probabilistic_programming/convolving_distributions_illustration.ipynb