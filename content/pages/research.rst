########
Research
########
:slug: research

======
Recent
======
I'm currently working on two projects:

**Auto-AMI** is a programme to undertake automated systematic follow-up 
observations of gamma-ray burst sources (GRBs). We're collaborating closely with 
the team at the Arcminute Microkelvin Imager, Cambridge, to create a fully
robotic system, from monitoring alert messages from the Swift satellite 
right through to slewing the telescope. As a result we're obtaining radio data
at very early times in the GRB afterglow evolution, and we'll shortly be 
submitting a paper to MNRAS. If you're interested in the software used to
automate the system, you should take a look at Comet and pysovo. 
If you're still interested, contact me.
 
Data obtained with AMI is also proving a conveniently manageable dataset for 
testing and refinement of **the Trap**, a software project I'm 
working on in close collaboration with developers at 
`UvA <http://www.astro.uva.nl/>`_.
Trap is a transients detection pipeline 
written primarily for use with data from 
LOFAR - a low frequency radio array. LOFAR will observe at ~10s to 100s 
of megahertz rather than the usual gigahertz range, 
giving us a new window on the radio sky.
The pipeline 'stack' employs
Python for data analysis, a MonetDB
backend, and Django for driving a 
browser-based science-user interface. 
While LOFAR presents a particular challenge due to the sheer volume
of data produced, the algorithms being developed are applicable to a range 
of transient astronomy projects. 

More details on the transients survey can
be found here:

- `LOFAR-TKP science case <http://www.lofar.org/astronomy/transients-ksp/scientific-rationale/scientific-rationale>`_
- `LOFAR-TKP technical information <http://www.lofar.org/astronomy/transients-ksp/technical-description/technical-description>`_


====  
PhD
====

**(2007 - 2011)**

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

If you're interested in the details you can download my thesis. Two versions of the PDF are available:  
`online <files/Staley_thesis_online_version.pdf>` and 
`print <files/Staley_thesis_print_version.pdf>` 
format.
