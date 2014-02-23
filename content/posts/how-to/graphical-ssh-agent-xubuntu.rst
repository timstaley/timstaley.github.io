
########################################
Graphical ssh-agent prompting in Xubuntu
########################################

:date: 2014-01-15
:tags: how to, Xubuntu, ssh

One of the fallbacks / features (depending on your preference) of using XFCE over the standard Ubuntu interface is that you don't get per-session ssh-agent handling (via a graphical interface) out-of-the-box, meaning you must manually fire up ssh-agent every time you login on your desktop. A minor annoyance, granted, but I remember it grating slightly after migrating from a pleasingly automated Ubuntu 10.04/Gnome setup. 

This is easily fixed, however. The basic idea can be found 
`here, <http://lekv.de/blog/2012/03/15/xfce-and-the-gnome-keyring-daemon-revised/>`_ after some googling
(and I think it was on one of the stack-exchange sites, but I've lost the link). 
However, what they don't mention is that **this squashes ssh-agent forwarding**. The SSH_AUTH_SOCK environment variable is always overwritten, so if you SSH to your desktop from elsewhere (your laptop, say), then attempt to tunnel forward to a third machine, you get a graphical prompt asking you to unlock your *desktop's* key, rather than silently forwarding the laptop's. Boo.

Fortunately, we only need to be marginally more sophisticated to make it watertight. 
Try adding this to your ``.bashrc``:

.. code:: 

    if [[ -z "${SSH_CONNECTION}" ]]; then
	    export $(gnome-keyring-daemon --start )
    fi

Tested on Xubuntu 12.04.
