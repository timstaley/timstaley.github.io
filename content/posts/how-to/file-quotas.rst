
########################################
Setting up disk quotas with Ubuntu 12.04
########################################
:date: 2013-07-24
:tags: how to, Ubuntu, sysadmin, disk quotas

There seems to be very little information on the web about setting up disk 
quotas, presumably because it's perceived as being trivial. 
However, it's nice to have this confirmed or refuted before you dive in, 
so here are my notes. 

First off:

.. code-block:: bash

   $ sudo apt-get install quota quotatool
   
Now edit */etc/fstab*; simply add a ``,usrquota,grpquota`` to the mount options 
as required like so::

   UUID=eafa3a88-2d0f-43c1-8992-1813ac3d530a /data1 ext4 defaults,user_xattr,usrquota,grpquota 0 2

Now, you have two options. 

The first is simply to reboot the machine. 
If all goes well, then the disk in question will mount with the new quota options,
and on starting the '``quota``' service will automatically build quotas, then start as normal -
your usual Ubuntu full-automation approach.
The only downsides to this are that you need to reboot, and unless you're paying close attention
you won't know exactly when the quota-building is done, as it happens in the background.
You *can* check to see if it's still running, using:

.. code-block:: bash

   $ ps -ef | grep quotacheck

The no-reboots option (or fallback, if the automated approach doesn't work) is to manually
shepherd your machine through the process. 
First, you'll need to remount the disk to activate the new mount options, e.g. 

.. code-block:: bash

   $ sudo umount /data1
   $ sudo mount -a

You can call ``mount`` again to check everything is correct. 
If the disk won't unmount cleanly, 
`determine what's blocking <http://stackoverflow.com/questions/7878707/umount-a-busy-device>`_, 
close it, and try again.

Next, (in case you rebooted but something went wrong, etc.) make sure that no 
quota-generation commands are running in the background, 
by stopping the service:

.. code-block:: bash

    $ sudo service quota stop

and doing a final check for any running services:

.. code-block:: bash

    $ ps -ef | grep quota

(You'll need to kill anything that looks like ``quotacheck`` or ``quotad``.)

You can now manually run:

.. code-block:: bash

   $ sudo quotacheck -avug #all, verbose, user and group quotas

This will create the files *aquota.group* and *aquota.user* 
in the root directory for all of your quota'd mount points.
This can take several hours on multi-terabyte RAID arrays, so you might want 
to run it from a `screen <http://en.wikipedia.org/wiki/GNU_Screen>`_.

Finally, just switch the quota service on:

.. code-block:: bash

   $ sudo service quota start

and give it a test run. My preferred flags are:

.. code-block:: bash

   $ quota -vs --show-mntpoint --hide-device

(you might want to alias that)
which results in something like::

  Disk quotas for user Bob (uid 1001): 
  Filesystem  space   quota   limit   grace   files   quota   limit 
    /data2    359G    0K      0K      1627k       0       0
    /data1    805G    0K      0K      68689       0       0




If you're already sharing the quota'd mounts over NFS, don't worry! 
The quota info is exported without any further configuration. 
Just run the quota command from the remote machine to see details immediately. 
(Although, nothing is certain in sysadmin. It worked for me, YMMV, etc.)

Of course, if you're using it for more than simply tracking usage, 
you'll need to set up quotas and so on. 
Google *edquota* and you should be alright at this point.
