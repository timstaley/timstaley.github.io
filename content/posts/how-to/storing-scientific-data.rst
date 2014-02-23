#######################
Storing scientific data
#######################

:date: 2012-09-17
:tags: how to, serialization, science
:status: draft

-------------------------------------------------------
A brief summary of serialization methods for scientists
-------------------------------------------------------

TODO: Add python examples / library links.

The aim of this post is to give a quick overview of serialization,
or in plain english, storing your data. 
It's introductory material that any compsci graduate or IT professional 
might scoff at,
but it wasn't until I was knee deep in my PhD that I ever thought hard 
about this stuff, and by then I'd been doing it wrong for quite a while.
So, this is the five-minute introduction to serialization I wish I'd had at the 
start of my PhD. 

Suppose you are generating some reasonably complex research data. 
Maybe it's quite simply structured, or maybe it has byzantine layers and 
cross-references.
You have enough datapoints that you don’t want to be shuffling your data 
around by hand – it has to be machine readable somehow.

Usually, your experiment, analysis or simulation is computationally expensive 
and time consuming, so you won’t want to repeat it if you don’t have to. 
On the other hand, you will want to plot different combinations of parameters 
again and again as you explore the data, 
pretty up your plots, and so on. 
Also, you need a way to store and distribute that data for the sake
of reproducibility. How should you go about it?

The catch-all term to search for is `serialization`_.
Typical methods and their pros/cons include:

Tabulated CSV / Text representation
-----------------------------------
Outputting everything to a text file (typically in CSV format)
is very simple to do, and has the advantage of being compatible with just 
about any language.  
However, be warned: if trying to roll your own in Fortran / C++, 
and your data is anything but simple integers, it's easy to hit 
problems to do with escaping unusual characters, rounding issues, etc.
Then there’s the problem that this is a flat format, 
which is to say it cannot encode a hierarchy in the data. 
So, for example, if you have a bunch of datapoints recorded with instrument 
configuration A, and another bunch with instrument configuration B, 
then you either have to record separate tables for your instrument 
configurations and the resulting data, or you have a table many columns 
wide with the instrument parameters duplicated for every datapoint in a set. 
This quickly becomes a pain as your data grows, although it does have the 
advantage that you can wrangle it via a familiar spreadsheet program.
   
Binary formats
--------------
Using library routines – or (shudder) writing your own –
to store data in a binary format (e.g. FITS tables)
has less issues with escaping and rounding, is usually more space efficient,
and may even allow for hierarchical groupings, 
but it’s often not very user friendly. 
Unlike a CSV file you can’t just open the data up in a spreadsheet program; 
you must use exactly the right software to decode the information. 
It can also be a pain to code up the data-output routines in a flexible or 
reusable manner. 
What if you realise halfway through your experiments that you want to 
record additional parameters? 
Congratulations, you’ve just hit the problem of versioning, 
and your binary serialization just got a whole lot more complex.

Database management systems
---------------------------
DBMS don’t exactly fit into the category of serialization methods - 
they're more of a category of their own -    
but I’ll mention them for completeness. 
DBMS are what you use if you have a seriously large dataset, 
or you’re handling concurrent access requests, 
or any one of many situations where they’re invaluable. 
But for most research scientists, the overheads of setting one up, 
finding the relevant interface library for your language, 
and learning SQL, mean DBMS are not worth the overheads vs simpler techniques.
To some extent the the versioning / flexibility pitfalls of binary stores
also apply. 

Standardised text serialization formats, e.g JSON
-------------------------------------------------
XML and JSON are both standards for encoding data in a flexible, 
hierarchical manner. 
Both are text-based, so even if you lose the arcane code you used to output 
your data, you need nothing more than a text editor to go back and check 
your crucial values - or you can load up the data in Python and explore
it via the interpreter. 
XML has a fairly ugly syntax necessitated by a bunch of features you
almost certainly won’t need, so for any data which has a hierarchical 
structure, JSON is usually the method of choice - it's relatively simple
and has a well featured libary in any language worth coding in.
JSON's only downside is that it can be a little hard to edit manually, 
due to all the parentheses - so program configuration files sometimes use
something a bit more esoteric like YAML or the Python configparser language,
and it's worthwhile being aware these exist too.
   
Via the magic of pickle
-----------------------
(Python only)
While the methods above will serve most purposes, I couldn't avoid
mentioning pickle here. It's Python specific, so you can't use it
to shuffle data between programming languages, but it has some very 
neat tricks - you can pickle most things in python, including 
complex data structures and functions. 
So for example, you might define a bunch of Python classes to make working
with your data easier. 
Then, you want to save the data represented by a list of those classes.
At this point, you have two options: you can define a 'serialize' function
for the class which converts the data into a JSON friendly dictionary, or
you can simply 'pickle' the list of classes, often with no extra code.
Of course, the downside is that this is akin to a magic binary format - 
versioning issues aren't such a big deal because the saving / loading
is taken care of for us, but now you can't manually check your data
without loading up the objects in Python. So, a good trick, but not 
recommended for general usage.
  

.. _serialization: http://en.wikipedia.org/wiki/Serialization