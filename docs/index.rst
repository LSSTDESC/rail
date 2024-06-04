===============================================
RAIL: Redshift Assessment Infrastructure Layers
===============================================

RAIL is a flexible open-source software library providing tools to produce at-scale photometric redshift data products, including uncertainties and summary statistics, and stress-test them under realistically complex systematics.

RAIL serves as the infrastructure supporting many extragalactic applications of `the Legacy Survey of Space and Time (LSST) <https://www.lsst.org/>`_ on `the Vera C. Rubin Observatory <https://rubinobservatory.org/>`_, including Rubin-wide commissioning activities. 
RAIL was initiated by the Photometric Redshifts (PZ) Working Group (WG) of the `LSST Dark Energy Science Collaboration (DESC) <https://lsstdesc.org/>`_ as a result of the lessons learned from the `Data Challenge 1 (DC1) experiment <https://academic.oup.com/mnras/article/499/2/1587/5905416>`_ to enable the PZ WG Deliverables in the `LSST-DESC Science Roadmap (see Sec. 5.18) <https://lsstdesc.org/assets/pdf/docs/DESC_SRM_latest.pdf>`_, aiming to guide the selection and implementation of redshift estimators in DESC analysis pipelines.

RAIL is developed and maintained by a diverse team comprising DESC Pipeline Scientists (PSs), international in-kind contributors, LSST Interdisciplinary Collaboration for Computing (LINCC) Frameworks software engineers, and other volunteers, but all are welcome to join the team regardless of LSST data rights. 
To get involved, chime in on the issues in any of the RAIL repositories described in the Overview section.


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

   Overview of Demonstrations <source/demonstrations>
   Core Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/core_notebooks.html>
   Creation Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/creation_notebooks.html>
   Estimation Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/estimation_notebooks.html>
   Evaluation Notebooks <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/evaluation_notebooks.html>
   Goldenspike <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/goldenspike_notebook.html>
