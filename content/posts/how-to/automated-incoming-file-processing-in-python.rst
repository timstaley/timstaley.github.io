##############################################
Automated incoming file processing with python
##############################################

:date: 2013-11-01
:tags: python, file monitoring, automation

:status: draft

#. Profile the file transfer using ipynotify module mode to watch the dir.
#. Note the transfer events. Set up a watch handler to deal with these 
   appropriately.
#. Hook up the watch handler with a processor function. 
   These can only take one argument - the file path - so you will need to define
   a wrapper function / partially bound version, if you have multiple arguments
   to deal with. 
   (See also: 
   `lambda vs partial in python. <http://stackoverflow.com/a/3252364/725650>`_)
#. Run your ipynotify / processing code in a terminal, and check that 
   everything is working OK.
#. [Optional] Multithreading! 
   It's trivial to enhance this simple code with a little multiprocessing magic. 
   Just use a Pool.
#. Profit! You may now leave your script running, eating up incoming files as 
   fast as your threads can handle them. Of course, unless this is rare 
   occurrence, you'll probably want to leave this running even when you don't 
   have a terminal open. Which leads us to...
#. Running a python script as a background process. The simplest way to do 
   this is to use a tool such as GNU screen, or possibly tmux. 
   For most purposes this will work just fine. The exception is if your script 
   does anything to do with parsing terminal output, 
   (perhaps using pexpect, for example). 
   This may still work for basic problems, but sooner or later you may find 
   you hit weird, unexplained crashes/bugs. (I did. It sucked). 
   As far as I can tell, this is because screen changes the way the terminal 
   output is handled slightly (http://unix.stackexchange.com/a/76211). 
   But it could be some obscure X-windows thing. 
   Anyway, GNU screen has to be manually restarted when the machine is rebooted. 
   We can do better. So we finally come to...
#. Running a python script as a service. This is easy to do using upstart. 
   Simply drop a script into /etc/init, with contents looking something like 
   this:

   Now, you may need to make some small alterations to get this working. 
   First and foremost, if you run your python script in a virtualenv, 
   you need to automate the activation. 
   You can do this 2 ways - call a shell script that activates the virtualenv, 
   then calls the python script, or just add a couple of lines to the python script:
   activate_this = '/home/ts3e11/.virtualenvs/autocrunch/bin/activate_this.py'
   execfile(activate_this, dict(__file__=activate_this))
   (This is generally my preferred method, but it really depends where you 
   want your configuration changes to live - in the python script, or a wrapper 
   bash script).

   Another trick that may be helpful is to assume the user identity. 
   There are two reasons to do this: A. to give certain file authorship. 
   This can be achieved in Ubuntu 12.04> via setuid.
   B. As 'A', but also to set up paths, env variables etc by sourcing the user's
   .bashrc. In which case, you want::
      
      su myuser -c "somecommand arg1 arg2"
      
   Finally (and this is a trivial one, but something that might not occur when 
   using an unfamilar toolset), you should make sure that the outputs are logged
   to file::
      
      su myuser -c "somecommand arg1 arg2 >/tmp/somecommand_log.txt 2>&1"
      
   This allows for debugging when the thing won't start - you won't get any 
   output to the terminal from a script being run as a service.
   
   So, to test, simply::
      
      sudo start mypyservice
      tail -f /tmp/somecommand_log.txt
   
Now start transferring some files and (hopefully) watch your script start crunching. Good luck!
