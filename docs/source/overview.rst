********
Overview
********

RAIL (Redshift Assessment Infrastructure Layers) is LSST-DESC software for the computation and assessment of redshifts derived from Rubin data.
RAIL addresses the challenge of enabling stress-testing of multiple photo-z codes in the presence of realistically complex systematic imperfections in the input photometry and prior information (such as template libraries and training sets), everything from the handling of diverse output storage formats to the propagation of assumptions inherent to individual codes to the architecture of the machines on which the code is run.
RAIL seeks to minimize such impacts by unifying much of the infrastructure in a single modular code base that can be used by photo-z developers and consumers alike.  
Beyond the comparison of different photo-z approaches, RAIL will be employed to generate photo-z catalogs used by DESC members in their science analyses. 

There are three aspects to the RAIL approach to photo-zs: the creation of self-consistently forward-modeled, realistically complex mock data for testing purposes, the estimation of individual galaxy and galaxy sample redshift uncertainties, and the evaluation of the results of the estimators by generic and science-specific metrics.
RAIL includes a subpackage for each, providing a flexible framework for handling different approaches and at least one baseline implementation of a method under that umbrella as an example for the broader community to integrate their own codes into RAIL.
The purpose of each piece of infrastructure is outlined below.
For a working example illustrating all four components of RAIL, see the `examples/goldenspike/goldenspike.ipynb <https://github.com/LSSTDESC/RAIL/blob/main/examples/goldenspike/goldenspike.ipynb>`_ jupyter notebook.


A brief note on core DESC software dependencies
===============================================

The `qp` Ensemble format is the expected default storage format for redshift information within DESC, and all redshift PDFs, for both individual galaxies and galaxy samples (such as tomographic bin members or galaxy cluster members), will be stored as `qp` Ensemble objects to be directly accessible to LSST-DESC pipelines, such as `TXPipe <https://github.com/LSSTDESC/TXPipe/>`_.
The use of a unified `qp` Ensemble as the output format enables a consistent evaluation of redshift uncertainties.  See `the qp repository <https://github.com/LSSTDESC/qp>`_ for more details, though in brief, `qp` enables transformation between different PDF parameterizations, computation of many useful metrics, and easy fileIO.

`creation`
==========

The creation subpackage has two main components enabling forward-modeling of realistically complex mock data.
The creation modules provide a joint probability space of redshift and photometry, and the degradation modules introduce systematic imperfections into galaxy catalogs, which can be used to stress-test photo-z estimators. 

**Creation modules**: 
This code enables the generation of mock photometry corresponding to a fully self-consistent forward model of the joint probability space of redshift and photometry.  
Beyond simply drawing samples of redshift and photometry defining galaxy catalogs, this forward model-based approach can provide a true posterior and likelihood for each galaxy, enabling novel metrics for individual galaxies that are not available from traditionally simulated catalogs without a notion of inherent uncertainty.

**Creation base design**: 
To ensure the mutual consistency of RAIL's mock data with known physics but leaving open the possibility of surprises beyond current data, we make an interpolative and extrapolative model beginning from input data of galaxy redshifts and photometry, for example, the DC2 extragalactic catalog.
While multiple generating engines are possible and desired, our initial implementation utilizes a normalizing flow via the `pzflow package <https://github.com/jfcrenshaw/pzflow>`_. 
The normalizing flow model fits the joint distribution of redshift and photometry (and any other parameters that are supplied as inputs), and galaxy redshifts and photometry drawn from that joint probability density will have a true likelihood and a true posterior.

**Degradation modules**: 
Degraders build upon the creator models of the probability space of redshift and photometry to emulate realistically complex imperfections, such as physical systematics, into mock data, which can be used to generate self-consistent photometric training/test set pairs.
The high-dimensional probability density outlined in the `creation` directory can be modified to reproduce the realistic mismatches between training and test sets, for example inclusion of photometric errors due to observing effects, spectroscopic incompleteness from specific surveys, incorrect assignment of spectroscopic redshift due to line confusion, the effects of blending, etc.
Training and test set data may be drawn from such probability spaces with systematics applied in isolation, which preserves the existence of true likelihoods and posteriors, though applying multiple degraders in series enables more complex selections to be built up. 

