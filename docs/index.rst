===============================================
RAIL: Redshift Assessment Infrastructure Layers
===============================================

The LSST-DESC Redshift Assessment Infrastructure Layer (RAIL) code is a framework to perform photometric redshift (PZ) estimation and analysis for DESC.

RAIL's purpose is to be the infrastructure enabling the PZ working group deliverables in `the LSST-DESC Science Roadmap (see Sec. 4.14) <https://lsstdesc.org/assets/pdf/docs/DESC_SRM_latest.pdf>`_,
aiming to guide the selection and implementation of redshift estimators in DESC pipelines.
RAIL differs from previous plans for PZ pipeline infrastructure in that it is broken into stages,
each corresponding to a manageable unit of infrastructure advancement, a specific question to answer with that code, and a guaranteed publication opportunity.
RAIL uses `qp <https://github.com/LSSTDESC/qp>`_ as a back-end for handling univariate probability density functions (PDFs) such as photo-z posteriors or :math:`n(z)` samples.

The RAIL source code is publically available at https://github.com/LSSTDESC/RAIL.


.. toctree::
   :maxdepth: 1
   :caption: Getting Started

   source/overview
   source/installation
   source/citing

.. toctree::
   :maxdepth: 1
   :caption: Contributing

   source/contributing
   source/fix_an_issue
   source/new_rail_stage
   source/new_algorithm
   source/sharing_pipeline

.. toctree::
   :maxdepth: 1
   :caption: API

   api

.. toctree::
   :maxdepth: 1
   :caption: Usage Demos

   Core Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/core_notebooks.html>
   Creation Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/creation_notebooks.html>
   Estimation Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/estimation_notebooks.html>
   Evaluation Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/evaluation_notebooks.html>
   Goldenspike <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/goldenspike_notebook.html>
