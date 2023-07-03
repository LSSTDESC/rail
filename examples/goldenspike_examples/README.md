This directory contains an example notebook showing a simplified version of the end-to-end functionality of RAIL.

- [goldenspike.ipynb](https://lsstdescrail.readthedocs.io/en/latest/source/other-notebooks.html#goldenspike-an-example-of-an-end-to-end-analysis-using-rail) is a notebook that chains together the functionality of the creation, estimation, and evaluation modules.

- `goldenspike.yml`, a pipeline file (plus `goldenspike_config.yml`, its associated config file).

---
 
  To run the pipeline file from the command line, you must:
 - `cd` to your `rail/` directory
 - `rail get-data` to download any required data from NERSC
 - `ceci examples/goldenspike_examples/goldenspike.yml` to run the pipeline