**Degradation base design**: 
The base design for degraders in our current scheme is that degraders take in a DataFrame (or a creator that can generate samples on the fly) and returns a modified dataframe with the effects of exactly one systematic degradation.  
That is, each degrader module should model one isolated form of degradation of the data, and more complex models are built by chaining degraders together.  
While the real Universe is usually not so compartmentalized in how systematic uncertainties arise, realistically complex effects should still be testable when a series of chained degraders are applied.  
RAIL has several degraders currently included: a (point-source-based) photometric error model, spectroscopic redshift LineConfusion misassignment, a simple redshift-based incompleteness, and generic QuantityCut degrader that lets the user cut on any single quantity. 

**Usage**: 
In the `example` directory, you can execute the creation/posterior-demo.ipynb and creation/degredation-demo.ipynb notebooks.

**Creation future extensions**: 
In the future, we may need to consider a probability space with more data dimensions, such as galaxy images and/or positions in order to consider codes that infer redshifts using, e.g. morphological, positional, or other sources of information.
Similarly, to evaluate template-fitting codes, we will need to construct the joint probability space of redshifts and photometry from a mock data set of SEDs and redshifts, which could include complex effects like emission lines.

**Degradation future extensions**: 
Building up a library of degraders that can be applied to mock data in order to model the complex systematics that we will encounter is the first step of extending functionality.  
Some systematics that we would like to investigate, such as incorrect values in the training set and blended galaxies, are in essence a form of model misspecification, which may be nontrivial to implement in the space of redshift and photometry probability density, and will likely not be possible with a single training set.
All effects will also need to be implemented for SED libraries in order to test template-fitting codes.

`estimation`
============

The estimation subpackage enables the automatic execution of arbitrary redshift estimation codes in a common computing environment.  
Each photo-z method usually has both an `inform` method that trains a model based on a dataset with known redshifts or ingests template information, and an `estimate` method that executes the particular estimation method.  
There are two types of quantities that RAIL can estimate: redshift PDFs for individual objects and overall PDFs for ensembles of objects, one obvious use case being tomographic redshift bins commonly used in cosmological analyses.  
Methods that estimate per-galaxy PDFs directly from photometry are referred to as Estimators, while those that produce a summary PDF and associated uncertainty of an ensemble of galaxies are referred to as Summarizers.
Individual estimation and summarization codes are "wrapped" as RAIL stages so that they can be run in a controlled way.  

**base design**: 
Estimators for several popular codes `BPZ_lite` (a slimmed down version of the popular template-based BPZ code), `FlexZBoost`, and delight `Delight` are included in rail/estimation, as are an estimator `PZFlowPDF` that uses the same normalizing flow employed in the creation module, and `KNearNeighPDF` for a simple color-based nearest neighbor estimator.  
The pathological `trainZ` estimator is also implemented.  
Several very basic summarizers such as a histogram of point source estimates, the naive "stacking"/summing of PDFs, and a variational inference-based summarizer are also included in RAIL.

**Usage**: 
In the `example` directory, you can execute the estimation/RAIL_estimation_demo.ipynb notebook.  
Estimation codes can also be run as ceci modules with variables stored in a yaml file.

**Immediate next steps**: 
More wrapped estimator and summarizer codes are always welcome for inclusion in upcoming comparison challenges, including at least one spatial clustering redshift estimator, a SOM or tree-based method, and a hierarchical inference, the simplest of which is `chippr <https://github.com/aimalz/chippr>`_.

`evaluation`
============

The evaluation module contains metrics for assessing the performance of redshift estimation codes.  
This can be done for "true" redshift draws from a distribution or catalog, or by comparing the marginalized "true" redshift likelihoods or posteriors from the creation module to the estimated PDFs.

**Base design**: 
The starting point for the evaluation module is to include metrics employed in the PZ DC1 paper `Schmidt & Malz et al. 2020  <https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.1587S/abstract>`_. 
Some simple evaluation metrics will employ aspects of the `qp <https://github.com/LSSTDESC/qp>`_ codebase (e.g. computing CDF values for Probability Integral Transform, aka PIT, distributions).

**Usage**: 
In the `example` directory, you can execute the evaluation/demo.ipynb jupyter notebook.

**Future extensions**: 
We aim to greatly expand the library of available metrics and welcome input from the community in doing so.  
An immediate extension would propagate estimated redshift posteriors to science-motivated metrics, and/or metrics related to computational requirements of the estimators. 
Within DESC, development of sophisticated metrics propagating photo-z uncertainties through cosmological probe analysis pipelines is now underway as part of Dark Energy Redshift Assessment Infrastructure Layers (DERAIL).
