##############################################
Automated incoming file processing with python
##############################################

:date: 2014-02-23
:tags: how to, python, rsync, automation

This weekend, I finally got around to spending a little time cleaning up
a single-file `script`_ I wrote to automatically process files as they are
transferred into a local directory, via rsync.

The fact that I was able to do this in a short script is largely thanks to
`pyinotify`_, which takes care of interfacing with the linux
`internals`_ which track file changes, so the hardest part was really done for
me - hurray for open source!

That said, I would have thought rsync transfers were a prime use-case for
this sort of tool, and yet I couldn't find any good examples on the web,
which is why I thought it might be worth writing up (and `pull-requesting`_).
Handling of rsync files is a little more complex than the standard examples,
because it creates temporary files for partial downloads, then renames them
once the download is complete. If you only want to catch new files
(my particular use case) then you need to track these temporary files as they
are created and renamed - but this is easily done with a few lines of python.

Anyway, for future reference: coding up custom file-tracking behaviour
with pyinotify is not too hard:

#. Profile your file transfer behaviour by running::

    python -m pyinotify /path/to/folder_to_watch

   Try manually transferring a single file, then pick out the sequence of
   events you want to track.

#. Create a class inheriting from ``pyinotify.ProcessEvent`` that will perform
   the required state-tracking and job-dispatching. Customising its behaviour
   is just a case of overriding certain class-methods.

#. Profit! That's it, basically. Now you just have to plug your custom class
   into one of the standard pyinotify usage examples.

More details can be found at the pyinotify `tutorial`_, in the pyinotify
`examples dir`_,
and (if you want to track rsync'ed files, or use asynchronous pool processing) by
reading through my `script`_.



.. _script: http://github.com/timstaley/autocrunch
.. _pyinotify: http://github.com/seb-m/pyinotify
.. _internals: http://en.wikipedia.org/wiki/Inotify
.. _pull-requesting: https://github.com/seb-m/pyinotify/pull/65
.. _tutorial: https://github.com/seb-m/pyinotify/wiki/Tutorial
.. _examples dir: https://github.com/seb-m/pyinotify/tree/master/python2/examples