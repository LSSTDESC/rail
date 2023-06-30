************
Overview
************

RAIL is a constellation of multiple packages developed publicly on GitHub and 
welcomes all interested developers, regardless of DESC membership or LSST data rights.

If you're interested in contributing, but don't know where to start, take a look 
at the list of good first issues from all RAIL repositories 
`here <https://github.com/orgs/LSSTDESC/projects/6/views/20>`_.
Or, create a new issue `here <https://github.com/LSSTDESC/rail/issues/new>`_ to 
suggest a change, and the team will route it to the appropriate repository.

In addition to GitHub, the RAIL team uses the LSSTC Slack workspace for organization.
Professional astronomers (including students!) based in the US, Chile, or a 
French IN2P3 institution are encouraged to 
`join the LSST-DESC <https://lsstdesc.org/pages/apply.html>`_ to gain access to 
the `\#desc-pz-rail <https://lsstc.slack.com/archives/CQGKM0WKD>`_ channel on 
the LSSTC Slack workspace.

Those without data rights who wish to gain access to the Slack channel should 
`create an Issue <https://github.com/LSSTDESC/RAIL/issues/new>`_ to request that 
the team leads initiate the process for adding a DESC External Collaborator.


Where to contribute: RAIL packages
==================================

RAIL functionality is split among several GitHub repositories to make it easier 
to manage ever-changing dependencies. 
Most contain the few stages sharing a particular challenging dependency, with 
the exception of three meta-repositories:

* ``rail`` is the portal for users who want to access all of RAIL's functionality across all the repositories. 

* ``rail_base`` is where the superclasses and underlying infrastructure used by all the standalone repositories are defined.

* ``rail_pipelines`` is a place for users to share the pipelines they build with RAIL so others can call them directly or adapt them to their needs.

Overall, you may find yourself contributing to one or more of these repositories and/or making a new one.

Similar to the installation process, depending on how you want to contribute to 
RAIL, you will be contributing to one or more of the RAIL packages.

In all cases, begin by following the developer installation instructions 
:ref:`Developer Installation` and follow the contribution workflow instructions below.


Contribution workflow
=====================

The ``rail`` and ``rail_<xxx>`` repositories use an issue-branch-review workflow, 
similar to the standard `GitHub Flow <https://docs.github.com/en/get-started/quickstart/github-flow>`_.

Issue
-----

When you identify something that should be done, `make an issue <https://github.com/LSSTDESC/rail/issues/new>`_
for it -- the admins can move it to the appropriate repository if necessary, but 
if you know the specific ``rail_<xxx>`` package that the issue applies to, please 
do make the issue in that repository.


Branch
------

See :ref:`Developer Installation` for installation instructions.

While developing in a branch, don't forget to pull from ``main`` regularly (at 
least daily) to make sure your work is compatible with other recent changes.

When you're ready to merge your branch into the ``main`` branch, create a pull request
("PR") in the rail repository you cloned from. GitHub has instructions 
`here <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_.

Several continuous integration checks will be performed for new pull requests. 
If any of these automatic processes find issues with the code, you should address 
them in the branch before sending for review. These include unit tests (does the 
code function correctly), pylint (code style), or coverage (how much code is 
exercised in unit tests).

Once you are satisfied with your PR, request that other team members review and 
approve it. You could send the request to someone whom you've worked with on the 
topic, or one of the core maintainers of rail.


Merge
-----

Once the changes in your PR have been approved, these are your next steps:

1. the author merges the change by selecting "Squash and merge" on the approved pull request
2. enter ``closes #[#]`` in the comment field to close the resolved issue
3. delete your branch using the button on the merged pull request.

Reviewing a PR
--------------

To review a pull request, it's a good idea to start by pulling the changes and 
running the unit tests locally. If the continuous integration tests have run 
successfully, there is good hope that the unit tests will run locally as well! 

Check the code for complete and accurate docstrings, sufficient comments, and 
ensure any instances of ``#pragma: no cover`` (excluding the code from unit test 
coverage accounting) are extremely well-justified.

Feel free to mark the PR with “Request changes” for necessary changes. e.g. 
writing an exception for an edge case that will break the code, updating names 
to adhere to the naming conventions, etc.

It is also considered good practice to make suggestions for optional improvements, 
such as adding a one-line comment before a clever block of code or including a 
demonstration of new functionality in the example notebooks.

Naming conventions
==================

We follow the `pep8 <https://peps.python.org/pep-0008/#descriptive-naming-styles>`_ 
recommendations for naming new modules and ``RailStage`` classes within them.

Modules
-------

Modules should use all lowercase, with underscores where it aids the readability
of the module name. If the module performs only one of p(z) or n(z) calculations,
it is convenient to include that in the module name.

e.g. 

*  ``simple_neurnet`` is a module name for algorithms that use simple neural networks from sklearn to compute p(z) or n(z)
*  ``random_pz`` is an algorithm that computes p(z)


Stages
------

RailStages are python classes and so should use CapWords convention. All rail 
stages using the same algorithm should use the same short, descriptive prefix, 
and the suffix is the type of stage.

e.g.

*  ``SimpleNNInformer`` is an informer using a simple neural network
*  ``SimpleNNEstimator`` is an estimator using a simple neural network

Possible suffixes include:

* Summarizer
* Informer
* Estimator
* Classifier
* Creator
* Degrader
* Evaluator


Contribution Types
==================

We anticipate a few types of contributions, and provide separate instructions 
for those workflows:

* :ref:`Fix an Issue` in the codebase
* :ref:`Adding a new Rail Stage` without new dependencies
* :ref:`Adding a new algorithm` (new engine or package)
* :ref:`Sharing a Rail Pipeline`
