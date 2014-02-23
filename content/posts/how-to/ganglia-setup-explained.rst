
#######################
Ganglia setup explained
#######################

:date: 2013-12-21
:tags: how to, Ubuntu, Ganglia, sysadmin, monitoring

**Or, everything you wanted to know about setting up Ganglia, but couldn't grok 
from the official documentation - part 2.**

In this post I'll cover:

- What purposes the different `Ganglia`_ utilities serve, and how they fit 
  together.
- How to set up a minimal configuration, from apt-get install through to 
  configuring Apache to serve the web interface.
  
(See `part 1 <{filename}why-ganglia.rst>`_ 
for a general explanation of what Ganglia is, 
and why you might want to use it.)

Although Ganglia will - if you're lucky - work out of the box, 
I found it pretty difficult to get a good overview of how 
the different utilities fit together, and likewise how the various 
config file sections interact (the latter is much easier to follow when you
have a good understanding of the former). 
After about a day of trawling over the wiki and experimenting with various
setups, I felt I had a much better idea of what was going on and how to tweak 
it. I should also mention that the first time I tried Ganglia,
I had zero experience with configuring a web-server, which (understandably)
isn't covered in the quickstart guide. 
So, I thought I'd put together all the information that would have helped
a year ago when I first got Ganglia up and running.  

Let's start with what the different `daemons`_ actually *do*.
There is a brief explanation on the ganglia wiki at 
http://sourceforge.net/apps/trac/ganglia/wiki/ganglia_documents, but it's a 
bit dense and jargon heavy - 
I've tried to expand in a more 'newbie friendly' manner below:

