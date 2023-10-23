*****************
Example Notebooks
*****************

RAIL comes with several notebooks that demonstrate how to use it to analyze data in a number of different ways.

Here we describe the various notebooks and suggest other ways in which you might study the data.


Starting out, overview notebooks
================================

We recommend starting with the `Goldenspike <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/goldenspike_notebook.html>`_ notebook, 
which demonstrates a relatively simple end-to-end analysis.  This analysis starts off by making a model that can be used to generate synthetic 
catalogs of photometric data.  It then uses that model to create sets of synthetic data to train and test per-object redshift estimators, i.e., 
estimators that compute p(z).  From there it trains and tests a few estimators using some common algorithms.   It then evaluates the 
performance of those estimators.   Finally, it shows a few methods that converts p(z) for a set of objects to an ensemble distribution n(z).

The `estimation <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/RAIL_estimation_demo.html>`_ notebook 
focuses more on the estimation parts of the analysis, and demonstrates a few additional estimation algorithms.

The `evaluation <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/evaluation_examples/demo.html>`_ of the estimator performance is described in more depth in its own notebook.

Finally, we have collected demonstrations of `useful utilites <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Useful_Utilities.html>`_ to explore which packages and algorithms are available in the current RAIL installation.



Deeper dives into synthetic data creation
=========================================

The notebooks in  `this <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/creation_notebooks.html>`_ directory demonstrate how 
how to generate synthetic photometric data, and also how to "degrade" the synthetic data by applying various effects to the data.

These notebooks demonstrate utilities that can be used to prepare data for analysis, e.g., by `converting fluxes to magnitudes and applying dereddening <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/FluxtoMag_and_Deredden_example.html>`_ and by `converting fluxes to hyperbolic magnitudes <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/hyperbolic_magnitude_test.html>`_



Examples of using specific estimators
=====================================

These three notebooks demonstrate specific p(z) estimators in more detail, specifically, the `CMNN <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/CMNN_Demo.html>`_, `GPz <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/GPz_Estimation_Example.html>`_ and `NZDIR 
<https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/NZDir.html>`_ algorithms.

These two notebooks demonstrate self-organizing map (SOM) based algorithms that estimate the ensemble n(z) distribution: `the first  <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/somocluSOM_demo.html>`_ works with the SOM directly, 
while `the second <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/somocluSOMcluster_demo.html>`_ clusters the SOM cells to reduce statistical fluctuations.

Finally, `this notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/estimation_examples/test_sampled_summarizers.html>`_ demonstrates converting collections of per-object p(z) estimates to ensemble n(z) estimates.



Deeper explanations of rail concepts
====================================

The two notebooks demonstrate how to `convert a notebook into a ceci analysis pipeline 
<https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Build_Save_Load_Run_Pipeline.html>`_ and how to
`run an existing pipeline <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Run_Pipe.html>`_

This notebook explains the concept of the `Data Store <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/FileIO_DataStore.html>`_ that keeps track of the data being used in an analysis pipeline, and which can be used to interactively access data.

Finally, `this notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/core_examples/Iterate_Tabular_Data.html>`_ demonstrates the mechanisms we use to iterate over tabular data, which is needed to avoid reading entire object catalogs into memory.



