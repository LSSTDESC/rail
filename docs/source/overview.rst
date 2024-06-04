********
Overview
********

RAIL enables production of photo-z data products at-scale for LSST as well as 
stress-testing of multiple estimation approaches in the presence of realistically 
complex systematic imperfections in the input photometry and prior information 
(such as template libraries and training sets) under science-agnostic and 
science-specific metrics. By providing both functionalities in the same package, 
the exact same estimation procedure validated through controlled experimentation 
may be applied to real data without loss of validity. To support such an ambitious 
goal, RAIL has a highly modular structure encompassing three aspects of this kind 
of experiment, enabled by specialized object types; however, the result is that 
RAIL is unavoidably complicated. This overview seeks to present the foundational
building blocks that underlie RAIL's structure, the overarching organizational 
philosophy, and the specific types of included functionality.


Introduction to stages and pipelines
************************************

While all of RAIL's functionality is accessible through Jupyter notebooks to 
facilitate experimentation, RAIL's utility is in being able to run the code
developed and validated under controlled conditions on real data at-scale by
executing scripts on high-performance computing clusters (HPCs).
The tool that RAIL uses to organize these scripts is 
`ceci <https://ceci.readthedocs.io/en/latest/>`_, a workflow management 
package specifically designed for running DESC analyses on HPCs, e.g. using 
`TXPipe <https://github.com/LSSTDESC/TXPipe/>`_. At a very high level, a 
workflow is a pipeline comprised of stages.

**Stages**:
A stage performs one unit of work, defined by its input(s) and output(s), its name, 
and its stage-specific configuration parameters. It can be parallelized across 
many processors, or even over many computing nodes. Stages produce output files in 
the directory in which they are executed. The RAIL-iverse provides a plethora of 
stages may be imported from the modules described below. 

**Pipelines**:
A pipeline is a directed acyclic graph of stages, defined by the guarantee that the 
inputs to each stage either exist already or are produced as output of earlier stages
in the pipeline. Pipelines are defined by a pair of `.yml` files, one specifying all 
the configuration parameters for every stage in the pipeline, including each stage's 
name and its inputs and outputs, and the other specifying the order in which the 
stages are to be run. Execution of a pipeline entails an `initialize()` step, in 
which `ceci` checks that each stage's inputs either exist or will be produced by an 
earlier stage in the pipeline, followed by a `run()` step to actually perform the 
specified calculations.


Core data structures
********************

**TODO: DataHandle/DataStore should be explained here**

**TODO: essential tables_io functionality should be introduced here**

**`qp.Ensemble` objects**:
Redshift data products may take many forms; probability density functions (PDFs) 
characterizing the redshift distribution of a sample of galaxies or each galaxy 
individually are defined by values of parameters under a choice of 
parameterization. To enable parameterization-agnostic downstream analyses,
the `qp <https://github.com/LSSTDESC/qp>`_ package provides a shared interface 
to many parameterizations of univariate PDFs and utilities for performing 
conversions, evaluating metrics, and executing at-scale input-output operations. 
RAIL stages provide and/or ingest their photo-z data products as ``qp.Ensemble`` 
objects, both for collections of individual galaxies and for the summarized 
redshift distribution of samples of galaxies (such as members of a tomographic 
bin or galaxy cluster members). The key features of a `qp.Ensemble` are the 
`metadata` of the type of parameterization and defining parameters shared by the 
entire ensemble, the `objdata` values unique to each row-wise member of the 
ensemble that specify its PDF given the `metadata`, and the `ancil` information 
associated to each row-wise member that isn't part of the parameterized PDF. 
**TODO: confirm the syntax here and link to qp demos**


Organizational philosophy and included functionality
****************************************************

An end-to-end experiment entails the creation of self-consistently forward-modeled, 
realistically complex mock data for testing purposes, the estimation of individual 
galaxy and/or galaxy sample redshift uncertainties, and the evaluation of the 
resulting photo-z data products by informative metrics.
RAIL includes subpackages for each, providing a flexible framework for accessing 
implementations of approaches under each umbrella.
The purpose of each piece of infrastructure is outlined below.
For a working example illustrating all three components of RAIL, see the 
`examples/goldenspike_examples/goldenspike.ipynb <https://github.com/LSSTDESC/RAIL/blob/main/examples/goldenspike_examples/goldenspike.ipynb>`_ 
Jupyter notebook.

