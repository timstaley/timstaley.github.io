
########################################
Setting up disk quotas with Ubuntu 12.04
########################################
:date: 2013-07-24
:tags: Ubuntu, sysadmin

There seems to be very little information on the web about setting up disk 
quotas, presumably because it's perceived as being trivial. 
However, it's nice to have this confirmed or refuted before you dive in, 
so here are my notes. 
All terminal commands should be performed with sudo rights. 

First off:

.. code-block:: bash

   $ apt-get install quota quotatool
   
Now edit */etc/fstab*; simply add a ``,usrquota,grpquota`` to the mount options 
as required like so::

   UUID=eafa3a88-2d0f-43c1-8992-1813ac3d530a /data1 ext4 defaults,user_xattr,usrquota,grpquota 0 2


Reboot.

Now, at this point your machine *may* reboot, build the quota files all by 
itself, and bring up the login all ready to go. 
Which is somewhat confusing, as the old-school guides dive into detail about 
how you do that manually. Or, confusingly, it may not. 
In which case 

**DON'T PANIC!**

Simply check for 2 things:

- The presence (or lack) of the files *aquota.group* and *aquota.user* 
  in the root directory of your quota'd mount points.
- Whether the quota service is running (try ``service quota status``).

If the files are missing, you need to manually force a quotacheck:

.. code-block:: bash

   $ service quota stop #Just to be certain
   $ quotacheck -avug #all, verbose, user and group quotas

This can take several hours on multi-terabyte RAID arrays, so you might want 
to run it from a `screen <http://en.wikipedia.org/wiki/GNU_Screen>`_.

Now just switch the service back on:

.. code-block:: bash

   $ service quota start

and give it a test run. My preferred flags are:

.. code-block:: bash

   $ quota -vs --show-mntpoint --hide-device

- you might want to alias that.

If you're already sharing the quota'd mounts over NFS, don't worry! 
The quota info is exported without any further configuration. 
Just run the quota command from the remote machine to see details immediately. 
(Although, nothing is certain in sysadmin. It worked for me, YMMV, etc.)

Of course, if you're using it for more than simply tracking usage, 
you'll need to set up quotas and so on. 
Google *edquota* and you should be alright at this point.