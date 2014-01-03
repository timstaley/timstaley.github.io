####
Code
####
:slug: code

=====================
(See also: `Github`_)
=====================

For a full listing of my public repositories and to see what I've been 
doing lately, check out my `profile`_ on Github. 
If you're feeling whimsical you might like to run it through 
Dan Foreman-Mackey's `Open Source Report Card`_.

I've highlighted some of my repositories with brief descriptions below.


=========
Astronomy
=========

`voevent-parse`_
----------------
A lightweight library for parsing, manipulating, and generating 
`VOEvent <http://www.ivoa.net/documents/VOEvent/index.html>`_ XML packets,
(**i.e. machine-readable transient alerts**) 
built on `lxml`_. 
The aim of this library was to make working with VOEvent packets simpler and 
more intuitive - take a look at the 
`usage <https://github.com/timstaley/voevent-parse/blob/master/usage_example.py>`_
`examples <https://github.com/timstaley/voevent-parse/blob/master/new_voevent_example.py>`_ 
and judge for yourself. It's reasonably well 
`documented <http://voevent-parse.readthedocs.org/>`_.

Anyone trying to use ``lxml.objectify`` and struggling with namespace handling,
PyType annotations etc. might be interested in the first few function 
definitions 
`here <https://github.com/timstaley/voevent-parse/blob/ce3728a8e189b08d378b72e97b7c4625f9051f9f/voeparse/voevent.py>`_. 


 
`drive-ami`_ / `drive-casa`_
----------------------------
Two wrapper libraries which make heavy use of `pexpect`_ to make complex 
scripting of astronomical data reduction tools from Python more bearable.
The `CASA`_ package is quite widely used in the radio astronomy community
and so I hope drive-casa will be of use to others - I've put up some 
basic `docs <http://drive-casa.readthedocs.org/en/latest/>`_ 
accordingly.

`pyds9_ex`_
-----------
The `DS9`_ FITS file viewer is fully scriptable -
this little known feature makes it a potentially very powerful tool for quickly 
throwing together a GUI of sorts, allowing the user to jump around different 
FITS images, select regions, etc. There are already
`python bindings <http://hea-www.harvard.edu/RD/ds9/pyds9/>`_ for it, 
but these are pretty low level, providing direct access to the scripting 
interface in a command-line fashion. 
This wrapper was a very brief attempt to provide some convenience routines 
around that low-level functionality. 
I've no plans to work on it further currently, but if anyone out there's 
interested there has been some 
`discussion <https://github.com/ericmandel/pyds9/issues>`_ on how to 
develop pyds9 in the future.
 




.. _profile: http://github.com/timstaley?tab=repositories 
.. _Github: http://github.com/timstaley
.. _Open Source Report Card: http://osrc.dfm.io/timstaley

.. _voevent-parse: http://github.com/timstaley/voevent-parse
.. _lxml: http://lxml.de/

.. _pysovo: https://github.com/timstaley/pysovo

.. _drive-ami: http://github.com/timstaley/drive-ami
.. _drive-casa: http://github.com/timstaley/drive-casa
.. _pexpect: http://www.noah.org/wiki/pexpect
.. _CASA: http://casa.nrao.edu/

.. _ds9: http://hea-www.harvard.edu/RD/ds9/site/Home.html
.. _pyds9_ex: https://github.com/timstaley/pyds9_ex