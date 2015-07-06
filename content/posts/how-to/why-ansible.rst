###############################################
Why is Ansible better than shell scripting?
###############################################
:slug: why-ansible
:date: 2015-07-01
:tags: ansible, scripting, provisioning, configuration management, deployment, devops, reproducibility

*(Edited 2015-07-06, added final note on downsides / Salt-stack.)*

Recently, I've been using Ansible_ to set up some new `VOEvent-node deployment scripts`_.
While I'm at it, I've also been converting a lot of messy provisioning
shell-scripts (see `old version`_, `new version`_ - work in progress).
Here are my notes on why Ansible is, IMO, much nicer than plain old shell-scripts,
and might be worth your time to learn.
Some of this stuff has been covered
`elsewhere <https://valdhaus.co/writings/ansible-vs-shell-scripts/>`_, and I
encourage you to go check out the code examples next.
However, my take is that in isolation none of the following features are really
compelling, and you actually need to use Ansible (or perhaps some other
configuration management tool) for a bit to see the full range of benefits and
realise what you gain. So, here's a fairly comprehensive feature-list in true
'what have the Romans ever done for us' style:

**Parallel execution across multiple machines.** This is what attracted me to
Ansible in the first place - using the ad-hoc_ mode to run shell commands
across many machines in parallel. Of course, there are other options
(e.g. pssh_), but it's a big part of what makes Ansible so powerful.

**A library of ready-made idempotent 'modules'** with a standarized
option format for dealing with common operations.
A lot of the idempotency_ (the concept that change commands should only
be applied when they need to be applied) you get with Ansible can be achieved
through careful shell scripting - always using ``mkdir -p``, carefully
cleaning and force-checkouting git repos, etc - and indeed with something like
``apt-get`` it's baked in. But, whenever there's a ready-made module,
Ansible takes care of those details for you, and also provides you with useful
additional options you might not have bothered with when writing shell scripts
from scratch, e.g. the ``apt`` module allows you to update the cached list of
packages prior to downloading, install recommended packages, etc.
Likewise the `git module`_
provides options to disable host key checking, use a custom SSH key file, perform a
recursive checkout, and so on. The module docs serve as handy
reminders of things you might need to switch on, and the option-specification
format provides an easy-to-read note of how each command should be
carried out.

**Automatic step-by-step reporting.** Ansible encourages you to name
each 'task' in your provisioning script, and then reports whether or not
that task succeeded with-or-without changes, or failed, and any error
messages. All colour coded. This is nice.

**Tagging.** You can tag_ your commands, making it easy to execute a subset
of a provisioning script without extracting that section or commenting
everything else out. Also nice.

**Convenient variable handling and logic-flow control.**
This is a big one. Ansible leverages the Jinja_
templating language, so you can use all the Python features that provides -
easy access to nested-dict variables, lists, string manipulation, and so on.
It also allows you to register_ the results of a command as a new variable.
This provides a dict containing entries telling you if that task succeeded,
whether it changed anything, what paths it created, etc. You can then
refer back to this variable in later commands, or even use it to perform
tasks conditionally_. Oh, and right out-of-the-box Ansible will provide you
with a bunch of machine-information variables like the operating-system family,
number of CPU cores, timezone, and so on. Again... you *could* do all this
in bash, but wouldn't you rather be using a well documented tool and coding in
Python?

**Readability.** I find the combination of YAML definition format and Jinja
templating quite readable, and certainly easier to skim than equivalent bash.
This is partly due to the enforced
whitespacing, and partly due to all the commands having a consistent options
format. Yes, you will need to learn a bit about YAML and Jinja to get the
most out of Ansible, but you can mostly pick it up from the examples laid
out in the docs. I haven't tried Puppet/Chef personally, so can't
directly compare,
but `others seem to think <http://probably.co.uk/puppet-vs-chef-vs-ansible.html>`_
Ansible is easier to get to grips with.
If you already know Ruby then perhaps Chef is a good option?


**Composability.**
Probably the biggest winner over shell-scripts in the long-term, although I get
the feeling that the community around Ansible is not quite there yet. Ansible
tries to solve the problem of code re-use by formalising a set of conventions
for building-blocks called roles_, and putting together a sort of 'github for
deployment-patterns' called `Ansible Galaxy`_. If things go well, this could
effectively become a PyPI or CPAN equivalent for devops. On the other hand, it
could devolve to a mess of untested, 'only works for my use-case' style packages
- success relies on an active community who are willing to test, review, extend
and maintain these packages. Time will tell if this is a realistic ask, but in
the meantime at least there's a standardized method for re-use in personal
collections.

**Downsides?**
Not many. Ansible only requires SSH, so you can use it with minimal
set-up overhead. It can be a bit slow to work through a playbook
when it's just checking system-state and not actually changing anything.
This can be improved somewhat by setting pipelining_ to True in your Ansible
config.
Others `report <http://ryandlane.com/blog/2014/08/04/moving-away-from-puppet-saltstack-or-ansible/>`_
that if you're working with a large number of machines SaltStack_ is considerably
faster in the check-and-do-nothing case.
It benefits from a similar Python/YAML markup, but isn't quite as well
documented for complete beginners, so that's perhaps a better option if you're
working in deployment full-time on large systems - though it does require a
client-side installation.


Comments
---------
Found this useful? Think I'm wrong, and want to tell me why?
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
.. _pipelining: http://docs.ansible.com/intro_configuration.html#pipelining
.. _SaltStack: http://saltstack.com/
.. _twitter: https://twitter.com/YossariansLife