`creation`
==========

The creation subpackage has two main components enabling forward-modeling of 
realistically complex mock data.
The creation modules provide a joint probability space of redshift and photometry, 
and the degradation modules introduce systematic imperfections into galaxy catalogs, 
which can be used to stress-test photo-z estimators. 

**Creation modules**: 
This code enables the generation of mock photometry corresponding to a fully 
self-consistent forward model of the joint probability space of redshift and photometry. 
Beyond simply drawing samples of redshift and photometry defining galaxy catalogs, 
this forward model-based approach can provide a true posterior and likelihood for 
each galaxy, enabling novel metrics for individual galaxies that are not available 
from traditionally simulated catalogs without a notion of inherent uncertainty.

**Creation base design**: 
To ensure the mutual consistency of RAIL's mock data with known physics while leaving 
open the possibility of surprises beyond current data, we make an interpolative 
and extrapolative model beginning from input data of galaxy redshifts and photometry, 
for example, the DC2 extragalactic catalog.
While multiple generating engines are possible and desired, our initial implementation 
utilizes a normalizing flow via the `pzflow package <https://github.com/jfcrenshaw/pzflow>`_. 
The normalizing flow model fits the joint distribution of redshift and photometry 
(and any other parameters that are supplied as inputs), and galaxy redshifts and 
photometry drawn from that joint probability density will have a true likelihood 
and a true posterior.

**Degradation modules**: 
Degraders build upon the creator models of the probability space of redshift and 
photometry to emulate realistically complex imperfections, such as physical systematics, 
into mock data, which can be used to generate self-consistent photometric training/test 
set pairs.
The high-dimensional probability density outlined in the `creation` directory can 
be modified to reproduce the realistic mismatches between training and test sets, 
for example, inclusion of photometric errors due to observing effects, spectroscopic 
incompleteness from specific surveys, incorrect assignment of spectroscopic redshift 
due to line confusion, the effects of blending, etc.
Training and test set data may be drawn from such probability spaces with systematics 
applied in isolation, which preserves the existence of true likelihoods and posteriors, 
though applying multiple degraders in series enables more complex selections to 
be built up. 

**Degradation base design**: 
The base design for degraders in our current scheme is that degraders take in a 
DataFrame (or a creator that can generate samples on the fly) and return a modified 
dataframe with the effects of exactly one systematic degradation. 
That is, each degrader module should model one isolated form of degradation of 
the data, and more complex models are built by chaining degraders together. 
While the real Universe is usually not so compartmentalized in how systematic 
uncertainties arise, realistically complex effects should still be testable when 
a series of chained degraders are applied. 
RAIL has several degraders currently included: a (point-source-based) photometric 
error model, spectroscopic redshift LineConfusion misassignment, a simple 
redshift-based incompleteness, and generic QuantityCut degrader that lets the 
user cut on any single quantity. 

**Usage**: 
The ``examples/creation_examples`` directory provides notebooks demonstrating degradation:

* `creation_examples/posterior-demo.ipynb <https://github.com/LSSTDESC/RAIL/blob/main/examples/creation_examples/posterior-demo.ipynb>`_
* `creation_examples/degradation-demo.ipynb <https://github.com/LSSTDESC/RAIL/blob/main/examples/creation_examples/degradation-demo.ipynb>`_

**Creation future extensions**: 
In the future, we may need to consider a probability space with more data dimensions, 
such as galaxy images and/or positions in order to consider codes that infer redshifts 
using, e.g. morphological, positional, or other sources of information.
Similarly, to evaluate template-fitting codes, we will need to construct the joint 
probability space of redshifts and photometry from a mock data set of SEDs and 
redshifts, which could include complex effects like emission lines.

