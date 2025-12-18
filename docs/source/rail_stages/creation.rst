********
Creation
********

.. quick summary: covers everything that you would skip if you had real data
.. creating and modeling samples of photometric catalogs of galaxies and modifying them to add noise and biases

Creation is a type of RAIL stage which creates and models samples of photometric
catalogs of galaxies, and modifies them to add noise and biases. Creation stages
use creators to generate data, and degraders to add noise.

.. flowchart

.. contents:: Table of Contents
   :backlinks: top
   :local:

==================
Creators
==================

.. format and check

Mock DESC data are important for systematically testing the performance of
various photo-$z$ algorithms.  One of the lessons learned from DC1 is that it is
desirable for the mock data to include not only true redshifts and LSST
photometry (i.e., fluxes in the six LSST bands) but also true posterior PDFs,
$p(z_t | \mathbf{p}_t)$, which are unavailable for spectroscopically confirmed
data sets as well as traditional simulations.  Furthermore, the mock photometry
data should contain realistic noise, selection effects, and biases. This is
critical for the training and validation of photo-$z$ algorithms.

To address these needs, :py:class:`rail.creation` enables us to create datasets
with true PDFs that allow PDF-to-PDF metrics computations and forward-modeling
of mock data for validating photo-$z$ approaches under realistically complex
conditions.  This is realized by two main types of stages within
:py:class:`rail.creation`: (1) `engines` that forward-model photometric catalogs
and (2) `degraders` that modify such catalogs to introduce tunable physical
imperfections.


An engine is defined by a pair of stages that are subclasses of each of the
following superclasses: :py:class:`rail.creation.Modeler` makes a model of the
$p(z, \mathrm{photometry})$ joint probability space based on input parameters or
data, and :py:class:`rail.creation.Creator` samples $(z, \mathrm{photometry})$
from the forward model.

.. ============
.. Creators API
.. ============

.. format and check

--------------------------------------------
FSPS (Flexible Stellar Population Synthesis)
--------------------------------------------

RAIL Package: https://github.com/LSSTDESC/rail_fsps

`FSPS` is a RAIL module that creates an interface to the `Python` bindings of
the popular stellar population synthesis (SPS) code `FSPS` (Flexible Stellar
Population Synthesis, Conroy et al. 2009, 2010). `FSPS` aims at generating
realistic galaxy spectral energy distributions (SEDs) by modelling all the
components that contribute to the light from a galaxy: stars, gas, dust and AGN.
`FSPS` is widely used both for stellar population inference (Johnson et al.
1)    and for forward modelling of galaxy SEDs (e.g., Alsing et al. 2023,
Tortorelli et al. 2024).

`FSPS` provides substantial flexibility in terms of the prescription for
modelling each of the mentioned components. It also requires physical properties
of galaxies as input, such as star formation histories (SFHs), metallicities and
redshift, in order to generate their SEDs. We maintained this flexibility in the
interface we implemented in `RAIL`, allowing the user to change every possible
`FSPS` parameter. The code has been parallelized to make efficient use of the
multiprocessing capabilities of CPUs.

The interface is integrated in the `RAIL` workflow, requiring as input a catalog
of galaxy physical properties in the form of `Hdf5Handle`. These are galaxy
redshifts, stellar metallicities, velocity dispersions, gas metallicities and
ionization parameters (defined as the ratio of ionizing photons to the total
hydrogen density), dust attenuation and emission parameters, and star-formation
histories.

`FSPS` follows the structure of `engines`. The `Modeler` class requires galaxy
physical properties as input and produces as output an `Hdf5Handle` that
contains the `FSPS`-generated rest-frame SED for each galaxy and the common
rest-frame wavelength grid. The user can choose the units of the output
rest-frame SEDs by setting the appropriate keyword value. The default behavior
is to output the SEDs in a wavelength grid.

The output rest-frame SEDs constitute the input for the `FSPS` `Creator` class.
The latter computes apparent $\mathrm{AB}$ magnitudes for a set of user-defined
waveband filters. Notice that the wavelength range spanned by the waveband
filters should be within the SED observed-frame wavelength ranges. A default set
of filters is implemented in :py:`rail.fsps`, containing the Rubin LSST filters
among others.


.. autoclass:: rail.fsps.FSPSSedModeler
    :noindex:

.. autoclass:: rail.fsps.FSPSPhotometryCreator
    :noindex:

--------------------------------------------------
DSPS (Differentiable Stellar Population Synthesis)
--------------------------------------------------

RAIL Package: https://github.com/LSSTDESC/rail_dsps

`dsps` is a module that creates an interface in `RAIL` to the code `DSPS`
(Differentiable Stellar Population Synthesis, Hearin et al. 2023). `DSPS` is
implemented natively in the JAX library as its main aim is to produce
differentiable predictions for the SED of a galaxy based on SPS. The
implementation in JAX allows `DSPS` to be a factor of 5 faster than standard SPS
codes, such as `FSPS`, and more than 300 times faster, if run on a modern GPU.
`DSPS` does not come with stellar population templates; they must be provided by
the user. The code contains a series of convenience functions that allow the
user to generate stellar population templates with `FSPS`. If no templates are
supplied, the implementation in `RAIL` automatically downloads a set of
`FSPS`-generated stellar population templates.

The `Modeler` class of `dsps` requires as input a catalog of galaxy physical
properties in the form of `Hdf5Handles`. In particular, the user provides, for
each galaxy, a star-formation history, a grid of Universe age over which the
stellar mass build-up takes place, and a value for the mean and scatter of the
stellar metallicity distribution. The output is an `Hdf5Handle` that contains
galaxy rest-frame SEDs, produced over the stellar population template wavelength
grid.

The `Creator` class of `dsps` uses the output rest-frame SEDs to compute
apparent and rest-frame AB magnitudes for a set of user-defined filters.
Rubin-LSST filters are present in the default filter suite. The magnitudes are
computed using the appropriate functions implemented in `DSPS` that, much like
the SED generation, can take advantage of multiprocessing capabilities.

.. autoclass:: rail.dsps.DSPSSingleSedModeler
    :noindex:

.. autoclass:: rail.dsps.DSPSPopulationSedModeler
    :noindex:

.. autoclass:: rail.dsps.DSPSPhotometryCreator
    :noindex:

-------------
PZFlow Engine
-------------

RAIL Package: https://github.com/LSSTDESC/rail_pzflow

`PZFlow` is a generative model that simulates galaxy catalogs using normalizing
flows. Normalizing flows learn differentiable mappings between complex data
distributions and a simple latent distribution, for example, a Normal
distribution, hence the name *normalizing* flow.  In the creation module, a
normalizing flow is trained to map the distribution of galaxy colors and
redshifts onto a simple latent distribution.  New galaxy catalogs can then be
simulated by sampling from the latent distribution and applying the inverse flow
to the samples.  In addition, because the samples are generated by sampling from
a distribution we have direct access to, there is a natural notion of a *true*
redshift distribution for each galaxy in the catalog.  For more information, see
Crenshaw et al. 2024. Note that `PZFlow` is also used to perform photo-$z$
estimation.

.. autoclass:: rail.pzflow.FlowModeler
    :noindex:

.. autoclass:: rail.pzflow.FlowPosterior
    :noindex:

====================
Degraders 
====================

.. format and check

Each engine produces a catalog from some input information, but turning the
truth catalog into realistically imperfect observations necessitates additional
steps in a forward model. A degrader may be a subclass of either
:py:class:`rail.creation.noisifier` (later referred to as noisifier) or
:py:class:`rail.creation.selector` (later referred to as selector), the first of
which modifies data in place and the second of which removes rows from a
catalog. The only exception is the blending degrader, which changes both. We
provide several survey-specific shortcuts to mimic the selection functions of
precursor data sets. Specifically, the noisifier superclass imposes
realistically complex noise and bias to the (𝑧, photometry) columns, and the
selector superclass introduces biased selection on the sample to mimic, e.g., an
incomplete spectroscopic training sample.

.. =============
.. Degraders API
.. =============

.. format and check

----------------
LSST Error Model
----------------

The `LSSTErrorModel` is a wrapper of the PhotErr photometric error model (Crenshaw et
al. 2024). `PhotErr` is a generalization of the error model described in Ivezić et al.
(2019) that includes multiple methods for modeling photometric errors, non-detections,
and extended source errors. In addition to photometric error model for LSST, we also
include models for Euclid (Euclid Collaboration et al. 2022) and Nancy Grace Roman
(Spergel et al. 2015) space telescopes. The magnitude errors are estimated based on the
input galaxy properties and the survey conditions, such as 5𝜎 depth and seeing, and
each galaxy has noise added to its magnitude according to a Gaussian distribution with
mean zero and standard deviation equal to its magnitude error. For more information, see
Appendix B of Crenshaw et al. (2024).

.. autoclass:: rail.astro_tools.PhotoErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.LSSTErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.RomanErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.RomanWideErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.RomanMediumErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.RomanDeepErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.RomanUltraDeepErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.EuclidErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.EuclidWideErrorModel
   :noindex:

.. autoclass:: rail.astro_tools.EuclidDeepErrorModel
   :noindex:

----------------------------
Observing Condition Degrader
----------------------------

This degrader produces observed magnitude and magnitude errors for the truth sample,
based on the input survey condition maps (Hang et al. 2024). The user provides a series
of survey condition maps in ``HEALPix`` (Górski et al. 2005) format with specified
𝑁side, e.g. the 5𝜎 depth in each band. The galaxies in the truth sample will be
assigned survey conditions corresponding to their ``HEALPix`` pixel, either based on
their coordinates in the original catalog, or randomly if only photometry is available
(e.g., generated from the engines). In the latter case, a weight map can be specified to
adjust the number of galaxies assigned to each pixel. A key input for
``ObservingConditionDegrader`` is ``map_dict``. This is a dictionary containing keys
with the same names as parameters for LSSTErrorModel. Under each key, one can pass a
series of paths for the survey condition maps for each band, or, if any quantity is held
constant throughout the footprint, one can also pass a float number. The degrader then
calls PhotErr to compute noisy magnitudes for each galaxy in each ``HEALPix`` pixel. The
output of this module is a table containing degraded magnitudes, magnitude errors, RA,
Dec, and the ``HEALPix`` pixel index of each galaxy.

.. autoclass:: rail.astro_tools.ObsCondition
   :noindex:

-----------------------
Spectroscopic Degraders
-----------------------

``SpectroscopicDegraders`` contains two simple degraders that simulate systematic errors
associated with the presence of spectroscopic redshifts in spectroscopic training
catalogs.

The first is ``InvRedshiftIncompleteness``. It is a toy model for redshift
incompleteness -- i.e., the failure of a particular spectrograph to obtain a redshift
estimate for a particular set of galaxies. It takes an input catalog and keeps all the
galaxies below a configurable redshift threshold while randomly removing galaxies above
it. The probability that a redshift $z$ galaxy is kept is:

$p(z) - \mathrm{min}\left( 1, \frac{z_\mathrm{th}}{z} \right)$,

where $z_\mathrm{th}$ is the threshold redshift.

The other degrader is ``LineConfusion``, which simulates redshift errors due to the
confusion of emission lines. For example, if the OII line at $3727 \text{\AA}$ was
misidentified as the OIII line at $5007 \text{\AA}$, the assigned spectroscopic redshift
would be greater than the true redshift (Newman et al. 2013). The inputs of this
degrader are a `true' and `wrong' redshift, and an error rate. The degrader then
randomly simulates line confusion, ignoring galaxies for which the misidentification
would result in a negative redshift (which can occur when the wrong wavelength is
shorter than the true wavelength).

.. autoclass:: rail.astro_tools.LineConfusion
   :noindex:

.. autoclass:: rail.astro_tools.InvRedshiftIncompleteness
   :noindex:


-----------
QuantityCut
-----------

This degrader provides a trimmed version of the input catalog based on selection cuts
applied to the catalog quantities. The user provides the parameter cuts, which is a
dictionary with keys being the columns to which the selection is to be applied (e.g.,
the 𝑖-band magnitude), and the values being the specific cuts. Two types of values can
be provided: a single float number (e.g., 25.3), which is interpreted as a maximum value
(i.e., the cut will remove samples with 𝑖 > 25.3), and a tuple (e.g., (17, 25.3)),
which is interpreted as a range within which the sample is selected (i.e., the selected
sample has 17 < 𝑖 < 25.3). When multiple cuts are applied at the same time, only the
intersection of selected samples of each cut will be kept in the output.

.. autoclass:: rail.creation.degraders.quantityCut.QuantityCut
   :noindex:

-----------------------
Spectroscopic Selectors
-----------------------

The ``SpectroscopicSelection`` degrader applies the selection for a spectroscopic
survey. It provides tailored catalogs that match a particular spectroscopic survey for
subsequent calibration steps. It can also be used to generate selected mock catalogs
used as realistic reference samples. The selection criteria are cuts on magnitudes or
colors adopted for the associated spectroscopic survey targeting. The current available
selectors are for VVDSf02 (Le Fèvre et al. 2005), zCOSMOS (Lilly et al. 2009), GAMA
(Driver et al. 2011), BOSS (Dawson et al. 2013), and DEEP2 (Newman et al. 2013).
SpectroscopicSelection requires a 2-dimensional spectroscopic redshift success rate as
a function of two variables (often two of magnitude, color, or redshift), specific to
the redshift survey for which selection is being emulated. The degrader will draw the
appropriate fraction of samples from the input data and return an incomplete sample.
Additional redshift cuts based on percentile can be applied when using a color-based
redshift cut.

Similar functionality is provided by ``GridSelection`` (Moskowitz et al. 2024), which
can be used to model spectroscopic success rates for the training sets used for the
second data release of the Hyper Suprime Cam Subaru Strategic Program (HSC; Aihara et
al. 2019). Given a 2-dimensional grid of spectroscopic success ratio as a function of
two variables (often magnitude or color), the degrader will draw the appropriate
fraction of samples from the input data and return incomplete sample. Additional
redshift cuts can also be applied, where all redshifts above the cutoff are removed. In
addition to the default HSC grid, RAIL accepts user-defined setting files for the
success ratio grids appropriate for other surveys.

.. autoclass:: rail.astro_tools.SpecSelection
   :noindex:

.. autoclass:: rail.astro_tools.SpecSelection_GAMA
   :noindex:

.. autoclass:: rail.astro_tools.SpecSelection_BOSS
   :noindex:

.. autoclass:: rail.astro_tools.SpecSelection_DEEP2
   :noindex:

.. autoclass:: rail.astro_tools.SpecSelection_VVDSf02
   :noindex:

.. autoclass:: rail.astro_tools.SpecSelection_zCOSMOS
   :noindex:

.. autoclass:: rail.astro_tools.SpecSelection_HSC
   :noindex:

. .autoclass: rail.astro_tools.GridSelection

---------------
SOMSpecSelector
---------------


While ``GridSelection`` defines a selection mask in two dimensions, ``SOMSpecSelector``
can take any number of input features with which to define a spectroscopic selection.
This selector takes an initial complete sample (which we will call the input sample) and
return a subset that approximately matches the properties of an incomplete sample (we
will refer to this as the specz sample). The selector operates by taking the list of
features (which must be present in both the input and specz samples) and constructs a
self-organizing map (SOM; Kohonen 1982) from the input data, creating a mapping from the
higher-dimensional feature set to the 2D grid of SOM cells. It then finds the best cell
assignment for each galaxy in both the input and specz samples. The selector builds a
mask as it iterates over all cells, and for each cell returns a random subset of input
objects that lie in that cell that equal in number to specz objects in the cell. If the
cell has more specz objects than are available in the input catalog, then it returns all
that are available. By matching the number of objects cell by cell the selector
naturally mimics the features of the specz sample.


.. autoclass:: rail.creation.degraders.specz_som.SOMSpecSelector
   :noindex:


-----------------
Blending Degrader
-----------------


This degrader creates mock unrecognized blends based on source density. Unrecognized
blends are sources overlapping too closely in projection and are detected as one object
(referred to as `ambiguous blends' in Dawson et al. 2016). This degrader first searches
for close objects that are likely to become unrecognized blends, then merges their
fluxes to create one blended object. The source IDs of blend components are saved for
references.

The blending components are found by matching the RA and Dec coordinates of an input
catalog with itself via a Friends-of-Friends (FoF) algorithm (Mao et al. 2021). The
advantage of the FoF algorithm is that it can produce unrecognized blends from multiple
sources rather than just pairs. The algorithm groups sources such that within each
group, every source is separated from at lease one another group member by an angular
distance less than a specified `linking length'. By setting a small enough linking
length (e.g., 1 arcsec), we assume that all group members will be blended into one
detection. In the future, we might implement options for a more sophisticated
identification of blends using source sizes and shapes. In the current release, this
degrader simply sums up fluxes over all group members to create one blended object per
group. Note that we do not currently simulate the impact on aperture photometry due to
irregular profiles of blends either, but are motivated to conduct such a study in the
future.

Note that the truth redshifts of blended objects are ambiguous since they are composed
of multiple objects. We provide several summary columns for the truth: ``z_brightest``
is the redshift of the brightest component; ``z_mean`` is the average redshift of all
components; and ``z_weighted`` is the flux-weighted average redshift. For blended
objects composed of more than (including) two components, the standard deviation of
redshifts is provided. The decision on the truth redshift is left to the users. For more
complicated truth estimation -- e.g., considering the colors of components, as bluer
galaxies tend to have strong emission lines which are often used to infer redshifts from
spectroscopy -- users have the option to trace the components with source IDs. The
tutorial ``blending_degrader_demo`` illustrates how to match the output catalog with the
source IDs and the input catalog to access more information.

The order of application is particularly important for this degrader. Generally, this
degrader should be applied before any selections on the truth catalog, including any
magnitude, color, or signal-to-noise ratio cuts. The reason is that bright sources can
blend with fainter ones, and two faint sources might blend into a brighter object that
enters the target depth selection. For example, a magnitude difference of $\sim2.5$
translates roughly into a flux contamination of 10%. However, applying this degrader to
the original truth catalog without any cuts can be a computational burden, because the
truth catalog is often much larger than the target-depth catalog. To mitigate this
issue, one can use a magnitude cut to decrease the target depth by {an arbitrary
threshold (e.g., 2 or 3 magnitudes)} before running this degrader.

While preliminary studies have addressed some aspects of blending on photo-z  (e.g.,
Nourbakhsh et al. 2022), a thorough quantitative exploration of this topic will be
important to develop a deeper understanding of the issue and its impacts on various
science cases.


.. autoclass:: rail.creation.degraders.unrec_bl_model.UnrecBlModel
   :noindex:
