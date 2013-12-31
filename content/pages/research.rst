########
Research
########
:slug: research

======
Recent
======

Since October 2011 I've been working with the `4 Pi Sky project`_, 
which (broadly) aims to automate both the detection and follow-up observation
of astronomical transients, motivated in large part by the next generation
of large radio telescopes.

Nuts and bolts, transient triggers
----------------------------------
A fair portion of my work to date has been developing basic software 
infrastructure, in the form of various small libraries and tools for automating 
processing of astronomical alerts and unattended data reduction 
(see the `code <{filename}code.rst>`_ page).
This sort of stuff is quite fun and satisfying when done well,
but I wouldn't really classify it as 'research' in its own right. 
However, the efforts are beginning to bear fruit. 
With the help of our collaborators at the MRAO, 
since mid-2012 we have been triggering automatic observations with the 
`AMI`_ Large Array, with one `paper`_ published and more in prep.  
 
Transient discovery with the 'Trap'
-----------------------------------
I've also been helping with development of a software project born out of the
`LOFAR-TKP`_ group at `UvA`_.
The `Trap`_ is a transients detection pipeline 
written primarily for use with data from 
`LOFAR`_ - a low frequency radio array. LOFAR will observe at ~10s to 100s 
of megahertz rather than the usual gigahertz range, 
giving us a new window on the radio sky.
While LOFAR presents a particular challenge due to the sheer volume
of data produced, the algorithms being developed are applicable to a range 
of transient astronomy projects. 
A paper and open-source release are in prep.

=============
Lucky Imaging
=============

**(PhD, 2007 - 2011)**

*NB link to* thesis_ *at end.*

My PhD research was focused upon algorithm and software development for a 
technique called 
`lucky imaging <http://www.ast.cam.ac.uk/research/lucky>`_.
Normally, ground based astronomy is limited in resolution due to time-evolving 
localised fluctuations in the refractive index of the atmosphere. 
Like grease on a camera lens, the atmospheric turbulence blurs the image in a 
long exposure. 
However, by taking very short exposures (i.e. at frame rates of around 25 frames 
per second and above),
we can 'freeze' these atmospheric effects and pick out moments when the blurring 
is at a minimum - so called 'lucky images.' We do this by tracking a bright 
object in every frame (the 'guide star'), which we also use to align the images 
before we add them to get the final result. 
For very bright objects such as planets, you can even do this at home 
with a small telescope and a webcam.

For many years the application of lucky imaging to general purpose astronomy was limited due to 
the levels of readout noise at high frame rates. However, with the development of electron-multiplying
CCDs, photon-counting performance at high frame rates became a possibility.

Over the course of my PhD I refined the data reduction techniques for lucky imaging,
optimising both the method for tracking the guide star and the thresholding algorithm used to 
perform photon counting. I also developed a high-performance data reduction pipeline
capable of reducing data from a multi-CCD mosaic camera at around 200 megabytes a second - 
lucky imaging with large format CCDs rapidly becomes a serious data handling challenge.  

I also did some work on Monte-Carlo simulation of lucky imaging data, 
both for simulation of combined adaptive-optics + lucky imaging systems, and for development 
of more sophisticated wide-field lucky imaging algorithms.

Thesis
------

If you're interested in the details you can download my thesis via the following
links:
  
- `One page summary (tiny). <http://www.astro.soton.ac.uk/~ts3e11/files/Staley_thesis_summary.pdf>`_  
- `Complete thesis, online format (23mb) <http://www.astro.soton.ac.uk/~ts3e11/files/Staley_thesis_online_version.pdf>`_  
  (i.e. with hyperlinks - note these don't show up when viewed via the Chrome integrated PDF reader)
- `Complete thesis, print format (23mb). <http://www.astro.soton.ac.uk/~ts3e11/files/Staley_thesis_print_version.pdf>`_ 

.. _4 Pi Sky project: http://www.4pisky.soton.ac.uk/

.. _AMI: http://www.mrao.cam.ac.uk/facilities/ami/
.. _paper: http://ukads.nottingham.ac.uk/abs/2012arXiv1211.3115S

.. _lofar-tkp: http://www.transientskp.org/
.. _uva:  http://www.astro.uva.nl/
.. _trap: http://docs.transientskp.org/
.. _lofar: http://en.wikipedia.org/wiki/LOFAR