gmond
   Responsible for actually collecting
   all the metric information we're interested in, and forwarding it on
   to somewhere else.  Keeps state only in RAM, 
   - i.e. does not save anything to disk, only knows the most recent stats. 
   This is the only service that needs to be run on every node, and has 
   very low CPU / RAM overheads (I never see it go about 0% CPU on `htop`_!).
   
   Communicates via two methods: 
   
   (for an explanation of TCP vs UDP, see e.g. 
   http://www.bleepingcomputer.com/tutorials/tcp-and-udp-ports-explained/,
   http://stackoverflow.com/questions/5970383/difference-between-tcp-and-udp )
   
   - gmond to gmond via UDP. 
      gmond daemons can be configured to share their state
      in a peer to peer fashion, so that when queried, one node can report 
      both its own most recent metrics, and those of other nodes. 
      This provides redundancy - if one node goes down
      the rest still pass their information around between them. 
   - gmond to <X> via TCP. 
      The gmond daemons can be polled for an update via
      a TCP connection (from any program, including e.g. netcat or telnet - this
      can be useful for checking everything is up and running).
      
gstat
   A command line tool which connects to gmond (via TCP) and provides a 
   quick summary of the current stats from all the nodes for which that gmond 
   daemon has data.
      
      
gmetad
   Responsible for polling gmond daemons via TCP on a
   regular basis. Records the information to disk in the form of `RRD`_ files.
   Depending on how your gmond daemons are configured (whether or not they are
   set to relay their status between nodes), gmetad can either be pointed 
   at one gmond daemon, and pull the entire cluster status from that one node,
   or it can pull the status from each gmond node individually. Or 
   you can configure it to do both, for redundancy.
   
   
ganglia-web
   Not a strictly essential part of the solution, but you'll probably 
   want a graphical way to view your collected statistics. 
   This is a web-page frontend built on PHP scripts, which queries the RRD 
   files saved by gmetad. 
   As far as I can tell it's stateless, i.e. the graphs are generated on the 
   fly - all the persistent data is in the RRDs.
   For a live and publicly accessible example, see 
   http://ganglia.wikimedia.org/ (which is currently tracking around 900 nodes).
   

**So, on to the configuration guide. This is tested on Ubuntu 12.04, 
but the ganglia-specific config tips should be broadly applicable.**

First off, we need to set up gmond on each machine we want to monitor, 
(or 'node'):

Start with 

.. code-block:: bash

   $ sudo apt-get install ganglia-monitor
   

Next we'll configure gmond via the file at ``/etc/ganglia/gmond.conf``. 
Assuming you just want the standard metrics, you only need to worry about the 
first few stanzas that control how the stats are distributed. 
By default, the ones we're interested in look like the following:

.. code-block:: squidconf

   globals {                    
     daemonize = yes              
     setuid = yes             
     user = ganglia              
     debug_level = 0               
     max_udp_msg_len = 1472        
     mute = no             
     deaf = no             
     host_dmax = 0 /*secs */ 
     cleanup_threshold = 300 /*secs */ 
     gexec = no             
     send_metadata_interval = 0     
   } 
   
   /* Feel free to specify as many udp_send_channels as you like.  Gmond 
      used to only support having a single channel */ 
   udp_send_channel { 
     mcast_join = 239.2.11.71 
     port = 8649 
     ttl = 1 
   } 
   
   /* You can specify as many udp_recv_channels as you like as well. */ 
   udp_recv_channel { 
     mcast_join = 239.2.11.71 
     port = 8649 
     bind = 239.2.11.71 
   } 
   
   /* You can specify as many tcp_accept_channels as you like to share 
      an xml description of the state of the cluster */ 
   tcp_accept_channel { 
     port = 8649 
   } 

Note the ``udp_send_channel`` and ``udp_recv_channel`` sections, 
which are configured to use 
`multicast <http://en.wikipedia.org/wiki/Multicast>`_ - essentially broadcasting
their status to all other nodes configured in the same manner, to provide
automatic discovery of new nodes. 

This default configuration works great if you're running on your
own private cluster of machines, on a local network with the UDP ports 
blocked between you and the outside world. In that case, you don't even
need to touch ``gmond.conf``.
However, there are situations where you might not want to do things this way. 
For example, `multicast may be disabled on
cloud server instances <http://www.openscg.com/2013/06/ganglia-in-the-cloud/>`_.
Another example is if you're on a large university campus network, when 
there's a significant chance you'll accidentally get cross-talk with someone
else's ganglia cluster, or you may find that e.g. multicast works on a single 
server rack but is blocked between different server farms. 
Whatever.
We can set up a much more finely controlled 
(although admittedly less redundant / robust) *unicast* configuration, 
very easily. Assuming you're happy with a single 'master' gmond node collecting
data from all the others, it might look something like this:   

.. code-block:: squidconf

   globals {                    
     daemonize = yes              
     setuid = yes             
     user = ganglia              
     debug_level = 0               
     max_udp_msg_len = 1472        
     mute = no             
     deaf = no             
     host_dmax = 3600 /*secs */ 
     cleanup_threshold = 300 /*secs */ 
     gexec = no             
     send_metadata_interval = 30     
   } 

   
   /* Feel free to specify as many udp_send_channels as you like.  Gmond 
      used to only support having a single channel */ 
   udp_send_channel { 
     host = master.node.address
     port = 8649
   }
   
   udp_recv_channel { 
    port = 8649
   }  
   
   tcp_accept_channel { 
     port = 8649
   } 

Note that I've also tweaked the ``host_dmax`` and  ``send_metadata_interval``
settings from their defaults. 

**host_dmax** simply controls how long a node remains listed once
it stops sending out new data. 
How you set this depends if you regularly add
temporary machines to the cluster then remove them later 
(leave it to something like an hour or they'll clutter up your stats), or 
if you have a stable cluster and you want to be reminded which machines are
currently down (leave it set to the default of 0).

**send_metadata_interval** controls how frequently the stats 
(and *I'm here / I'm alive* status) are pushed out 
blindly over UDP to any recipients listed under ``udp_send_channel`` stanzas.
If this is left to the default of 0, then the node will only broadcast 
its presence when the daemon is started, relying on other nodes to 
request updates ('poll') it via the port listed under the 
``udp_recv_channel`` stanza. 
You can in fact configure the node
to just broadcast blindly at regular intervals 
(set ``send_metadata_interval`` to a nonzero value, 
delete the udp_recv_channel stanza) 
or you can rely solely on polling, but it seems sensible to have both 
switched on. 
See the 
`relevant wiki page <http://sourceforge.net/apps/trac/ganglia/wiki/Gmond%203.1.x%20General%20Configuration>`_
for more details. 
  
With that done, do a 

.. code-block:: bash

   $ sudo service ganglia-monitor restart
   
on each node, then log onto the master node and try

.. code-block:: bash

   $ gstat -a
   
Which should hopefully report the current CPU / load stats of all the nodes 
in the ganglia cluster.

Next we need to set up gmetad, to record the stats to disk.
First of all, let's check that we don't have any connection issues,
by polling the master gmond daemon manually.
On the machine you'll be using to serve up the web-frontend
simply run:

.. code-block:: bash

   $ netcat master.node.address 8649
   
(Assuming your gmond is configured with the default ``tcp_accept_channel``
port, as above.)
If you get a bunch of XML stats, congratulations, you're good to go. 
Next:

.. code-block:: bash

   $ sudo apt-get install gmetad
   
then do a single line edit on ``/etc/ganglia/gmetad.conf`` to tell it 
which gmond node to poll for information, e.g. something like::
 
   data_source "MyCluster" 10 master.node.address
   
where 10 is simply the polling interval. If you have your gmond daemons 
set up to share data around in full-on redundancy fashion, 
you can add multiple addresses on this line - 
if gmetad can't access the first, it will try the others one-by-one until it 
gets a response. 
(More info 
`here <http://sourceforge.net/apps/trac/ganglia/wiki/Ganglia%203.1.x%20Installation%20and%20Configuration#gmetad_configuration>`_.)

Finally, we need to install the web-based frontend. 
There is a Ubuntu package for this, but it's a little dated - I much prefer the
look and feel of the latest release. So let's grab it from GitHub:
 
.. code-block:: bash

   $ git clone git@github.com:ganglia/ganglia-web.git 
   $ cd ganglia-web
   $ sudo make install
   
Which will dump some config files to ``/var/lib/ganglia-web``, 
and all the php into ``/usr/share/ganglia-webfrontend``.

Next we install Apache and the relevant supporting libraries:
  
.. code-block:: bash

   $ sudo apt-get install apache2 libapache2-mod-php5 php5-gd rrdtool
   
Finally, we configure apache to serve the PHP pages in 
``/usr/share/ganglia-webfrontend``. There's an example config in the
ganglia-web repository, called ``apache.conf``. 
Assuming you're not serving anything else from apache, the easy way to do this 
is to add a ``<VirtualHost *:80>`` and ``</VirtualHost>`` at the beginning and 
end of that file, then

.. code-block:: bash

   $ sudo cp apache.conf /etc/apache2/sites-available/ganglia
   $ sudo a2dissite default
   $ sudo a2ensite ganglia
   $ sudo service apache2 reload
   
(If you're already serving other sites, you can just paste the contents
of apache.conf into whatever site config you're currently running - but then
you probably don't need me to tell you that. 
NB though, you might need to enable:: 

  DirectoryIndex index.html index.php
   
if you've specified it to only allow::
 
  DirectoryIndex index.html
   
previously. That caught me out.)

Hopefully, you should now be able to browse to 
``http://your.web.server/ganglia`` and 
see a bunch of performance stats. 

HTH. 
 
   

.. _daemons: http://en.wikipedia.org/wiki/Daemon_(computing)

.. _Ganglia: http://ganglia.sourceforge.net/

.. _htop: http://htop.sourceforge.net/

.. _RRD: http://en.wikipedia.org/wiki/Round-Robin_Database




