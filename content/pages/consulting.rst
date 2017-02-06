##########
Consulting
##########
:slug: consulting

*In short:*

I'm available for hire as an independent software consultant, happy to work
on projects at all stages from "we've got an idea of something we'd like, but
no idea how to build it"
to "we have a five-year old website that talks to our database, and no-one
knows how it works anymore".


I primarily work as a back-end Python engineer, which means I write code that does
data processing, loads and extracts information from databases,
or makes data available over the web.
More broadly, I'm experienced in continuous cloud-deployment,
I enjoy diving into SQL, and I spent 4 years working in C++ for my PhD project.
I also have some experience in probabilistic modelling and data-visualisation.

Read on for a bit more detail, or jump to the end for a short list of
tools and frameworks.

Things I can do
---------------

First off, by (undergraduate) training I'm a mathematician. Day to day this
doesn't influence my work much, but the analytical background
occasionally comes in handy; e.g. when picking up the literature in a new area,
or verifying that an ad-hoc approximate formula implemented in someone else's
code actually calculates the right thing.

Since branching into software development, I've picked up a range of skills in
order to get things done, working variously as part of a distributed team of
dedicated software engineers, and as the software-focused researcher embedded in
a more conventional academic group. As a result I'm well versed in the 'bread
and butter' of modern software development and project management - automated
testing, version control, documentation, continuous deployment and release
management.

Perhaps more importantly, I've picked up the soft skills needed to discuss a
technical problem with domain specialists and put together a clean, maintainable
solution to their problem using the appropriate tools.

Previous briefs include:

- We have a custom data-reduction pipeline written in C++. It needs to
  run an order-of-magnitude faster, and we need the following new features to
  handle an entirely new data-model...
- We reduce our data via a manual, interactive process requiring significant
  domain expertise and specialized scientific software. We need a 'good enough'
  version of this process to be automated so we can respond to incoming data in
  timely fashion.
- We need a way to archive, retrieve and search through millions of custom
  data-packets, so that crucial scientific clues don't get lost in the noise.
  It needs to be a web-service too, so we can share it.
- We need a way to easily install and run our code on a 'cloud' server, test new
  versions, and make sure we can update it reliably or spin up a backup machine.
- We need a back-end web-service that receives data from a mobile app,
  queues it for processing with some heavyweight C++ code, and then inserts
  the results into a database.


Tools and frameworks
--------------------
I've built substantial, in-production projects using the following
(see the code_ page for open-source examples):

Python
^^^^^^
- Numpy / Scipy
- Django / Django-Rest-Framework
- Flask
- SQLAlchemy (w/ Postgres)
- LXML
- Pytest
- Sphinx documentation

Deployment
^^^^^^^^^^
- Ansible
- Vagrant
- Linux (Debian / Ubuntu, Centos)
- Apache / mod_wsgi
- uwsgi / nginx

C++
^^^
- Thread Building Blocks
- CMake
- GTest


General collaborative development skills
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
- Git (I know my way around the reflog and rebase private branches as a matter
  of course).
- Github (pull requests, continuous integration and documentation build hooks,
  etc)



Get in touch
------------
If you'd be interested in working together, or would like some specifics
on my previous work, please don't hesitate to email:

.. raw:: html

    <p>
    <ul class="fa-ul fa-lg">
      <li>
        <a href="mailto:Tim Staley <consulting(no-spam-please-at)timstaley.co.uk>">
            <i class="fa-li fa fa-envelope"></i>
                <span style="unicode-bidi:bidi-override; direction: rtl;">
                ku.oc.yelatsmit@gnitlusnoc
                </span>
        </a>
      </li>
    </ul>
    </p>
    </br>

P.S.
^^^^
I'm located in Oxford, UK. Remote work is no problem, but alternately if
you're in the area and would like to chat
in person, just drop me a quick line via email or twitter - always happy
to hear what other techies in the region are up to!



.. _code: /code