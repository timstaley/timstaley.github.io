############################################
How to pip install NumPy in two seconds flat
############################################

:date: 2015-05-07
:tags: how to, Python, pip, virtualenv, offline, wheel, tox, numpy, speed up

*Edit, July 2016:*

A mere two weeks after I posted this, pip version 7 was released and
changed things again. If you have the wheel library and pip version 7 or
above, wheel building and caching is now switched on and run by default,
you just need to ``pip install`` away and the caching happens in the background.

This can result in mild disbelief when numpy installs near-instantly the second
time around, with no configuration! Anyway, I'll leave the rest of this post
here for posterity - the note about caching the pip and wheel packages using
older pip versions may still be useful to some.

------------------------------------



I've `previously posted <{filename}/posts/how-to/python-pip-offline.rst>`_
on making pip usable offline by caching package files in a local directory.
That approach can probably be considered out-of-date now, though the
information is still useful if you're stuck with an old version of pip.
I expected to be able to run::

    pip install --user --upgrade pip

to get the latest version of pip whenever I was logged in, but this doesn't seem
to work, so unless you're going to do a system-wide (``sudo``) upgrade
you still need to upgrade pip for each new virtualenv you create.
You can do that offline (if you're prepared) using the following pip commands.
First, while you're still online (you only have to run this once, to download
the ``pip`` and ``wheel`` source tarballs)::

    pip install --download=$HOME/.cache/pip/tarballs pip wheel

Then, when you've just created a new virtualenv (while on or offline)::

    pip install --no-index --find-links=file://$HOME/.cache/pip/tarballs pip wheel

I recommend saving that second command in a script (or you could even alias it
to something).

So, now we've got the latest pip (version 6.1.1 as of writing).
This gives you a much improved alternative to caching source-tarballs.
Since version 1.6 / 6.0, (see `release notes`_), Pip provides support for the
Wheel_ format, allowing caching of pre-built packages.
With pip version 6.1, this seems to be stable and very useful.

The new wheel format not only provides download-caching,
but does away with build times, by caching a pre-built binary on command.
This is awesome - it makes virtualenvs feel much more lightweight (no
waiting five-to-ten minutes to spin one up with numpy, scipy, and astropy),
It's also a massive boon if you're running automated install testing with tox_,
since this may run a fresh install for each test-run.
You can find usage details here:
https://pip.pypa.io/en/latest/reference/pip_wheel.html
but I'll give you the basics below.

First, we set up some environment variables, so that you don't have to supply
the wheel-cache directory on the command-line
every time (default is current working directory, which is not what you want
for sharing e.g. a single numpy build between projects). You can set it
via environment variables, e.g. (in your ``.bashrc``)::

    export WHEELHOUSE="${HOME}/.cache/pip/wheelhouse"
    export PIP_FIND_LINKS="file://${WHEELHOUSE}"
    export PIP_WHEEL_DIR="${WHEELHOUSE}"

Then (e.g. for a ``numpy`` install)::

    pip install wheel   #Only needed if caching new packages
    pip wheel numpy     #First time only, to seed the cache.
    pip install numpy   #Takes less than 2 seconds. Amaze.

And you're away.

Hat-tip to `@ionelmc`_ for pulling this information into one easy-to-read
`post <http://blog.ionelmc.ro/2015/01/02/speedup-pip-install/>`_, which I found
when infuriated by tox_ build-times.
There's also a nice
`write-up <http://lucumr.pocoo.org/2014/1/27/python-on-wheels/>`_ of the
wheel format by Armin Ronacher (of flask fame), but although I came across
and skim-read the article some months ago, I but never got around to actually
trying it out till now. So it goes.


.. _release notes: https://pip.pypa.io/en/latest/news.html
.. _Wheel: https://wheel.readthedocs.org/en/latest/
.. _tox: https://tox.readthedocs.org/
.. _@ionelmc: https://twitter.com/ionelmc