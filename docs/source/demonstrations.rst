*****************
Example Notebooks
*****************

RAIL comes with several notebooks that demonstrate how to use it to analyze data in a number of different ways.

Here we describe the various notebooks and suggest and other in which you might study them.


Starting out, overview notebooks
================================

We recommend starting with the `Goldenspike <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/goldenspike_notebook.html>`_ notebook, 
which demonstrates a relatively simple end-to-end analysis.  This analysis starts off by making a model that can be used to generate synthetic 
catalogs of photometric data.  It then uses that model to create sets of synthetic data to train and test per-object redshift estimators, i.e., 
estimators that compute p(z).  From there it trains and test a few estimators using some common algorithms.   It then evaluates the 
performance of those estimators.   Finally, it shows a few methods that converts p(z) for a set of objects to an ensemble distribution n(z).

`This <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/RAIL_estimation_demo.html>_` notebook 
focus more on the estimation parts of the analysism, and demonstrates a few other algorithms.

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/evaluation_examples/demo.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Useful_Utilities.html



Deeper dives into synthetic data creation
=========================================

The notebooks in  `this <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/creation_notebooks.html>`_ directory demonstate how 
how to generate synthetic photometric data, and also how "degrade" the 

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/FluxtoMag_and_Deredden_example.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/hyperbolic_magnitude_test.html





Examples of using specific estimators
=====================================

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/CMNN_Demo.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/GPz_Estimation_Example.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/NZDir.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/somocluSOM_demo.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/somocluSOMcluster_demo.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/test_sampled_summarizers.html



Deeper explanations of rail concepts
====================================

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Build_Save_Load_Run_Pipeline.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Run_Pipe.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/FileIO_DataStore.html#

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Iterate_Tabular_Data.html

https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/iterator_test.html


