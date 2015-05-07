############################################
How to pip install NumPy in two seconds flat
############################################

:date: 2015-05-07
:tags: how to, Python, pip, virtualenv, offline, wheel, tox, numpy, speed up

I've `previously posted <{filename}/posts/how-to/python-pip-offline.rst>`_
on making pip usable offline by caching package files in a local directory.
That approach can probably be considered out-of-date now, though the
information may be useful if you're stuck with an old version of pip for some
reason. Mostly you should just be able to run::

    pip install --user --upgrade pip

or suchlike, and get the latest version (6.1.1 as of writing).
This gives you a much improved alternative:

Since version 1.6 / 6.0, (see `release notes`_), Pip provides support for the
Wheel_ format, allowing caching of pre-built packages. Now we're at pip
version 6.1, this seems to be quite stable and useful.

The new wheel format not only provides caching, but does away with build times,
after the initial build-for-the-cache (this is awesome!).
You can find usage details here:
https://pip.pypa.io/en/latest/reference/pip_wheel.html

Note that you don't have to supply the wheel-dir on the command-line
every time (default is current working directory, which is not what you want
for sharing e.g. a single numpy build between projects) - you can set it
via environment variables, e.g. (in your ``.bashrc``)::

    export WHEELHOUSE="${HOME}/.cache/pip/wheelhouse"
    export PIP_FIND_LINKS="file://${WHEELHOUSE}"
    export PIP_WHEEL_DIR="${WHEELHOUSE}"

Then::

    pip install wheel   #Only needed if caching new packages
    pip wheel numpy     #First time only, to seed the cache
    pip install numpy   #Takes less than 2 seconds. Amaze.

(Hat-tip to @ionelmc for pulling this information into one easy-to-read
`post <http://blog.ionelmc.ro/2015/01/02/speedup-pip-install/>`_, which I found
when infuriated by tox_ build-times.
There's also a nice
`write-up <http://lucumr.pocoo.org/2014/1/27/python-on-wheels/>`_ of the
wheel format by Armin Ronacher (of flask fame), but although I came across
and skim-read the article some months ago, I but never got around to actually
trying it out till now. So it goes.)


.. _release notes: https://pip.pypa.io/en/latest/news.html
.. _Wheel: https://wheel.readthedocs.org/en/latest/
.. _tox: https://tox.readthedocs.org/