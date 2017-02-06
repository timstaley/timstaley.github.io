#####
Talks
#####
:slug: talks

I've given a number of presentations at seminars and conferences.
Most of them are available online; I've listed each below with a brief summary.
The PDF files are available in bulk
`via github <https://github.com/timstaley/presentations>`_.

Jump to:

* `Talks on software`_
* `Talks on transient astronomy`_
* `Talks on lucky imaging`_


-----------


Talks on software
-----------------

VOEventDB and Sustainable Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Hotwiring the Transient Universe V, Villanova, PA, October 2016*

.. raw:: html

    <a href="http://timstaley.co.uk/sustainable-software-in-astro/">
        <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Online slides
        </button>
    </a>
    <a href="https://github.com/timstaley/sustainable-software-in-astro/blob/master/proceedings_full.md">
        <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span>  Source and summary on Github
        </button>
    </a>

An invited talk for an audience lying at the intersection of astronomy and
software development. I gave a brief teaser-introduction to VOEventDB,
and tried to use parts of that project to illustrate some points on the
wider topic of sustainable software.



A brief introduction to version control systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Southampton, November 2013*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2013-11_DVCS-intro_Soton/Brief_introduction_to_version_control_systems.pdf?raw=true">
        <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
        </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/a-brief-introduction-to-version-control-systems" target="_blank">
        <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
        </button>
    </a>



A short (fifteen minute) explanation of version control, aimed at an academic
audience.  The goal was to introduce the underlying concepts of version control
systems, and give an idea of when they are most useful.


-----------


Talks on transient astronomy
------------------------------------------

Which transient, when?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Southampton colloquia series, May 2015*

*Hotwiring the Transient Universe IV, Santa Barbara, May 2015*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/raw/master/2015-05_Which-transient-when/which_transient_when_2015_long.pdf">
        <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/which-transient-when-a-utility-function-for-transient-followup-scheduling" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

I gave this talk to the astronomy group in Southampton,
and a shorter version at `Hotwired IV`_. Here's the abstract:

Next-generation astronomical facilities such as the LSST and the SKA will be
game-changers, allowing us to observe the entire southern sky and track
changing sources in near real-time. Keeping up with their alert-streams
represents a significant challenge - how do we make the most of our limited
telescope resources to follow up 100000 sources per night?

The biggest problem here is classification - we want to find the really interesting
transients and spend our time watching those. However, classification based
on the initial survey data can only get you so far - we'll need to use
robotic follow-up telescopes for rapid-response observations, to give us more
information on the most promising targets. To get the most science done, we
need to be smart about scheduling that follow-up. We're exploring use of
active learning algorithms (AKA Bayesian Decision Theory) to solve this
problem, building a framework that allows for iterative refinement of a
probabilistic classification state. Because there are no algorithms that fit
this problem 'out-of-the-box', we've built our own analysis framework using
the emcee and PyMultiNest packages to power the underlying Bayesian
inference. I'll give an overview of how our proposed system fits into the
wider context of an automated astronomy ecosystem, then give a gentle
introduction to Bayesian Decision Theory and how it can be applied to this
problem.

.. _Hotwired IV: http://lcogt.net/hotwired-iv-science-topics/



How to build a TraP: An image-plane transient-detection tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Southampton lunchtime seminar January 2015*

*Oxford SPIMAX talk, January 2015*

*Hotwiring the Transient Universe IV, Santa Barbara, May 2015*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2015-01_TraP-an-image-plane-transient-discovery-tool/TraP-image-plane-transient-discovery.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/how-to-build-a-trap-an-imageplane-transientdiscovery-tool" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

