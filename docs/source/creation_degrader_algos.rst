**********************
Degradation Algorithms
**********************

Each engine produces a catalog from some input information, but turning the truth catalog into realistically imperfect observations necessitates additional steps in a forward model. A degrader may be a subclass of either :py:class:`rail.creation.noisifier` (later referred to as noisifier) or :py:class:`rail.creation.selector` (later referred to as selector), the first of which modifies data in place and the second of which removes rows from a catalog. The only exception is the blending degrader, which changes both. We provide several survey-specific shortcuts to mimic the selection functions of precursor data sets. Specifically, the noisifier superclass imposes realistically complex noise and bias to the (𝑧, photometry) columns, and the selector superclass introduces biased selection on the sample to mimic, e.g., an incomplete spectroscopic training sample. 

================
LSST Error Model
================

The `LSSTErrorModel` is a wrapper of the PhotErr photometric error model (Crenshaw et al. 2024). `PhotErr` is a generalization of the error model described in Ivezić et al. (2019) that includes multiple methods for modeling photometric errors, non-detections, and extended source errors. In addition to photometric error model for LSST, we also include models for Euclid (Euclid Collaboration et al. 2022) and Nancy Grace Roman (Spergel et al. 2015) space telescopes. The magnitude errors are estimated based on the input galaxy properties and the survey conditions, such as 5𝜎 depth and seeing, and each galaxy has noise added to its magnitude according to a Gaussian distribution with mean zero and standard deviation equal to its magnitude error. For more information, see Appendix B of Crenshaw et al. (2024).

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

============================
Observing Condition Degrader
============================

This degrader produces observed magnitude and magnitude errors for the truth sample, based on the input survey condition maps (Hang et al. 2024). The user provides a series of survey condition maps in ``HEALPix`` (Górski et al. 2005) format with specified 𝑁side, e.g. the 5𝜎 depth in each band. The galaxies in the truth sample will be assigned survey conditions corresponding to their ``HEALPix`` pixel, either based on their coordinates in the original catalog, or randomly if only photometry is available (e.g., generated from the engines). In the latter case, a weight map can be specified to adjust the number of galaxies assigned to each pixel. A key input for ``ObservingConditionDegrader`` is ``map_dict``. This is a dictionary containing keys with the same names as parameters for LSSTErrorModel. Under each key, one can pass a series of paths for the survey condition maps for each band, or, if any quantity is held constant throughout the footprint, one can also pass a float number. The degrader then calls PhotErr to compute noisy magnitudes for each galaxy in each ``HEALPix`` pixel. The output of this module is a table containing degraded magnitudes, magnitude errors, RA, Dec, and the ``HEALPix`` pixel index of each galaxy.

.. autoclass:: rail.astro_tools.ObsCondition
   :noindex:

=======================
Spectroscopic Degraders
=======================

``SpectroscopicDegraders`` contains two simple degraders that simulate systematic errors associated with the presence of spectroscopic redshifts in spectroscopic training catalogs.

The first is ``InvRedshiftIncompleteness``. It is a toy model for redshift incompleteness -- i.e., the failure of a particular spectrograph to obtain a redshift estimate for a particular set of galaxies. It takes an input catalog and keeps all the galaxies below a configurable redshift threshold while randomly removing galaxies above it. The probability that a redshift $z$ galaxy is kept is:

$p(z) = \mathrm{min}\left( 1, \frac{z_\mathrm{th}}{z} \right)$,

where $z_\mathrm{th}$ is the threshold redshift.

The other degrader is ``LineConfusion``, which simulates redshift errors due to the confusion of emission lines.
For example, if the OII line at $3727 \text{\AA}$ was misidentified as the OIII line at $5007 \text{\AA}$, the assigned spectroscopic redshift would be greater than the true redshift (Newman et al. 2013).
The inputs of this degrader are a `true' and `wrong' redshift, and an error rate.
The degrader then randomly simulates line confusion, ignoring galaxies for which the misidentification would result in a negative redshift (which can occur when the wrong wavelength is shorter than the true wavelength).

.. autoclass:: rail.astro_tools.LineConfusion
   :noindex:

.. autoclass:: rail.astro_tools.InvRedshiftIncompleteness
   :noindex:


===========
QuantityCut
===========

This degrader provides a trimmed version of the input catalog based on selection cuts applied to the catalog quantities. The user provides the parameter cuts, which is a dictionary with keys being the columns to which the selection is to be applied (e.g., the 𝑖-band magnitude), and the values being the specific cuts. Two types of values can be provided: a single float number (e.g., 25.3), which is interpreted as a maximum value (i.e., the cut will remove samples with 𝑖 > 25.3), and a tuple (e.g., (17, 25.3)), which is interpreted as a range within which the sample is selected (i.e., the selected sample has 17 < 𝑖 < 25.3). When multiple cuts are applied at the same time, only the intersection of selected samples of each cut will be kept in the output.

.. autoclass:: rail.creation.degraders.quantityCut.QuantityCut
   :noindex:

=======================
Spectroscopic Selectors
=======================

