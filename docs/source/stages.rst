*********
RailStage
*********

:py:class:`rail.core.RailStage` is the main user facing class.  It
serves as the base class for all the classes that implement parts of
an analysis, and sets of `RailStage` can be combined into a
:py:class:`rail.core.RailPipeline` to perform a complete analysis.

In short, any `RailStage` does a single operation in a reproducible way.
It can be thought of as a way to wrap a single function so as to make
it both configurable and reproducible. 

This presents a few contraints and limitations, basically, the
`RailStage` needs use a save configuration to set any parameters it
uses, and it needs to get input from specified locations and write
to a specified location.  `RailStage` provides mechanism to do all of
these things, sub-classes must implement the actually work of the stage.


================
RailStage basics
================

.. autoclass:: rail.core.RailStage
    :noindex:

       
=======================
RailStage Functionality
=======================


Running a rail stage
--------------------

.. automethod:: rail.core.RailStage.run
    :noindex:

       
Note that subclass of `RailStage` each implement a method that
wraps :py:func:`rail.core.RailStage.run`, taking input data and
properly attaching it to the stage, and wrapping the output data
produced by the stage.


Building and configuring stages
-------------------------------

.. automethod:: rail.core.RailStage.make_and_connect		
    :noindex:

.. automethod:: rail.core.RailStage.build		
    :noindex:

.. automethod:: rail.core.RailStage.connect_input		
    :noindex:


Methods used by rail stage
--------------------------

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
