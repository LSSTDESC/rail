This directory contains an example notebook showing a simplified version of the end-to-end functionality of RAIL.

- [goldenspike.ipynb](https://lsstdescrail.readthedocs.io/en/latest/source/other-notebooks.html#goldenspike-an-example-of-an-end-to-end-analysis-using-rail) is a notebook that chains together the functionality of the creation, estimation, and evaluation modules.

- `goldenspike.yml`, a pipeline file (plus `goldenspike_config.yml`, its associated config file).

To run the pipeline file from the command line, you must:
- Make sure you have [ceci](https://github.com/LSSTDESC/ceci) installed (run `pip install ceci`)
- Point your shell to the root of your RAIL directory
- Run `ceci examples/goldenspike_examples/goldenspike.yml`