The ``SpectroscopicSelection`` degrader applies the selection for a spectroscopic survey. It provides tailored catalogs that match a particular spectroscopic survey for subsequent calibration steps. It can also be used to generate selected mock catalogs used as realistic reference samples. The selection criteria are cuts on magnitudes or colors adopted for the associated spectroscopic survey targeting. The current available selectors are for VVDSf02 (Le Fèvre et al. 2005), zCOSMOS (Lilly et al. 2009), GAMA (Driver et al. 2011), BOSS (Dawson et al. 2013), and DEEP2 (Newman et al. 2013). SpectroscopicSelection requires a 2-dimensional spectro- scopic redshift success rate as a function of two variables (often two of magnitude, color, or redshift), specific to the redshift survey for which selection is being emulated. The degrader will draw the appropriate fraction of samples from the input data and return an incomplete sample. Additional redshift cuts based on percentile can be applied when using a color-based redshift cut.

Similar functionality is provided by ``GridSelection`` (Moskowitz et al. 2024), which can be used to model spectroscopic success rates for the training sets used for the second data release of the Hyper Suprime Cam Subaru Strategic Program (HSC; Aihara et al. 2019). Given a 2-dimensional grid of spectroscopic success ratio as a function of two variables (often magnitude or color), the degrader will draw the appropriate fraction of samples from the input data and return incomplete sample. Additional redshift cuts can also be applied, where all redshifts above the cutoff are removed. In addition to the default HSC grid, RAIL accepts user-defined setting files for the success ratio grids appropriate for other surveys.

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

===============
SOMSpecSelector
===============


While ``GridSelection`` defines a selection mask in two dimensions, ``SOMSpecSelector`` can take any number of input features with which to define a spectroscopic selection. This selector takes an initial complete sample (which we will call the input sample) and return a subset that approximately matches the properties of an incomplete sample (we will refer to this as the specz sample). The selector operates by taking the list of features (which must be present in both the input and specz samples) and constructs a self-organizing map (SOM; Kohonen 1982) from the input data, creating a mapping from the higher-dimensional feature set to the 2D grid of SOM cells. It then finds the best cell assignment for each galaxy in both the input and specz samples. The selector builds a mask as it iterates over all cells, and for each cell returns a random subset of input objects that lie in that cell that equal in number to specz objects in the cell. If the cell has more specz objects than are available in the input catalog, then it returns all that are available. By matching the number of objects cell by cell the selector naturally mimics the features of the specz sample.


.. autoclass:: rail.creation.degraders.specz_som.SOMSpecSelector
   :noindex:


=================
Blending Degrader
=================


This degrader creates mock unrecognized blends based on source density. Unrecognized blends are sources overlapping too closely in projection and are detected as one object (referred to as `ambiguous blends' in Dawson et al. 2016). This degrader first searches for close objects that are likely to become unrecognized blends, then merges their fluxes to create one blended object. The source IDs of blend components are saved for references.

The blending components are found by matching the RA and Dec coordinates of an input catalog with itself via a Friends-of-Friends (FoF) algorithm (Mao et al. 2021). The advantage of the FoF algorithm is that it can produce unrecognized blends from multiple sources rather than just pairs. The algorithm groups sources such that within each group, every source is separated from at lease one another group member by an angular distance less than a specified `linking length'. By setting a small enough linking length (e.g., 1 arcsec), we assume that all group members will be blended into one detection. In the future, we might implement options for a more sophisticated identification of blends using source sizes and shapes. In the current release, this degrader simply sums up fluxes over all group members to create one blended object per group. Note that we do not currently simulate the impact on aperture photometry due to irregular profiles of blends either, but are motivated to conduct such a study in the future.

Note that the truth redshifts of blended objects are ambiguous since they are composed of multiple objects. We provide several summary columns for the truth: ``z_brightest`` is the redshift of the brightest component; ``z_mean`` is the average redshift of all components; and ``z_weighted`` is the flux-weighted average redshift. For blended objects composed of more than (including) two components, the standard deviation of redshifts is provided. The decision on the truth redshift is left to the users. For more complicated truth estimation -- e.g., considering the colors of components, as bluer galaxies tend to have strong emission lines which are often used to infer redshifts from spectroscopy -- users have the option to trace the components with source IDs. The tutorial ``blending_degrader_demo`` illustrates how to match the output catalog with the source IDs and the input catalog to access more information.

The order of application is particularly important for this degrader. Generally, this degrader should be applied before any selections on the truth catalog, including any magnitude, color, or signal-to-noise ratio cuts. The reason is that bright sources can blend with fainter ones, and two faint sources might blend into a brighter object that enters the target depth selection. For example, a magnitude difference of $\sim2.5$ translates roughly into a flux contamination of 10%. However, applying this degrader to the original truth catalog without any cuts can be a computational burden, because the truth catalog is often much larger than the target-depth catalog. To mitigate this issue, one can use a magnitude cut to decrease the target depth by {an arbitrary threshold (e.g., 2 or 3 magnitudes)} before running this degrader. 

While preliminary studies have addressed some aspects of blending on photo-z  (e.g., Nourbakhsh et al. 2022), a thorough quantitative exploration of this topic will be important to develop a deeper understanding of the issue and its impacts on various science cases.


.. autoclass:: rail.creation.degraders.unrec_bl_model.UnrecBlModel
   :noindex:
