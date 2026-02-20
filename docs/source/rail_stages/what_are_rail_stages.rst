.. _rail-stages:

*********************
What Are RAIL Stages?
*********************

.. flowchart: stages to other stages

A RAIL stage is a single algorithm that can be run in a reproducible way. Each
stage has a specific goal, but can be configured through the use of parameters.
They are the basic building blocks of a larger pipeline and can be parallelized
across processors or computing nodes.

===============
Types of Stages
===============

There are three main types of stages in RAIL:

#. :ref:`Creation <creation>`: create sample photometric data
#. :ref:`Estimation <estimation>`: estimate photometric redshift from any input data
#. :ref:`Evaluation <evaluation>`: evaluate the performance of estimations against known true values
#. :ref:`Tools <tools>`: "pseudo-stage" providing utilities and tools for running stages

These stages generate data products that can be used independently, or as input
for other stages.

.. image:: /images/stages_detailed.png

========
Examples
========

Here we link the RAIL stages as listed above, with how they can be used to answer
specific scientific questions.

-----------------------------
Comparing Redshift Algorithms
-----------------------------

As one example, you may wish to examine which method of calculating photometric
redshifts is most appropriate for your dataset and final use case.

To do this with RAIL, you would:

#. Gather the data (either from an external source, or by generating it with RAIL)
#. Use several different *estimation* algorithms (stages available under the
   ``rail.estimation.algos`` namespace), to estimate photometric redshift values for the
   galaxies.
#. *Evaluate* the photometric redshift values, either by your own methods, or by using
   the *evaluators* and available *metrics* from the ``rail.evaluation`` namepace.

For a worked example of a case like this, see the `Goldenspike notebook
<https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/pipeline_examples/rendered/goldenspike_examples/goldenspike.html>`_.

-------------------------------------
Comparing Data Degradation Algorithms
-------------------------------------

As another example, you may wish to find what kind of data is best estimated by
a given redshift estimation algorithm. 

To do this with RAIL, you would:

#. Select an estimation algorithm and the evaluator stage that assesses its
   performance.
#. Use several different *creator* and *degrader* algorithms to determine which
   data creation and noise / bias algorithms generate datasets *best* estimated
   by the selected estimation algorithm.

For a worked example of a case like this, see `Exploring the Effects of Degraders <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/interactive_examples/rendered/creation_examples/Exploring_the_Effects_of_Degraders.html>`_ 
which explores how differently degraded training data sets affect how well the estimation algorithm works. 

=======================
Methods of Running RAIL
=======================

----------------
Interactive Mode
----------------

RAIL stages can be run interactively, such as in a Jupyter notebook. This is done via
specific function calls.

To learn about the available functions, visit the :ref:`Interactive
API<page-interactive-api>`.

To see examples of using stages interactively, visit the :ref:`interactive mode
notebooks`.

-------------
Pipeline Mode
-------------

:py:class:`rail.core.RailStage` is the main class.  It serves as the base class for all
the classes that implement parts of an analysis, and sets of ``RailStage`` can be
combined into a :py:class:`rail.core.RailPipeline` to perform a complete analysis.

In short, any ``RailStage`` does a single operation in a reproducible way. It can
be thought of as a way to wrap a single function so as to make it both
configurable and reproducible.

This presents a few constraints and limitations: the ``RailStage`` needs to save the
configuration of any parameters it uses, and it needs to get input from as well as write
output to specified locations. While the ``RailStage`` class provides mechanism to do
all of these things, sub-classes must implement the actual computational work of the
stage.

Below we give the API documentation for a few key elements of a ``RailStage``.

^^^^^^^^^^^^^^^^
RailStage basics
^^^^^^^^^^^^^^^^

.. autoclass:: rail.core.RailStage
    :noindex:

^^^^^^^^^^^^^^^^^^^^
Running a rail stage
^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.RailStage.run
    :noindex:

..
Note that subclasses of ``RailStage`` each implement a method that wraps
:py:func:`rail.core.RailStage.run`, taking input data and properly attaching it
to the stage, and wrapping the output data produced by the stage.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Building and configuring stages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.RailStage.make_and_connect
    :noindex:

.. automethod:: rail.core.RailStage.build
    :noindex:

.. automethod:: rail.core.RailStage.connect_input
    :noindex:

^^^^^^^^^^^^^^^^^^^^^^^^^^
Methods used by rail stage
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.RailStage.get_handle
    :noindex:

.. automethod:: rail.core.RailStage.add_handle
    :noindex:

.. automethod:: rail.core.RailStage.input_iterator
    :noindex:

.. automethod:: rail.core.RailStage.get_data
    :noindex:

.. automethod:: rail.core.RailStage.set_data
    :noindex:
