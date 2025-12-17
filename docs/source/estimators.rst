*****************************
Photo-z Estimation Algorithms
*****************************

`rail.estimation` encompasses all methods that derive redshift information from
photometry, as either an estimate of per-galaxy photo-z PDFs, a summary of the redshift
distribution $n(z)$ for an ensemble of galaxies, or tomographic bin assignments.
Technically, information other than photometry can also be input to the photo-z
algorithms and is allowed in RAIL, especially for the machine learning methods. Every
such method is implemented with an `Informer` stage paired with any combination of
`Estimator`, `Summarizer`, and `Classifier`, depending on which procedures are supported
by the underlying estimator and wrapped for RAIL.

An `Estimator` produces a `qp.ensemble` of per-galaxy photo-z PDFs, a `Summarizer`
produces a `qp.ensemble` of redshift distributions and/or samples thereof, and a
`Classifier` produces per-galaxy integer class IDs for tomographic binning.

`Informer` generates a model for the `Estimator`, `Summarizer`, and `Classifier` by the
training data. Because ceci requires stages to have fixed numbers and types of inputs,
each of these stage types is implemented in at least one flavor specifying what it takes
as input; `CatInformer` and `CatEstimator` take as input a photometric galaxy catalog
with magnitudes; `PZInformer`, `PZClassifier`, and `PZSummarizer` take as input a
`qp.ensemble` of per-galaxy photo-z PDFs; and `SZPZSummarizer` takes as input both a
spectroscopic galaxy catalog and a `qp.ensemble` of per-galaxy photo-z PDFs. Specific
algorithms, which are detailed below, are implemented as subclasses of these parent
classes.


====================================
BPZ (Bayesian Photometric Redshifts)
====================================

RAIL Package: https://github.com/LSSTDESC/rail_bpz

BPZ is a template-based estimator developed by [Benitez et al
(2000)](https://ui.adsabs.harvard.edu/abs/2000ApJ...536..571B).  Like many
template-based codes, it operates by computing synthetic fluxes for an input set of SEDs
by integrating the products of the SEDs and the filter bandpass curves for a particular
survey.

The `BPZliteEstimator` stage takes a `TableHandle` catalog of magnitudes and magnitude
errors as input, and returns an interpolated grid `qp.Ensemble` of posterior PDFs.  As
the likelihood values are computed on a grid, the mode values for each galaxy as
measured on the grid are also returned by default.  Also included in the ancillary data
are values `tb` corresponding to the `best-fit SED type` (evaluated at the mode
redshift), and `todds`, a parameter that gives the fraction of the probability that
comes from SED type `tb` at the mode redshift.  Low values of `todds` mean that multiple
SEDs are contributing to the probability total at the mode redshift, and thus a `best
fit type` is ill-defined, while values close to unity mean that most or all of the
probability is from a single SED type, and thus the use of a `best fit type` may be
appropriate for the individual galaxy.

.. autoclass:: rail.estimation.algos.bpz_lite.BPZliteInformer
    :noindex:

.. autoclass:: rail.estimation.algos.bpz_lite.BPZliteEstimator
    :noindex:

=====================================
CMNN (Color-Matched Nearest Neighbor)
=====================================

RAIL Package: https://github.com/LSSTDESC/rail_sklearn

`CMNN`, short for *Color-Matched Nearest Neighbor*, is a method introduced in [Graham et
al. (2018)](https://ui.adsabs.harvard.edu/abs/2018AJ....155....1G).  The algorithm
identifies nearest neighbors based on the Mahalanobis distance in color space from a set
of galaxies with known spectroscopic redshifts with the Mahalanobis distance.

Neighboring galaxies within a minimum Mahalanobis distance, defined via the percent
point function (PPF), are retained, and there are several options from which a user can
estimate a PDF from this subset: 1) a single galaxy from the subset is chosen at random
from the subset; 2) a single galaxy is chosen, but with a probability weighted by the
inverse of the square root of Mahalanobis distance; 3) the galaxy withthe smallest
Mahalanobis distance is chosen.  In all three instances, the PDF for a galaxy is
returned as a single Gaussian, where the central value is assigned to the spectroscopic
redshift of the galaxy chosen from one of the three options listed above, and the
uncertainty is calculated by computing the standard deviation of all galaxies in the
minimum distance subset. When there are less than $n_{\rm min}$ galaxies in the subset,
the redshift will fail and an error flag is assigned to the galaxy.


.. autoclass:: rail.estimation.algos.cmnn.CMNNInformer
    :noindex:

.. autoclass:: rail.estimation.algos.cmnn.CMNNEstimator
    :noindex:


=======
Delight
=======

RAIL Package: https://github.com/LSSTDESC/rail_delight

[Leistedt et al. (2017)](https://ui.adsabs.harvard.edu/abs/2017ApJ...843...25L)
introduced a novel approach to inferring photometric redshifts which combines some of
the strengths of machine learning and template-fitting methods by implicitly
constructing flexible template SEDs directly from the spectroscopic training data,
called Delight. It is a method for calculating the posterior probability of redshift
given a catalog of deep observations acting as a data-driven prior. The catalog can have
observations in arbitrary bands and with arbitrary noise; Gaussian processes are used as
a principled method to implicitly construct SEDs (capturing the effects of redshifts,
bandpasses and noise). The hyperparameters of the Gaussian process can be optimized as a
calibration step.

.. autoclass:: rail.estimation.algos.delight_hybrid.DelightInformer
    :noindex:

.. autoclass:: rail.estimation.algos.delight_hybrid.DelightEstimator
    :noindex:


======================================
DNF (Directional Neighborhood Fitting)
======================================

RAIL Package: https://github.com/LSSTDESC/rail_dnf

`DNF` (Directional Neighborhood Fitting) is a photometric redshift estimation method
described by [De Vicente et al.
(2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.459.3078D). The algorithm estimates
the photo-z of each galaxy from the hyperplane that best fits its directional
neighborhood in the training sample. `DNF` supports three main distance metrics: `ENF`
(Euclidean Neighborhood Fitting), `ANF` (Angular Neighborhood Fitting), and a
combination of both (`DNF`). `ENF` relies on the Euclidean distance, making it a
straightforward and commonly used approach in k-Nearest Neighbors (`kNN`) methods. `ANF`
uses a normalized inner product, which provides the most accurate redshift predictions,
particularly in data sets with fluxes in more than four bands and sufficiently high
signal-to-noise ratios. Finally, `DNF` combines the Euclidean and angular metrics,
improving accuracy in cases of few bands and low signal-to-noise conditions.

`DNF` provides two photometric redshift estimates: `DNF_Z`, which is computed as the
weighted average or hyperplane fit of a set of neighbors determined by a specific
metric, and `DNF_ZN`, which corresponds to the redshift of the closest neighbor and can
be used for estimating the sample redshift distribution.

To construct the PDF for photometric redshifts, `DNF` selects a set of nearest neighbors
based on one of these distance metrics and assigns weights to them. The PDF is computed
by estimating the redshift distribution of the selected neighbors and applying a
Gaussian smoothing function to account for uncertainties.

.. autoclass:: rail.estimation.algos.dnf.DNFInformer
    :noindex:

.. autoclass:: rail.estimation.algos.dnf.DNFEstimator
    :noindex:


==========
FlexZBoost
==========

RAIL Package: https://github.com/LSSTDESC/rail_flexzboost

`FlexZBoost` ([Izbicki & Lee,
2017](https://academic.oup.com/mnras/article/499/2/1587/5905416), [Dalmasso et al.,
2020](https://academic.oup.com/mnras/article/499/2/1587/5905416)) is an algorithm based
on conditional density estimation that uses the `FlexCode` package (available at
[https://github.com/lee-group-cmu/FlexCode](https://github.com/lee-group-cmu/FlexCode)).
The package parameterizes the PDF as a linear combination of orthonormal basis functions
(a set of unit vectors in the color space that are orthogonal to each other), where the
basis function coefficients can be determined by regression. The `rail` implementation
uses `xgboost` ([Chen & Guestrin, 2016](https://arxiv.org/abs/1603.02754)) to perform
the regression. The basis function representation of the photo-z PDF of a galaxy can
lead to small-scale residual "bumps". In the course of training the density estimate, an
optimal threshold (configuration parameter `bump_thresh`) below which small-scale
features are removed is determined by setting aside a fraction of the training data and
minimizing the CDE loss at different threshold values. Additionally, the width of the
final PDF is similarly optimized by the inclusion of a "sharpening" parameter that
scales the PDF by a power law value $\alpha$. Again, a fraction of the training data is
set aside and the CDE loss is minimized over a set of $\alpha$ values. The resultant
photo-z PDF distributions can be stored as `qp.Ensembles` either in their native basis
function representation or as a linearly interpolated grid.


.. autoclass:: rail.estimation.algos.flexzboost.FlexZBoostInformer
    :noindex:

.. autoclass:: rail.estimation.algos.flexzboost.FlexZBoostEstimator
    :noindex:


===
GPz
===

RAIL Package: https://github.com/LSSTDESC/rail_gpz_v1

`GPz` is an algorithm based on sparse Gaussian Processes, introduced by [Almosallam et
al. (2016)](https://arxiv.org/abs/1604.03593). The current `rail` implementation of
`GPz` is a preliminary version; it predicts a single Gaussian PDF rather than the more
sophisticated multimodal PDFs implemented in newer versions of `GPz` ([Stylianou et al.,
2022](https://arxiv.org/abs/2202.12775)). `GPz` models both the mean and standard
deviation of the Gaussian PDF as a linear combination of basis functions, learning the
parameters for these basis functions via a Gaussian process. The method can make several
assumptions about the covariance between these basis functions, controlled via the
configuration parameter `gpz_method` as outlined in the `rail` documentation.


.. autoclass:: rail.estimation.algos.gpz.GPzInformer
    :noindex:

.. autoclass:: rail.estimation.algos.gpz.GPzEstimator
    :noindex:

==================
k-Nearest Neighbor
==================

RAIL Package: https://github.com/LSSTDESC/rail_sklearn

The nearest-neighbor code estimates redshift PDFs as a Gaussian mixture model, where the
number of Gaussians, M, is determined during the inform stage, as are the width of the
Gaussians. This is done by setting aside a fraction of the training data as a validation
set and minimizing the Conditional Density Estimate (CDE) Loss of the PDFs versus the
true values for that set.  `KNearNeighInformer` uses `sklearn.neighbors.KDTree` to build
a tree from the colors, or colors plus a reference band magnitude, of the training data.
`KNearNeighEstimator`  then searches the tree for the `M` closest neighbors, and
constructs a PDF with `M` Gaussians centered at each of the corresponding nearest
neighbor redshifts.

.. autoclass:: rail.estimation.algos.k_nearneigh.KNearNeighInformer
    :noindex:

.. autoclass:: rail.estimation.algos.k_nearneigh.KNearNeighEstimator
    :noindex:

=======
LePhare
=======

RAIL Package: https://github.com/LSSTDESC/rail_lephare

We have implemented the LePHARE code within `rail`. LePHARE (Photometric Analysis for
Redshift Estimation) is a template-fitting algorithm originally introduced by [Arnouts
et al. (1999)](https://ui.adsabs.harvard.edu/abs/1999MNRAS.310..540A) and further
developed by [Ilbert et al.
(2006)](https://ui.adsabs.harvard.edu/abs/2006A%26A...457..841I). It is written in C++
with a `Python` wrapper and is used to estimate redshift and physical property
posteriors.

Within `rail`, we have integrated LePHARE with a default set of parameters optimized for
LSST passbands. However, it remains fully customizable, consistent with the general
LePHARE configuration parameters, which are extensive and well documented. These default
configurations are based on those used for the COSMOS2020 data sets, as detailed in
[Weaver et al. (2022)](https://ui.adsabs.harvard.edu/abs/2022ApJS..258...11W). The full
set of values is available in the public version of the LePHARE code.

This implementation adds functionality such as the estimation of stellar mass,
star-formation rate, and best-fitting model.


.. autoclass:: rail.estimation.algos.lephare.LephareInformer
    :noindex:

.. autoclass:: rail.estimation.algos.lephare.LephareEstimator
    :noindex:

==============
Neural Network
==============

RAIL Package: https://github.com/LSSTDESC/rail_sklearn

The neural network estimator is an unsophisticated implementation and is not meant to be
a competitive algorithm. Instead, it is used as a simple example code and a baseline
against which to test. This method constructs a model using
`sklearn.neural_network.MLPRegressor` to build a neural network trained on one magnitude
(set by the `ref_band` configuration parameter) and all of the colors from the training
data, though it first regularizes the data using
`sklearn.preprocessing.StandardScaler.transform`.

The network is set up using two hidden layers of size twelve, and a hyperbolic tangent
activation function. The estimation stage produces a Gaussian redshift PDF by running
the `MLPRegressor`'s `predict` method to estimate the mean redshift. A configuration
parameter, `width` is used to set the width of the Gaussian PDF, which is scaled by
(1+z) to increase with redshift, since the uncertainty in wavelength, which directly
translates to photo-z uncertainty, scales with (1+z).


.. autoclass:: rail.estimation.algos.sklearn_neurnet.SklNeurNetInformer
    :noindex:

.. autoclass:: rail.estimation.algos.sklearn_neurnet.SklNeurNetEstimator
    :noindex:

======
PZFlow
======

RAIL Package: https://github.com/LSSTDESC/rail_pzflow

`PZFlow` is a photometric redshift estimation algorithm that utilizes normalizing flows.
It takes a catalog of galaxy colors and redshifts and learns a differentiable mapping
from the data space to a simple latent space, such as a Normal distribution. A photo-$z$
posterior can then be estimated by evaluating this probability over a grid of redshifts
and normalizing the posterior to unit probability. See [Crenshaw et al.
(2024)](https://arxiv.org/abs/2405.04740) for more details.


.. autoclass:: rail.estimation.algos.pzflow_nf.PZFlowInformer
    :noindex:

.. autoclass:: rail.estimation.algos.pzflow_nf.PZFlowEstimator
    :noindex:

===============
Random Gaussian
===============

RAIL Package: https://github.com/LSSTDESC/rail_base

Benchmark algorithm.

.. autoclass:: rail.estimation.algos.random_gauss.RandomGaussInformer
    :noindex:

.. autoclass:: rail.estimation.algos.random_gauss.RandomGaussEstimator
    :noindex:


===
TPZ
===

RAIL Package: https://github.com/LSSTDESC/rail_tpz

.. autoclass:: rail.estimation.algos.tpz_lite.TPZliteInformer
    :noindex:

.. autoclass:: rail.estimation.algos.tpz_lite.TPZliteEstimator
    :noindex:


======
TrainZ
======

RAIL Package: https://github.com/LSSTDESC/rail_base

Benchmark Algorithm.

.. autoclass:: rail.estimation.algos.train_z.TrainZInformer
    :noindex:

.. autoclass:: rail.estimation.algos.train_z.TrainZEstimator
    :noindex:
