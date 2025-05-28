********************************************
Ensemble Redshift Distribution Algorithms
********************************************

The summarizers summarize the redshift distribution of an ensemble, whether based on photo-z or on other dataset such as spectroscopic redshift, or both. The calibration modules, which make adjustments globally to photo-z based on extra information from other datasets, usually reference samples of a spectroscopic survey, also are also among the summarizers. 


==========================================
Self Organizing Maps (minisom and somoclu)
==========================================

RAIL Package: https://github.com/LSSTDESC/rail_som

`rail_som` contains two implementations of SOM-based calibration: `minisom_som`, based on the light minimalistic SOM package [`minisom`](https://pypi.org/project/MiniSom/), and `somoclu_som` using the [`somoclu`](https://somoclu.readthedocs.io/en/stable/) package.

`somoclu` is a parallelized package capable of constructing SOMs on large datasets. It supports rectangular and hexagonal SOM cells, planar and toroidal topologies, and random or principal component analysis initialization. 

There is an option to further group the SOM cells into hierarchical clusters using the `AgglomerativeClustering` class from the `sklearn.cluster` package. This option adds flexibility and speed when grouping galaxies in the magnitude/color space.

Minisom informer and estimator:

.. autoclass:: rail.estimation.algos.minisom_som.MiniSOMInformer
    :noindex:

.. autoclass:: rail.estimation.algos.minisom_som.MiniSOMSummarizer
    :noindex:

Somoclu informer and estimator:

.. autoclass:: rail.estimation.algos.somoclu_som.SOMocluInformer
    :noindex:

.. autoclass:: rail.estimation.algos.somoclu_som.SOMocluSummarizer
    :noindex:
    
Useful function for the SOMoclu (see SOM tutorial for example):

.. automethod:: rail.estimation.algos.somoclu_som.get_bmus
    :noindex:

.. automethod:: rail.estimation.algos.somoclu_som.plot_som
    :noindex:

=================
Yet Another Wizz
=================

RAIL Package: https://github.com/LSSTDESC/rail_yaw

The method proposed in [Schmidt et al. (2013)](https://ui.adsabs.harvard.edu/abs/2013MNRAS.431.3307S) — measuring the correlation functions between pairs of photometric samples and reference samples in a single bin of radial distance between the two samples at a fixed physical scale — is implemented in [`yet_another_wizz`](https://github.com/jlvdb/yet_another_wizz) (YAW; [van den Busch et al., 2020](https://ui.adsabs.harvard.edu/abs/2020A%26A...642A.200V)). We provide a wrapper in `cc_yaw`.

This wrapper consists of a number of stages that interface with all primary YAW functionality:

- `YawCacheCreate`: Data preparation — splitting input data samples into regions for spatial resampling and covariance estimation.
- `YawAutoCorrelate`: Measurement of the angular autocorrelation function amplitude to estimate the evolution of galaxy bias with redshift.
- `YawCrossCorrelate`: Measurement of the angular cross-correlation amplitude.
- `YawSummarize`: Estimation of the ensemble redshift distribution according to Eq.~(X) (as referenced in the original context).

.. autoclass:: rail.estimation.algos.cc_yaw.YawCacheCreate
    :noindex:

.. autoclass:: rail.estimation.algos.cc_yaw.YawAutoCorrelate
    :noindex:
    
.. autoclass:: rail.estimation.algos.cc_yaw.YawCrossCorrelate
    :noindex:
    
.. autoclass:: rail.estimation.algos.cc_yaw.YawSummarize
    :noindex:
    
    

==============
Naive Stacking
==============

RAIL Package: https://github.com/LSSTDESC/rail_base

Stack the PDF of the photo-z output and normalize as the n(z) distribution.


.. autoclass:: rail.estimation.algos.naive_stack.NaiveStackInformer
    :noindex:
    
.. autoclass:: rail.estimation.algos.naive_stack.NaiveStackSummarizer
    :noindex:
    
.. autoclass:: rail.estimation.algos.naive_stack.NaiveStackMaskedSummarizer
    :noindex:
    

==============================
Variational Inference Stacking
==============================

RAIL Package: https://github.com/LSSTDESC/rail_base

.. autoclass:: rail.estimation.algos.var_inf.VarInfStackInformer
    :noindex:
    
.. autoclass:: rail.estimation.algos.var_inf.VarInfStackSummarizer
    :noindex:
    

========================
Point Estimate Histogram
========================

RAIL Package: https://github.com/LSSTDESC/rail_base

Use the point estimate histogram as n(z), baseline method. 

.. autoclass:: rail.estimation.algos.point_est_hist.PointEstHistInformer
    :noindex:
    
.. autoclass:: rail.estimation.algos.point_est_hist.PointEstHistSummarizer
    :noindex:
    
.. autoclass:: rail.estimation.algos.point_est_hist.PointEstHistMaskedSummarizer
    :noindex:
