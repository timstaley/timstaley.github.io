Code
####
:slug: code


.. raw:: html

    <h3>(See also:
        <a href="http://github.com/timstaley">
            Github profile <i class="fa fa-github"></i>
            </a> )
    </h3>


For a full listing of my public software projects, and to find out what I've been
doing lately, see my `profile`_ on Github.

I've highlighted some projects with brief descriptions below.

-----------

Sole-author projects
====================
Things I've made:


drive-ami_ / drive-casa_
----------------------------
*Built with: Python, pexpect.*

Two interface libraries which make heavy use of `pexpect`_ to enable complex
scripting of astronomical data reduction tools from Python.
The `CASA`_ package is quite widely used in the radio astronomy community,
so I've put up some basic
`docs <http://drive-casa.readthedocs.org/en/latest/>`_
to help others get started.

amisurvey_ / chimenea_
-----------------------
*Built with: Python, drive-ami, drive-casa.*

These packages represent a (telescope-specific) end-to-end data-reduction
pipeline and the more generally applicable data-reduction algorithm used
therein. Both build on the interfacing packages described above, introducing
various data-structures to allow a higher-level view of the data-flow.


voevent-parse_
----------------
*Built with: Python, LXML.*

A lightweight library for parsing, manipulating, and generating
VOEvent_ XML packets, (*i.e. machine-readable transient alerts*)
built on lxml_.
The aim of this library was to make working with VOEvent packets simpler and
more intuitive - take a look at the
`usage examples`_ and judge for yourself.
It's reasonably well
`documented <http://voevent-parse.readthedocs.org/>`_.
As of version 0.8 (Jan 2015) voevent-parse is fully Python 3 compatible.

Anyone trying to use ``lxml.objectify`` and struggling with namespace handling,
PyType annotations etc. might be interested in the first few function
definitions
`here <https://github.com/timstaley/voevent-parse/blob/ce3728a8e189b08d378b72e97b7c4625f9051f9f/voeparse/voevent.py>`_.

fourpiskytools_
----------------
*Built with: Python, voevent-parse, Comet.*

A 'quick-start' template to help astronomers get started sending or receiving
VOEvents. Essentially provides a stock configuration for starting
Comet_ and connecting it to some scripts built with voevent-parse.
This allows you to connect to our VOEvent broker and get desktop
notifications when a VOEvent arrives - more info, and some background on
VOEvents, can be found `here <getting-started-voevents_>`_.



Coelacanth_
-----------
*Built with: C++, CMake, Boost, TBB, Minuit2, UNURAN, UnitTest++.*

"Codes for EMCCD and Lucky-Imaging Analysis", around 15K lines of C++ code that
grew out of my PhD_ project. The data-volumes and limited processing power
available on-site (i.e. while up a mountain observing) required a set of
high-performance codes for specialized data-reduction. Part of the challenge
was to implement complex algorithms such as Drizzle_ in C++ in a maintainable
fashion - you can see the `results here <drizzle implementation_>`_. The final
pipeline made use of the `Thread Building Blocks <TBB_>`_ `pipeline`_ pattern
to achieve excellent throughput.

-----------

Collaborator projects
=====================
Things I've helped other people to make:

TKP TraP_
---------
An astronomical transient-detection pipeline for ingesting radio-synthesis
images. In a nutshell, we extract source intensities from images,
then build a lightcurve catalog and search it for
variability. This requires some fairly involved NumPy routines for the
source-extraction (all in-house Python, at least for the first edition), and
some hairy SQL queries for building and searching the catalogs.
TraP received its first `open release <TraP release_>`_ in Feb 2015, with
an `accompanying paper <TraP paper_>`_ providing an extensive reference on the
underlying algorithms.

I wrote a short summary piece on TraP which you can see `here <TraP post_>`_,
and I've also given a couple of short summary talks_ introducing it.

See also: Banana_, a Django-based
web-interface for exploring and visualising the results.

-----------

Bric-a-brac
===========
Less substantial, but possibly still useful:

- autocrunch_
    A Python script demonstrating how to use `pyinotify`_ to monitor a local
    directory for files that have been transferred with rsync,
    then process them in a parallel fashion using a multiprocessing pool
    (via whatever Python reduction process you care to define).
    This has been road-tested quite a bit, and includes decent
    logging and error handling.

- pyds9_ex_
    The `DS9`_ FITS file viewer is fully scriptable, but only has a low-level
    interface.
    This wrapper provides some convenience routines
    around that low-level functionality.

- python-imap-monitoring_
    Procmail for the Python + GMail generation. Monitor your GMail inbox and
    trigger Python scripts in response to special emails.

- `FSlint for humans`_
    Some scripts to parse the output from FSlint_ into a useful CSV summary,
    allowing the user to locate the largest duplicate files, and who they belong
    to, on a multi-user cluster with lots (~100's of TB) of disk space.





.. _profile: http://github.com/timstaley?tab=repositories 
.. _Github: http://github.com/timstaley
.. _Open Source Report Card: http://osrc.dfm.io/timstaley

.. _Coelacanth: https://github.com/timstaley/coelacanth
.. _PhD: http://uk.arxiv.org/abs/1404.5907
.. _Drizzle: http://en.wikipedia.org/wiki/Drizzle_(image_processing)
.. _Drizzle implementation: https://github.com/timstaley/coelacanth/blob/ec97ae1e39de1336734b8dd09b638c616944b8e0/coela_core/src/implementation/drizzle.cc#L65
.. _TBB: https://www.threadingbuildingblocks.org/
.. _pipeline: http://www.threadingbuildingblocks.org/docs/help/tbb_userguide/Working_on_the_Assembly_Line_pipeline.htm


.. _drive-ami: http://github.com/timstaley/drive-ami
.. _drive-casa: http://github.com/timstaley/drive-casa
.. _pexpect: http://www.noah.org/wiki/pexpect
.. _CASA: http://casa.nrao.edu/

.. _amisurvey: https://github.com/timstaley/amisurvey
.. _chimenea: https://github.com/timstaley/chimenea

.. _voevent-parse: http://github.com/timstaley/voevent-parse
.. _usage examples: http://voevent-parse.readthedocs.org/en/master/examples.html

.. _VOEvent: http://www.ivoa.net/documents/VOEvent/index.html
.. _lxml: http://lxml.de/
.. _fourpiskytools: https://github.com/timstaley/fourpiskytools
.. _Comet: http://comet.transientskp.org/en/1.2.1/
.. _getting-started-voevents: http://4pisky.org/2014/11/12/getting-started-with-voevents/

.. _TraP: http://docs.transientskp.org/
.. _TraP release: https://github.com/transientskp/tkp/
.. _TraP paper: http://adsabs.harvard.edu/cgi-bin/bib_query?arXiv:1503.01526
.. _Banana: https://github.com/transientskp/banana
.. _TraP post: http://4pisky.org/2015/03/06/trap-r2/
.. _talks: {filename}talks.rst


.. _autocrunch: http://github.com/timstaley/autocrunch
.. _pyinotify: http://github.com/seb-m/pyinotify

.. _ds9: http://hea-www.harvard.edu/RD/ds9/site/Home.html
.. _pyds9_ex: https://github.com/timstaley/pyds9_ex

.. _python-imap-monitoring: https://github.com/timstaley/python-imap-monitoring-demo

.. _FSLint: http://en.flossmanuals.net/FSlint/
.. _FSLint for humans: https://github.com/timstaley/lofar_data_management