*********
Pipelines
*********

A key concept in `rail` are ceci `Pipelines`, which run blocks of analysis code using `ceci`.


================
Pipelines basics
================

:py:class:`rail.core.RailPipeline` is the base class for all RAIL pipelines.

.. autoclass:: rail.core.RailPipeline
    :noindex:


====================
Pipeline definitions
====================

.. automethod:: rail.core.RailPipeline.print_classes
    :noindex:
       
.. automethod:: rail.core.RailPipeline.get_pipeline_class
    :noindex:

.. automethod:: rail.core.RailPipeline.load_pipeline_class
    :noindex:

.. automethod:: rail.core.RailPipeline.build_and_write
    :noindex:



============================
Building pipelines with rail
============================

===========================
Running pipelines with ceci
===========================