The TraP (http://ascl.net/1412.011) is a pipeline for processing streams of
astronomical image-data in near real-time with the aim of identifying transient
and variable sources.
This talk will give you a working understanding of what the TraP does at the
algorithmic level, to allow you to judge for yourself if it's relevant to your
work, or if you might be able to reuse parts of it in another context.

In the first half I give a brief recap on the kinds of astronomical
transients we hope to see in image-plane radio surveys, and how new telescopes
such as LOFAR are changing the parameters of what's possible in the radio-domain.
I then give an overview of how the TraP works, using plenty of diagrams
(and no code!).
Finally I talk a little bit about the development model behind TraP,
and how you can get started with it if you're interested.


From gamma-ray to radio: Multi-wavelength follow-up in the first five minutes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*RAS LT2 meeting, London, November 2014*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2014-11_gamma-ray-to-radio_RAS_LT2/gamma-ray-to-radio.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/from-gammaray-to-radio-multiwavelength-followup-in-the-first-five-minutes" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

In this short talk I cover some research highlights from the `4 Pi Sky`_ project,
including recent successes in fast radio follow-up and exploratory work on the
potential of radio observations for transient classification.
Finally I introduce our work on making the VOEvent standard more accessible to
the astronomical community, with the long-term goal of enabling more optimal
automated follow-up strategies.

.. _4 Pi Sky: http://4pisky.org


Tunable algorithms for transient follow-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*LOFAR-TKP meeting, Jodrell Bank, September 2014*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/raw/master/2014-09_Tunable-algos-for-transient-followup_Jodrell/tunable_algos_for_transient_followup.pdf">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/tunable-algorithms-for-transient-followup" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

This talk gives a gentle introduction to Bayesian decision theory, a methodology
I'm trying to apply to the problem of automated follow-up prioritisation and
scheduling.


Training your astronomy robots to work as a team
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Radio transients with SKA pathfinders, South Africa, July 2013*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2013-07_SKA-Transients_ZA/training_your_astro_robots_to_work_as_a_team.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/training-your-astronomy-robots-to-work-as-a-team" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

I present a case that the astronomy community is missing a part of the puzzle
for the next era of automated big-survey astronomy: we currently have very
little published work on target prioritization and optimized observation
scheduling. This talk also highlights some sociological issues surrounding the
sort of open collaboration needed to make optimal use of globally distributed
observatories,
and shows some preliminary work on generally-applicable classification methods.


Fast radio follow-up
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*LOFAR-TKP meeting, Amsterdam, December 2012*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2012-12_Fast-Radio-Followup_Amsterdam/Fast_radio_followup.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/fast-radio-followup" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

An iterated version of the earlier talk on ALARRM_. This version delves a little
deeper into why early-time radio follow-up of GRBs is interesting, and touches
on the problem of collaborative transient follow-up.


Fast radio follow-up of GRBs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*SKA-KAT offices, Capetown, November 2012*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2012-11_Ami-GRBS_Capetown/Fast_radio_followup_of_GRBs.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/fast-radio-followup-of-grbs" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

An early talk on the ALARRM_ rapid radio follow-up project, touching on the
science of GRB progenitors and possible LOFAR transient science.

.. _ALARRM: http://4pisky.org/tag/alarrm/


-----------



Talks on lucky imaging
----------------------

Lucky imaging: Life in the visible after HST
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*Southampton, March 2012*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2012-03_Intro-to-lucky-imaging_Soton/Lucky_Imaging.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/lucky-imaging-life-in-the-visible-after-hst" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

An introduction to lucky imaging, the subject of my PhD.

A user's guide to lucky imaging
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*RS meeting on lucky imaging and microlensing, Chicheley Hall, April 2013*

.. raw:: html

    <a href="https://github.com/timstaley/presentations/blob/master/2013-04_Users-guide-to-Lucky-Imaging_Chicheley/users_guide_to_lucky_imaging.pdf?raw=true">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-download-alt" aria-hidden="true"></span> PDF
    </button>
    </a>
    <a href="http://www.slideshare.net/TimStaley1/a-users-guide-to-lucky-imaging" target="_blank">
    <button type="button" class="btn btn-sm">
            <span class="glyphicon glyphicon-cloud" aria-hidden="true"></span> Slideshare
    </button>
    </a>

An invited talk given to an audience interested in using lucky imaging for
microlensing studies. I tried to give an overview of where the challenges lie
in getting good science data using lucky imaging techniques.