===============================================
RAIL: Redshift Assessment Infrastructure Layers
===============================================

RAIL is a flexible open-source software library providing tools to produce at-scale
photometric redshift data products, including uncertainties and summary statistics, and
stress-test them under realistically complex systematics.


.. _cards-clickable: 

.. grid:: 2
    :gutter: 3
    :margin: 5 5 0 0
    :padding: 0

    .. grid-item-card::
        :link: source/start_here
        :link-type: doc 
        :link-alt: start-here
        :text-align: center 


        :fas:`fa-solid fa-bullseye; fa-5x`


        **Start Here**
        
        If it's your first time using RAIL, this is where to go for the basics.


    .. grid-item-card::
        :link: source/user_guide/what_is_rail
        :link-type: doc
        :link-alt: what-is-rail
        :text-align: center

        :fas:`fa-solid fa-circle-question; fa-5x`

        **User guide**

        The basics of how RAIL works and what you should know. 
     
    .. grid-item-card::
        :link: source/user_guide/interactive_usage
        :link-type: doc
        :link-alt: interactive-usage
        :text-align: center

        :fas:`fa-solid fa-keyboard; fa-5x`

        **Interactive Usage**

        How to interactively use RAIL on your own computer 

    .. grid-item-card::
        :link: source/user_guide/pipeline_usage
        :link-type: doc
        :link-alt: pipeline-usage
        :text-align: center

        :fas:`fa-solid fa-gears; fa-5x`

        **Pipeline Usage**

        How to build RAIL pipelines for use on larger computer systems 

    .. grid-item-card::
        :link: source/interactive_notebooks/index
        :link-type: doc
        :link-alt: interactive-notebooks
        :text-align: center

        :fas:`fa-solid fa-book; fa-5x`

        **Interactive Example Notebooks**

        Example Jupyter notebooks for using RAIL in interactive mode 

    .. grid-item-card::
        :link: source/pipeline_notebooks/index
        :link-type: doc
        :link-alt: pipeline-notebooks
        :text-align: center

        :fas:`fa-solid fa-book-atlas; fa-5x`

        **Pipeline Example Notebooks**

        Example Jupyter notebooks for using RAIL in pipeline mode 

RAIL serves as the infrastructure supporting many extragalactic applications of `the
Legacy Survey of Space and Time (LSST) <https://www.lsst.org/>`_ on `the Vera C. Rubin
Observatory <https://rubinobservatory.org/>`_, including Rubin-wide commissioning
activities. RAIL was initiated by the Photometric Redshifts (PZ) Working Group (WG) of
the `LSST Dark Energy Science Collaboration (DESC) <https://lsstdesc.org/>`_ as a result
of the lessons learned from the `Data Challenge 1 (DC1) experiment
<https://academic.oup.com/mnras/article/499/2/1587/5905416>`_ to enable the PZ WG
Deliverables in the `LSST-DESC Science Roadmap (see Sec. 5.18)
<https://lsstdesc.org/assets/pdf/docs/DESC_SRM_latest.pdf>`_, aiming to guide the
selection and implementation of redshift estimators in DESC analysis pipelines.

RAIL is developed and maintained by a diverse team comprising DESC Pipeline Scientists
(PSs), international in-kind contributors, LSST Interdisciplinary Collaboration for
Computing (LINCC) Frameworks software engineers, and other volunteers, but all are
welcome to join the team regardless of LSST data rights. To get involved, chime in on
the issues in any of the RAIL repositories described in the Overview section.


.. toctree::
   :hidden:
   :maxdepth: 4

   source/start_here

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: User Guide

   source/user_guide/what_is_rail
   source/user_guide/installation
   source/user_guide/interactive_usage
   source/user_guide/pipeline_usage
   source/user_guide/citations

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: RAIL Stages

   source/rail_stages/what_are_rail_stages
   source/rail_stages/creation
   source/rail_stages/estimation
   source/rail_stages/evaluation
   source/rail_stages/tools

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Interactive Mode Notebooks

   source/interactive_notebooks/index

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Pipeline Mode Notebooks

   source/pipeline_notebooks/index


.. toctree::
   :hidden:
   :maxdepth: 5
   :caption: API Documentation

   api_interactive
   api

.. toctree::
   :hidden:
   :maxdepth: 4
   :caption: Development

   source/development/contribute_to_rail
   source/development/contributor_concepts
   source/development/developer_installation
   source/development/style_guide
   source/development/add_stage
   source/development/documentation
