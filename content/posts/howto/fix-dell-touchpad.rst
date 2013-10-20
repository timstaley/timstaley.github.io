
#######################################
Fix your Dell laptop touchpad in Ubuntu
#######################################

:date: 2013-02-15

Just testing a shiny new Dell Precision M4700, which is great... 
except the trackpad isn't recognized in Xubuntu 12.04, 
resulting in no multi-touch - it's amazing how clunky resorting to scroll bars 
seems now. 
Anyway, it turns out Dell are not thoroughly supporting the 'Alps' trackpads 
used on their latest models, which is a shame, as it results in reduced 
functionality out of the box for a raft of their laptops. 
(`See bug report <https://bugs.launchpad.net/ubuntu/+source/linux/+bug/606238/>`_.)

Fortunately, there is a fix (tested on Xubuntu 12.04): 


First, download 
`psmouse-alps-1.3 <http://www.dahetral.com/public-download/alps-psmouse-dlkm-for-3-2-and-3-5/view>`_. 
Then (using sudo / root):

- Extract the folder *psmouse-alps-1.3* to */usr/src*
- cd to */usr/src*
- ``dkms add psmouse-alps-1.3``
- ``dkms autoinstall``
- ``rmmod psmouse && modprobe psmouse``

That's it! Working multitouch! :-)