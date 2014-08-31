############################################
EuroSciPy 2014
############################################
:slug: euroscipy2014
:date: 2014-08-31
:tags: conferences

**Some personal highlights, in five minutes or less.**


I spent the past couple of days attending the `scientific talks`_ at
EuroSciPy 2014.
Everything seemed to run smoothly, and hit about the right balance of
packing a lot in without being overwhelming, so kudos to the organisers.
I've summarised my personal highlights,
with the relevant links in case anything piques your interest.
(Even if no-one else reads it, at least I'll be able to find the links in six
months.)
I've tended towards the more generally applicable Python stuff,
as opposed to domain-specific talks.

I think all talks were recorded - if those become available I'll update the post.
This list is simply in chronological order.

Julia
-----
The `opening keynote <juliaslides_>`_ was about the Julia_ programming language.
While I'd heard a little about Julia
before, this was my first proper introduction, and I'm seriously impressed.
It seems that, even to those of us stuck in our Python mindset
for general work, Julia provides a credible, high-level alternative to
C / C++ / Fortran for writing high-performance inner-loop code, which is
quite the achievement in itself. And for those who want to properly jump ship,
you can take your Python ecosystem with you -
the interoperability is quite amazing, including that of
IPython Notebook / Julia-Jupyter.

Astropy
-------
While I'm reasonably familiar with astropy_, it was nice to get an update,
and a quick look at the units_ module, which I hadn't come across before -
I can see that being useful for a lot of complex physical simulation projects,
not just in astronomy.
Even more generally applicable, their asv_
(airspeed velocity) performance testing tool looks really nice, and is
available as a standalone package.


`Sloth-Hunting`_
-----------------
(AKA Neural Networks for Computer Vision.)

Re-using a feature network (expensively) trained for cat / dog recognition,
together with some fresh
classifier weights for a rapid adaptation to sloth hunting. Lots of fun.
(Ok, this was kind of specific, but who doesn't love sloths?)

Vispy
-----
Vispy_ is a Python package for high-quality interactive OpenGL plotting,
providing rich plots in two and three dimensions.
This was the first I've heard of Vispy,
and I'm not quite sure when I'll use it yet,
but I'll definitely keep it in mind.
As opposed to say, Blender, which is a largely polygonal
(and hence pre-rendered) 3D modelling tool,
Vispy makes extensive use of OpenGL trickery.
This allows more efficient rich and even interactive plotting -
for example you might graph thousands of points
as little spheres, without actually needing (say) a hundred polygons per sphere
- you just feed their positions and radii into the OpenGL engine.

Plotly
------
Plotly_ allows collaboration on plots *across different languages and tools*,
which is smart. Adds a user-friendly web-interface for tweaking and annotating.
They've also open-sourced a scientific plotting library for Javascript;
`plotly.js`_.
As the speaker might have put it: sweet!

Biggus
------
Biggus_ provides deferred access Numpy arrays,
allowing for (basic) lazy evaluation in Python.
Useful for massive data arrays that might not even fit in RAM.
I suspect I won't really understand how this works until I try using it,
so I'm not going to attempt to explain further, but certainly worth noting.


Dill / Pathos
-------------
It seems `Mike McKerns`_ has been on a one-man mission_ to fix heterogeneous cluster
computing in Python.
Interesting stuff, and definitely bookmarked for future trials.

DyND
-----
Finally, DyND_ provides an N-dimensional array handling library for C++, with
Python wrappers from the get-go!
Very excited about this, since I think it really fills a gap
in the Python/C++ interface space.
I've been thinking of trying `Boost.NumPy`_ for this sort of problem,
but using something that's a first-class
C++ library from the start sounds like a better way of going about it.


EuroSciPy is back to Cambridge in 2015 - see you there next year!

.. _scientific talks: https://www.euroscipy.org/2014/schedule/euroscipy-2014-general-sessions/

.. _Julia: http://www.julialang.org
.. _juliaslides: https://github.com/stevengj/Julia-EuroSciPy14

.. _astropy: http://www.astropy.org/
.. _units: http://docs.astropy.org/en/latest/units/index.html
.. _asv: http://spacetelescope.github.io/asv/index.html

.. _Sloth-hunting: https://www.euroscipy.org/2014/schedule/presentation/2/

.. _Vispy: http://vispy.org/

.. _Plotly: https://plot.ly/
.. _plotly.js: https://plot.ly/javascript-graphing-library/

.. _Biggus: https://github.com/SciTools/biggus

.. _Mike McKerns: https://www.euroscipy.org/2014/speaker/profile/62/
.. _mission: https://www.euroscipy.org/2014/schedule/presentation/3/

.. _DyND: https://github.com/ContinuumIO/libdynd
.. _Boost.NumPy: https://github.com/ndarray/Boost.NumPy