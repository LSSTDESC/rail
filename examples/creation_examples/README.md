This directory contains example notebooks explaining how to use the RAIL Creation Module.

- [degradation-demo.ipynb](https://htmlpreview.github.io/?https://github.com/LSSTDESC/RAIL/blob/master/examples/creation/degradation-demo.html) explains how to construct a basic `Engine`, draw samples, and use Degraders to degrade the samples in various ways.

- **dsps_sed_demo.ipynb** demonstrates some basic usage of the DSPS library.

- [example_GridSelection_for_HSC.ipynb](https://lsstdescrail.readthedocs.io/en/latest/source/creation-notebooks.html#grid-selection-degrader-to-emulate-hsc-training-samples) creates a grid of mock galaxies and plots the success rate to visualize the spectroscopic success rate for HSC.

- **example_ObsConditions.ipynb** generates the photometric error using the Rubin Observatory Metrics Analysis Framework (MAF).

- [example_SpecSelection_for_zCOSMOS](https://lsstdescrail.readthedocs.io/en/latest/source/creation-notebooks.html#spectroscopic-selection-degrader-to-emulate-zcosmos-training-samples) teaches how to select galaxies based on zCOSMOS selection function.

- **photometric_realization_demo.ipynb** demonstrates how to do photometric realization from different magnitude error models. (For a more completed degrader demo, see `degradation-demo.ipynb`.)

- [posterior-demo.ipynb](https://htmlpreview.github.io/?https://github.com/LSSTDESC/RAIL/blob/master/examples/creation/posterior-demo.html) explains how to use the `Engine` to calculate posteriors for galaxies in the sample, including complex examples of calculating posteriors for galaxies with photometric errors and non-detections.
