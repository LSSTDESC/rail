****************
Creation Engines
****************

Mock DESC data are important for systematically testing the performance of various photo-$z$ algorithms. 
One of the lessons learned from DC1 is that it is desirable for the mock data to include not only true redshifts and LSST photometry (i.e., fluxes in the six LSST bands) but also true posterior PDFs, $p(z_t | \mathbf{p}_t)$, which are unavailable for spectroscopically confirmed data sets as well as traditional simulations.
Furthermore, the mock photometry data should contain realistic noise, selection effects, and biases. This is critical for the training and validation of photo-$z$ algorithms.

To address these needs, :py:class:`rail.creation` enables us to create datasets with true PDFs that allow PDF-to-PDF metrics computations and forward-modeling of mock data for validating photo-$z$ approaches under realistically complex conditions. 
This is realized by two main types of stages within :py:class:`rail.creation`: (1) `engines` that forward-model photometric catalogs and (2) `degraders` that modify such catalogs to introduce tunable physical imperfections.


An engine is defined by a pair of stages that are subclasses of each of the following superclasses:
:py:class:`rail.creation.Modeler` makes a model of the $p(z, \mathrm{photometry})$ joint probability space based on input parameters or data, and :py:class:`rail.creation.Creator` samples $(z, \mathrm{photometry})$ from the forward model.

============================================
FSPS (Flexible Stellar Population Synthesis)
============================================

RAIL Package: https://github.com/LSSTDESC/rail_fsps

`FSPS` is a RAIL module that creates an interface to the `Python` bindings of the popular stellar population synthesis (SPS) code `FSPS` (Flexible Stellar Population Synthesis, Conroy et al. 2009, 2010). `FSPS` aims at generating realistic galaxy spectral energy distributions (SEDs) by modelling all the components that contribute to the light from a galaxy: stars, gas, dust and AGN. `FSPS` is widely used both for stellar population inference (Johnson et al. 2021) and for forward modelling of galaxy SEDs (e.g., Alsing et al. 2023, Tortorelli et al. 2024).

`FSPS` provides substantial flexibility in terms of the prescription for modelling each of the mentioned components. It also requires physical properties of galaxies as input, such as star formation histories (SFHs), metallicities and redshift, in order to generate their SEDs. We maintained this flexibility in the interface we implemented in `RAIL`, allowing the user to change every possible `FSPS` parameter. The code has been parallelized to make efficient use of the multiprocessing capabilities of CPUs.

The interface is integrated in the `RAIL` workflow, requiring as input a catalog of galaxy physical properties in the form of `Hdf5Handle`. These are galaxy redshifts, stellar metallicities, velocity dispersions, gas metallicities and ionization parameters (defined as the ratio of ionizing photons to the total hydrogen density), dust attenuation and emission parameters, and star-formation histories.

`FSPS` follows the structure of `engines`. The `Modeler` class requires galaxy physical properties as input and produces as output an `Hdf5Handle` that contains the `FSPS`-generated rest-frame SED for each galaxy and the common rest-frame wavelength grid. The user can choose the units of the output rest-frame SEDs by setting the appropriate keyword value. The default behavior is to output the SEDs in a wavelength grid.

The output rest-frame SEDs constitute the input for the `FSPS` `Creator` class. The latter computes apparent $\mathrm{AB}$ magnitudes for a set of user-defined waveband filters. Notice that the wavelength range spanned by the waveband filters should be within the SED observed-frame wavelength ranges. A default set of filters is implemented in :py:`rail.fsps`, containing the Rubin LSST filters among others.


.. autoclass:: rail.fsps.FSPSSedModeler
    :noindex:

.. autoclass:: rail.fsps.FSPSPhotometryCreator
    :noindex:

==================================================
DSPS (Differentiable Stellar Population Synthesis)
==================================================

RAIL Package: https://github.com/LSSTDESC/rail_dsps

`dsps` is a module that creates an interface in `RAIL` to the code `DSPS` (Differentiable Stellar Population Synthesis, Hearin et al. 2023). `DSPS` is implemented natively in the JAX library as its main aim is to produce differentiable predictions for the SED of a galaxy based on SPS. The implementation in JAX allows `DSPS` to be a factor of 5 faster than standard SPS codes, such as `FSPS`, and more than 300 times faster, if run on a modern GPU. `DSPS` does not come with stellar population templates; they must be provided by the user. The code contains a series of convenience functions that allow the user to generate stellar population templates with `FSPS`. If no templates are supplied, the implementation in `RAIL` automatically downloads a set of `FSPS`-generated stellar population templates.

The `Modeler` class of `dsps` requires as input a catalog of galaxy physical properties in the form of `Hdf5Handles`. In particular, the user provides, for each galaxy, a star-formation history, a grid of Universe age over which the stellar mass build-up takes place, and a value for the mean and scatter of the stellar metallicity distribution. The output is an `Hdf5Handle` that contains galaxy rest-frame SEDs, produced over the stellar population template wavelength grid.

The `Creator` class of `dsps` uses the output rest-frame SEDs to compute apparent and rest-frame AB magnitudes for a set of user-defined filters. Rubin-LSST filters are present in the default filter suite. The magnitudes are computed using the appropriate functions implemented in `DSPS` that, much like the SED generation, can take advantage of multiprocessing capabilities.

.. autoclass:: rail.dsps.DSPSSingleSedModeler
    :noindex:

.. autoclass:: rail.dsps.DSPSPopulationSedModeler
    :noindex:

.. autoclass:: rail.dsps.DSPSPhotometryCreator
    :noindex:

=============
PZFlow Engine
=============

RAIL Package: https://github.com/LSSTDESC/rail_pzflow

`PZFlow` is a generative model that simulates galaxy catalogs using normalizing flows.
Normalizing flows learn differentiable mappings between complex data distributions and a simple latent distribution, for example, a Normal distribution, hence the name *normalizing* flow.
In the creation module, a normalizing flow is trained to map the distribution of galaxy colors and redshifts onto a simple latent distribution.
New galaxy catalogs can then be simulated by sampling from the latent distribution and applying the inverse flow to the samples.
In addition, because the samples are generated by sampling from a distribution we have direct access to, there is a natural notion of a *true* redshift distribution for each galaxy in the catalog.
For more information, see Crenshaw et al. 2024. Note that `PZFlow` is also used to perform photo-$z$ estimation.

.. autoclass:: rail.pzflow.FlowModeler
    :noindex:

.. autoclass:: rail.pzflow.FlowPosterior
    :noindex:
