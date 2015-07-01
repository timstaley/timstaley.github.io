###############################################
Why is Ansible better than shell scripting?
###############################################
:slug: why-ansible
:date: 2015-07-01
:tags: ansible, scripting, provisioning, configuration management, deployment, devops, reproducibility


Recently, I've been using Ansible to set up some new `VOEvent-node deployment scripts`_.
While I'm at it, I've also been converting a lot of messy provisioning
shell-scripts (see `old version`_, `new version`_ - work in progress).
Here are my notes on why Ansible_ is, IMO, much nicer than plain old shell-scripts,
and might be worth your time to learn.
This sort of stuff has been covered
`elsewhere <https://valdhaus.co/writings/ansible-vs-shell-scripts/>`_, and I
encourage you to go check out the code examples next, but I wanted to get my
thoughts down in a few short(ish) bullet points.
Anyway, here's why it's handy:

**Parallel execution across multiple machines.** This is what attracted me to
Ansible in the first place - using the ad-hoc_ mode to run shell commands
across many machines in parallel. Of course, there are other options
(e.g. pssh_), but it's a big part of what makes Ansible so powerful.

**A decent library of ready-made 'modules'** with useful options
for dealing with common operations. For example, take ``apt-get``. This
is one utility where idempotency_ (the concept that change commands should only
be applied when they need to be applied) is already baked in to the command
itself, so Ansible doesn't really gain you much there - but it provides you with
a handy option to update the cached list of packages prior to downloading,
another option to install recommended packages, etc. Likewise the `git module`_
provides options to disable host key checking, use a custom SSH key file, perform a
recursive checkout, and so on. Of course, you can do these yourself (Ansible
just runs the commands under the hood after all) but the docs serve as handy
reminders of things you might need to switch on, and the option-specification
format provides an easy-to-read note of how each command should be
carried out. Now, you *could* build up a library of e.g. bash functions
that provide similar wrapping and defaults, but then
A. you'd be writing functions in bash,
B. you'd have to start from scratch, and
C. anyone else touching your scripts
would have to learn your one-off custom DSL_.

**Automatic step-by-step reporting.** Ansible encourages you to name
each 'task' in your provisioning script, and then reports whether or not
that task succeeded with-or-without changes, or failed, and any error
messages. All colour coded. This is nice.

**Tagging.** You can tag_ your commands, making it easy to execute a subset
of a provisioning script without extracting that section or commenting
everything else out. Also nice.

**Convenient variable handling and logic-flow control.**
This is a big one. Ansible leverages the Jinja_
templating language, so you can use all the features that provides -
easy access to nested-dict variables, lists, string filters, and so on.
It also allows you to register_ the results of a command as a new variable.
This provides a dict containing entries telling you if that task succeeded,
whether it changed anything, what paths it created, etc. You can then
refer back to this variable in later commands, or even use it to perform
tasks conditionally_. Oh, and right out-of-the-box Ansible will provide you
with a bunch of machine-information variables like the operating-system family,
number of CPU cores, timezone, and so on. Again... you *could* do all this
in bash, but you'd have to spend the time figuring out obscure bash tricks,
and probably no mere mortal could make sense of your scripts afterwards.

**Readability.** I find the combination of YAML definition format and Jinja
templating quite readable - much more so than equivalent bash.
This is partly due to the enforced
whitespacing, and partly due to all the commands having a consistent options
format. Yes, you will need to learn a bit about YAML and Jinja to get the
most out of Ansible, but you can mostly pick it up from the examples laid
out in the docs. I haven't tried Puppet/Chef personally, so can't
directly compare,
but `others seem to think <http://probably.co.uk/puppet-vs-chef-vs-ansible.html>`_
Ansible is easier to get to grips with.
If you know Ruby then perhaps Chef is a good option, but then again,
maybe a full scripting language encourages overly-complex approaches?


**Composability.**
Probably the biggest winner in the long-term, although I get the feeling
that the community around Ansible is not quite there yet. Ansible tries to solve
the problem of code re-use by formalising a set of conventions for building-blocks
called roles_, and putting together a sort of 'github for deployment-patterns'
called `Ansible Galaxy`_. If things go well, this could effectively become
a PyPI or CPAN equivalent for devops. On the other hand, it could devolve
to a mess of untested, 'only works for my use-case' style packages - success
relies on an active community who are willing to test, extend and maintain
these packages. Time will tell if this is a realistic ask, but in the meantime
at least there's a standardized method for re-use in personal
collections.

Comments
---------
Found this useful? Think I'm a misguided fool, and want to tell me why?
Let me know on twitter_.

.. _VOEvent-node deployment scripts: https://github.com/timstaley/voevent-node-deploy/
.. _old version: https://github.com/timstaley/SAL-build-scripts
.. _new version: https://github.com/timstaley/ansible-casa-libs
.. _Ansible: http://docs.ansible.com/
.. _Jinja: http://jinja.pocoo.org/docs/dev/
.. _ad-hoc: http://docs.ansible.com/intro_adhoc.html
.. _pssh: http://linux.die.net/man/1/pssh
.. _idempotency: http://docs.ansible.com/glossary.html#idempotency
.. _git module: http://docs.ansible.com/git_module.html
.. _DSL: https://en.wikipedia.org/wiki/Domain-specific_language
.. _tag: http://docs.ansible.com/playbooks_tags.html
.. _register: https://docs.ansible.com/playbooks_conditionals.html#register-variables
.. _conditionally: https://docs.ansible.com/playbooks_conditionals.html#conditionals
.. _roles: https://docs.ansible.com/playbooks_roles.html#roles
.. _Ansible Galaxy: https://galaxy.ansible.com/
.. _twitter: https://twitter.com/YossariansLife