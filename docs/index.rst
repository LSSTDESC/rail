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
   source/contributing
   source/citing

.. toctree::
   :maxdepth: 1
   :caption: RAIL Plans

   source/immediateplans
   source/futureplans
   
.. toctree::
   :maxdepth: 1
   :caption: Usage Demos

   demos

.. toctree::
   :maxdepth: 1
   :caption: API

   api
