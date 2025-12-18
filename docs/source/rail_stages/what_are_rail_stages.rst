.. _rail-stages:

*********************
What Are RAIL Stages?
*********************

.. introduction
.. flowchart: stages to other stages

A RAIL stage is a configurable process that performs a single operation in a
reproducible way. Stages have defined inputs, outputs, and stage-specific
configuration parameters. They can be parallelized across processors or computing
nodes.

========
Examples
========

.. provide example use cases

------------------
Example Use Case 1
------------------

.. e.g. test how well estimation algorithms work under different degraders

------------------
Example Use Case 2
------------------

.. 

---------
Notebooks
---------

.. link to notebooks

===============
Types of Stages
===============

.. list each stage, i.e. creation, estimation, evaluation, explain each is known as a RAIL stage
.. include tool "stages"

There are three main types of stages in RAIL. For further reading, visit their
pages by clicking on their respective links.

#. :ref:`Creation <creation>`: create sample photometric data
#. :ref:`Estimation <estimation>`: estimate photometric redshift from any input data
#. :ref:`Evaluation <evaluation>`: evaluate the performance of estimations against known true values
#. :ref:`Tools <tools>`: "pseudo-stage" providing utilities and tools for running stages

----------------
Interactive Mode
----------------

.. link to interactive mode API

RAIL stages can be run interactively, such as in a Jupyter notebook. This is
done via specific command calls. 

To learn about the commands, visit the :ref:`interactive-api`.

To see more examples of using stages interactively, visit the
:ref:`interactive-notebooks`.

-------------
Pipeline Mode
-------------

.. format and check

:py:class:`rail.core.RailStage` is the main user facing class.  It serves as the
base class for all the classes that implement parts of an analysis, and sets of
``RailStage`` can be combined into a :py:class:`rail.core.RailPipeline` to perform
a complete analysis.

In short, any ``RailStage`` does a single operation in a reproducible way. It can
be thought of as a way to wrap a single function so as to make it both
configurable and reproducible.

This presents a few constraints and limitations, basically, the ``RailStage``
needs use a save configuration to set any parameters it uses, and it needs to
get input from specified locations and write to a specified location.
``RailStage``` provides mechanism to do all of these things, sub-classes must
implement the actually work of the stage.


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
