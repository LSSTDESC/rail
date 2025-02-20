*********
Pipelines
*********

A key concept in `rail` are ceci `Pipelines`, which run a series of
`RailStages` using the `ceci` framework.


================
Pipelines basics
================

:py:class:`rail.core.RailPipeline` is the base class for all RAIL
pipelines.   Subclasses can build particular types of analysis
piplines subject to some configuration choices, such as which
algorithms to use.

.. autoclass:: rail.core.RailPipeline
    :noindex:


======================
Pipeline Functionality
======================

Making a pipeline configuraiton file
------------------------------------

.. automethod:: rail.core.RailPipeline.build_and_write
    :noindex:


Introspection various types of Pipelines
----------------------------------------

.. automethod:: rail.core.RailPipeline.print_classes
    :noindex:
       
.. automethod:: rail.core.RailPipeline.get_pipeline_class
    :noindex:

.. automethod:: rail.core.RailPipeline.load_pipeline_class
    :noindex:


============================
Building pipelines with rail
============================

===========================
Running pipelines with ceci
===========================
