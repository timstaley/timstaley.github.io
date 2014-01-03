
##############################################
Cluster monitoring via multiple htop instances
##############################################

:date: 2013-02-17
:tags: sysadmin, monitoring

For cluster-usage monitoring I've mostly been using Ganglia, as covered 
`here <{filename}why-ganglia.rst>`_.
But while it provides a great overview, sometimes you need to drill down and 
quickly see who's running what, on which node. 

For this, `htop`_ is a great tool with minimal overheads - console friendly 
interface, tiny footprint etc. 

I've put together a little script that allows the user to fire up multiple 
instances of htop, by opening multiple terminals with a 'ssh-and-run' combo 
that works well for me, so I thought I'd post it:

.. code:: bash
   
   #!/bin/bash
   ALL_HOSTS=(node1 node2 node3)
   
   if [ $# == 0 ]; then
       TARGETS=("${ALL_HOSTS[@]}")
   else
       echo '$0:' $0
       TARGETS=("$@")
   fi
   
   for HOST in "${TARGETS[@]}"; do
       gnome-terminal -t $HOST -e "ssh $HOST -t htop" &
   done


Run with no arguments, this will open up 3 child terminals and connect to the 
nodes listed as ``ALL_HOSTS``. 
Alternatively the user may supply a list of ssh targets as arguments. 
The tricky bit is the population and expansion of bash variable arrays - 
see http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_10_02.html 
for details.


.. _htop: http://htop.sourceforge.net/