This directory contains example notebooks explaining how to use the RAIL Creation Module.

- [00_Quick_Start_in_Creation.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/00_Quick_Start_in_Creation.html) explains how to construct a basic `Engine`, draw samples, and use Degraders to degrade the samples in various ways.

- [01_Photometric_Realization.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/01_Photometric_Realization.html) demonstrates how to do photometric realization from different magnitude error models. (For a more completed degrader demo, see `00_Quick_Start_in_Creation.ipynb`.)

- [02_Photometric_Realization_with_Other_Surveys.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/02_Photometric_Realization_with_Other_Surveys.html) demonstrates the use of photometric error models created for various surveys.

- [03_GridSelection_for_HSC.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/03_GridSelection_for_HSC.html) creates a grid of mock galaxies and plots the success rate to visualize the spectroscopic success rate for HSC.

- **04_Plotting_interface_skysim_cosmoDC2_COSMOS2020.ipynb** demonstrates plotting with the cosmoDC2 and skysim catalogs.

- [05_True_Posterior.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/05_True_Posterior.html) explains how to use the `Engine` to calculate posteriors for galaxies in the sample, including complex examples of calculating posteriors for galaxies with photometric errors and non-detections.

- [06_Blending_Degrader.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/06_Blending_Degrader.html) demonstrates the use of the ``unrec_bl_model`` degrader, which uses Friends of Friends to find sources that are close together and merges them into unrecognized blends.

- **07_DSPS_SED.ipynb** demonstrates some basic usage of the DSPS library.

- **07_FSPS_SED.ipynb** demonstrates some basic usage of the FSPS library.

- [09_Spatial_Variability.ipynb](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/09_Spatial_Variability.html) generates the photometric error using the Rubin Observatory Metrics Analysis Framework (MAF).

- **10_SOM_Spectroscopic_Selector.ipynb** demonstrates some basic usage of the SOM-based spectroscopic degrader that is designed to make mock spectroscopic selections for a training set.

- [11_Spectroscopic_Selection_for_zCOSMOS](https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/rendered/creation_examples/11_Spectroscopic_Selection_for_zCOSMOS.html) teaches how to select galaxies based on zCOSMOS selection function.

