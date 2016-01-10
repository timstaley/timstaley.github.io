########
Research
########
:slug: research

Selected publications
=========================
For the most up-to-date listing of my publications, I suggest trying
`this ADS author query <ADS query_>`_,
which gives a comprehensive list including ASCL_ citations and Atels_.
Alternatively, see my manually curated
`ORCiD entry`_, which is less frequently updated (and limited to more traditional
publications), but a little easier to read.

.. _ADS query: http://labs.adsabs.harvard.edu/adsabs/search/?q=Staley%2C+T&year_from=2007&db_f=astronomy&no_ft=1&bigquery=&aut_f=-(%220%2FStaley%2C+A%22)&page=1
.. _ASCL: http://ascl.net/
.. _Atels: http://www.astronomerstelegram.org/
.. _ORCiD entry: http://orcid.org/0000-0002-4474-5253


A radio jet from the optical and x-ray bright stellar tidal disruption flare ASASSN-14li
-----------------------------------------------------------------------------------------
Published in `Science (2016) <http://www.sciencemag.org/content/351/6268/62>`_

A high-impact publication about a transient flare event, thought to be caused by
a star accreting onto a black hole. The work made extensive use of our software
tooling (and close collaboration with the AMI team)
to achieve unprecedented temporal-resolution in the radio-lightcurve and a fast
turnaround of the analysis.

Coverage in the popular media was quite extensive, examples below:

- `Washington post <https://www.washingtonpost.com/news/speaking-of-science/wp/2015/11/27/scientists-just-caught-a-black-hole-swallowing-a-star-and-burping-a-bit-back-out/>`_
- `Huffington post <http://www.huffingtonpost.com/entry/black-hole-ate-star-burped_565cbaace4b079b2818b5b90>`_
- `Weather Network <http://www.theweathernetwork.com/news/articles/star-eating-black-hole-highlights-universes-cosmic-elegance/60404/>`_
- And the infamous `Daily Mail <http://www.dailymail.co.uk/sciencetech/article-3336226/Massive-black-hole-caught-devouring-star-burping-plasma-speed-light.html>`_

Chimenea and other tools: Automated imaging of multi-epoch radio-synthesis data with CASA
------------------------------------------------------------------------------------------
Published in `Astronomy and Computing (2015) <http://www.sciencedirect.com/science/article/pii/S2213133715000736>`__

Describes how we combined multiple legacy software components together with
Python interfacing code and some novel algorithms to automate a previously
labour intensive data analysis task. The outcome is greatly improved response
times to transient astronomical events,
and perhaps just as importantly, a *reproducible* reduction process.

The LOFAR Transients Pipeline
-------------------------------
Published in `Astronomy and Computing (2015) <http://www.sciencedirect.com/science/article/pii/S2213133715000207>`__

A thorough reference work laying out the core algorithms behind the TraP_, a
transients-detection and cataloguing pipeline developed initially for LOFAR.
TraP is the first pipeline of its kind to be fully open-sourced and
comprehensively documented. Technically, the codebase is interesting for its
extensive use of SQL procedures to perform in-database analysis and processing
of spatial data. The accompanying data-exploration and visualisation tool
Banana_ is also quite novel in astronomy - we pushed Django to its limits to
perform detailed queries on the dataset via a web-based interface that allowed
fluid user interaction without complex local installation procedures.

More detail can be found `on the code page </code#tkp-trap>`_

.. _TraP: https://github.com/transientskp/tkp
.. _Banana: https://github.com/transientskp/banana


--------------------

Background: A software ecosystem for transient astronomy
==================================================================

Since October 2011 I've been working with the `4 Pi Sky project`_, 
which (broadly) aims to automate both the detection and follow-up observation
of astronomical transients, motivated in large part by the next generation
of large radio telescopes.

Nuts and bolts, transient triggers
----------------------------------
A fair portion of my work to date has been developing basic software 
infrastructure, in the form of various small libraries and tools for automating 
processing of astronomical alerts and unattended data reduction.
This sort of stuff is quite satisfying when done well,
but I wouldn't really classify it as 'research' in its own right. 
However, the efforts are beginning to bear fruit.
With the help of our collaborators at the MRAO, 
since mid-2012 we have been triggering automatic observations with the 
`AMI`_ Large Array, with
`three <http://ukads.nottingham.ac.uk/abs/2013MNRAS.428.3114S>`_
`papers <http://adsabs.harvard.edu/abs/2014MNRAS.440.2059A>`_
`published <http://adsabs.harvard.edu/abs/2015MNRAS.446L..66F>`_
to date, and further work in prep.
These tools are all open-sourced and publicly available (more details
on the `code page <{filename}code.rst>`_).
 
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
A paper and open-source release are now available - see the
`code </code>`_ page for details.

Application of active-learning / Bayesian decision theory to transient follow-up
--------------------------------------------------------------------------------
Finally, the most abstract (but potentially most exciting)
aspect of my current research addresses the problem of automating
transient follow-up - how to decide what to observe, and when.
This is still a work in progress, but I hope to start presenting early results
in the next couple of months.

--------------


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
links, or via the `arxiv <http://arxiv.org/abs/1404.5907>`_:
  
- `One page summary (tiny). <http://www.astro.soton.ac.uk/~ts3e11/files/Staley_thesis_summary.pdf>`_  
- `Complete thesis, online format (23mb) <http://www.astro.soton.ac.uk/~ts3e11/files/Staley_thesis_online_version.pdf>`_  
  (i.e. with hyperlinks - note these don't show up when viewed via the Chrome integrated PDF reader)
- `Complete thesis, print format (23mb). <http://www.astro.soton.ac.uk/~ts3e11/files/Staley_thesis_print_version.pdf>`_ 

.. _4 Pi Sky project: http://4pisky.org

.. _AMI: http://www.mrao.cam.ac.uk/facilities/ami/

.. _lofar-tkp: http://www.transientskp.org/
.. _uva:  http://www.astro.uva.nl/
.. _lofar: http://en.wikipedia.org/wiki/LOFAR