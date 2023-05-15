***************
Immediate plans
***************

This repo is home to a series of LSST-DESC projects aiming to quantify the impact of imperfect prior information on probabilistic redshift estimation.
An outline of the baseline RAIL is illustrated `here <https://docs.google.com/drawings/d/1or8xyBqLkpc_4_Cr-ROSA3F7fBm3RMRnRzytorw_FYM/edit?usp=sharing>`_.

1. *Golden Spike*: Build the basic infrastructure for controlled experiments of forward-modeled photo-z posteriors
==================================================================================================================

* a `rail.creation` subpackage that can generate true photo-z posteriors and mock photometry.

* a `rail.estimation` subpackage with a superclass for photo-z posterior estimation routines and at least one subclass template example implementing the trainZ (experimental control) algorithm.

* a `rail.evaluation` subpackage that calculates at least the metrics from the `PZ DC1 Paper <https://github.com/LSSTDESC/PZDC1paper>`_ for estimated photo-z posteriors relative to the true photo-z posteriors.

* documented scripts that demonstrate the use of RAIL in a DC1-like experiment on NERSC.

* sufficient documentation for a v1.0 release.

* an LSST-DESC Note presenting the RAIL infrastructure.

2. *RAILroad*: Quantify the impact of nonrepresentativity (imbalance and incompleteness) of a training set on estimated photo-z posteriors by multiple machine learning methods
===============================================================================================================================================================================

* parameter specifications for degrading an existing `Creator` to make an imperfect prior of the form of nonrepresentativity into the observed photometry.

* at least two `Estimator` wrapped machine learning-based codes for estimating photo-z posteriors.

* additional `Evaluator` metrics with feed-through access to the `qp <https://github.com/LSSTDESC/qp>`_ metrics.

* end-to-end documented scripts that demonstrate a blinded experiment on NERSC.

* an LSST-DESC paper presenting the results of the experiment.
