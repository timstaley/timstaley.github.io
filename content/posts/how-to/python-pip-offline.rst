########################
Using python pip offline
########################

:date: 2014-03-20
:tags: how to, python, pip, virtualenv, offline

After you've been coding in python for a while, and you've been bitten by a
few package-version incompatibility bugs, it gets to the stage where the
**first** thing you do upon starting a new project, is fire up a new
virtualenv_.

The second thing you (might) do is curse like a sailor upon realising
you'll have to re-download, compile and install numpy, scipy, matplotlib, etc.
Especially if you're on a slow connection, or worse yet, completely offline.

Fortunately, the python package installer, pip_, has been coming on in
`leaps and bounds <http://www.pip-installer.org/en/latest/news.html>`_ recently,
with many improvements to the package caching behaviour,
most noticeably improved flag syntax. It's taken me a while
to put together all the relevant details, change notes, and workflow, plus the
`stackoverflow question <http://stackoverflow.com/questions/4806448/how-do-i-install-from-a-local-cache-with-pip>`_
is a bit outdated in places, so I thought I'd post.

First off, make sure you've got the most recent pip version (1.5.4 as of
writing). If you're on \*buntu 12.04 and previously installed it via apt-get,
then I'd recommend:

.. code-block:: bash

   sudo apt-get remove python-pip
   sudo easy_install -U pip

If pip was already a custom install then you're probably fine to just run

.. code-block:: bash

   sudo pip install -U pip

While you're at it, might as well grab the latest version of
virtualenv, virtualenv-clone, and virtualenvwrapper:

.. code-block:: bash

   sudo pip install -U virtualenv-clone virtualenvwrapper

That's the last sudo'ing - from here on out we keep the system clean!

So, improvement number one: with the latest pip, you can set up a cache folder
to keep a copy of all your favourite packages.

The full details can be found
`here <http://www.pip-installer.org/en/latest/user_guide.html#fast-local-installs>`_,
but in short, you can just drop two tiny scripts into the folder you want to use
as your package cache directory, e.g. as ``download.sh``::

    #!/usr/bin/env bash
    PIP_CACHE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    pip install --download=$PIP_CACHE $*

and ``install.sh``::

    ##!/usr/bin/env bash
    PIP_CACHE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    echo "USING CACHE: ${PIP_CACHE}"
    pip install --no-index --find-links=file://$PIP_CACHE  $*

Where the first line is just
`some bash voodoo <http://stackoverflow.com/a/246128/725650>`_
to locate the parent directory of the shell scripts.
Usage is then something like the following:

.. code-block:: bash

    #Ahead of time
    cd project-folder
    ~/pip_cache/download.sh -r requirements.txt
    ~/pip_cache/download.sh someotherpackage

    #When creating a new virtualenv offline
    mkvirtualenv foo
    cd project-folder
    ~/pip_cache/install.sh -r requirements.txt
    ~/pip_cache/install.sh someotherpackage

(assuming you dropped the pip scripts into *~/pip_cache*)
which will leave a neat selection of *tar.gz* package tarballs in your cache
folder.

Of course, this still leaves you with a long wait while scipy compiles, but
this too is fixable. One option might be to inherit system-packages upon
creating a new virtualenv, but then you're back to choosing between ``sudo pip``
or ancient ``apt`` packages.
The more explicit, controllable approach is to
create a 'common-core' virtualenv template containing your commonly used large
packages, then ``virtualenv-clone`` it whenever you want to start a new project,
e.g.

.. code-block:: bash

    cd ~/.virtualenvs
    virtualenv-clone template-env some-new-env

Note that this comes with a health warning - it seems ``virtualenv-clone`` does
not create a full copy, instead it copies some things and symlinks others,
so your new virtualenv will in fact be partially reliant on the template one!
But as long as you're aware of that issue, it's a great way to save
compile-time.

If you're going to be working offline you'll want to make sure
you cache all *suggested* as well as required package dependencies.
For example, ``ipython`` does not, by default, come with all the dependencies
needed to run the notebook (i.e. jinja2, pyzmq, etc).
However, you **can** grab these by specifying the package name with an ``[all]``
suffix, e.g.

.. code-block:: bash

    pip install ipython[all]

Oh, and one last thing. With a fresh virtualenv,

.. code-block:: bash

    pip install scipy

is **still** broken - it fails unless you've installed numpy first, for some
reason. I can't be bothered to dig up the bug report.
I'll leave you with a basic ``requirements.txt`` for your template
virtualenv::

    numpy
    scipy
    ipython[all]
    matplotlib


Footnote: you can use a pip-cache in fully automated fashion to save repeated
package downloads (and this has been available for a while) - simply drop the
`relevant line <http://stackoverflow.com/a/15948679/725650>`_ into your
*~/.pip/pip.conf* file, but I prefer the methods above - these give you
fine grained control to download and install separately, and also to
choose to grab a fresh copy from PyPI (by reverting to usual behaviour)
when you'd rather do so.


.. _virtualenv: http://www.virtualenv.org/en/latest/virtualenv.html
.. _pip: http://www.pip-installer.org/en/latest/