**Degradation future extensions**: 
Building up a library of degraders that can be applied to mock data in order to 
model the complex systematics that we will encounter is the first step of extending 
functionality. 
Some systematics that we would like to investigate, such as incorrect values in 
the training set and blended galaxies, are in essence a form of model misspecification, 
which may be nontrivial to implement in the space of redshift and photometry 
probability density, and will likely not be possible with a single training set.
All effects will also need to be implemented for SED libraries in order to test 
template-fitting codes.

`estimation`
============

The estimation subpackage enables the automatic execution of arbitrary redshift 
estimation codes in a common computing environment. 
Each photo-z method usually has both an ``inform`` method that trains a model 
based on a dataset with known redshifts or ingests template information, and an 
``estimate`` method that executes the particular estimation method. 
There are two types of quantities that RAIL can estimate: redshift PDFs for individual 
objects and overall PDFs for ensembles of objects, one obvious use case being 
tomographic redshift bins commonly used in cosmological analyses. 
Methods that estimate per-galaxy PDFs directly from photometry are referred to as 
Estimators, while those that produce a summary PDF and associated uncertainty of 
an ensemble of galaxies are referred to as Summarizers.
Individual estimation and summarization codes are "wrapped" as RAIL stages so 
that they can be run in a controlled way.

**base design**: 
Estimators for several popular codes ``BPZliteEstimator`` (a slimmed down version 
of the popular template-based BPZ code), ``FlexZBoostEstimator``, and ``DelightEstimator`` 
are included in rail/estimation, as are an estimator ``PZFlowEstimator`` that uses 
the same normalizing flow employed in the creation module, and ``KNearNeighEstimator`` 
for a simple color-based nearest neighbor estimator. 
The pathological ``TrainZEstimator`` estimator is also implemented. 
Several very basic summarizers such as a histogram of point source estimates, the 
naive "stacking"/summing of PDFs, and a variational inference-based summarizer are 
also included in RAIL.

**Usage**: 
The ``examples/estimation_examples`` directory provides notebooks demonstrating 
estimation.
Note that estimation codes can also be run as ceci modules with variables stored 
in a yaml file.

* `estimation_examples/RAIL_estimation_demo.ipynb <https://github.com/LSSTDESC/RAIL/blob/main/examples/estimation_examples/RAIL_estimation_demo.ipynb>`_

**Immediate next steps**: 
More wrapped estimator and summarizer codes are always welcome for inclusion in 
upcoming comparison challenges, including at least one spatial clustering redshift 
estimator, a SOM or tree-based method, and a hierarchical inference, the simplest 
of which is `chippr <https://github.com/aimalz/chippr>`_.

`evaluation`
============

The evaluation module contains metrics for assessing the performance of redshift 
estimation codes. 
This can be done for "true" redshift draws from a distribution or catalog, or by 
comparing the marginalized "true" redshift likelihoods or posteriors from the creation 
module to the estimated PDFs.

**Base design**: 
The starting point for the evaluation module is to include metrics employed in the 
PZ DC1 paper `Schmidt & Malz et al. 2020  <https://ui.adsabs.harvard.edu/abs/2020MNRAS.499.1587S/abstract>`_. 
Some simple evaluation metrics will employ aspects of the `qp <https://github.com/LSSTDESC/qp>`_ 
codebase (e.g. computing CDF values for Probability Integral Transform, aka PIT, 
distributions).

**Usage**: 
The `examples/evaluation_examples` directory provides the following demonstration notebook:

* `evaluation_examples/demo.ipynb <https://github.com/LSSTDESC/RAIL/blob/main/examples/evaluation_examples/demo.ipynb>`_.

**Future extensions**: 
We aim to greatly expand the library of available metrics and welcome input from 
the community in doing so. 
An immediate extension would propagate estimated redshift posteriors to science-motivated 
metrics, and/or metrics related to computational requirements of the estimators. 
Within DESC, development of sophisticated metrics propagating photo-z uncertainties 
through cosmological probe analysis pipelines is now underway as part of Dark Energy 
Redshift Assessment Infrastructure Layers (DERAIL).
