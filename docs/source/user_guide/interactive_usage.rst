*****************
Interactive Usage
*****************

.. introduction of what interactive is, note that it's a front end to functionality, when you should or shouldn't use, link to notebooks

This page details the usage of RAIL in interactive mode. RAIL can be run
interactively, such as in a Jupyter notebook. This interactive mode provides a
user-friendly front-end to RAIL functionality. It is the recommended mode of
usage for:

* exploring the functionality, stages, and objects of RAIL
* developing new workflows and pipelines
* operating on smaller data sets
* integrating other code bases

To see examples of how to use RAIL in interactive mode, visit the
:ref:`interactive mode notebooks` page.

To see the interactive mode API reference, visit the :ref:`interactive api` page.

To learn how to run RAIL in pipeline mode, visit the :ref:`pipeline usage` page.

===============
RAIL Namespaces
===============

.. namespace explanation in a table, copy and paste in different places

A RAIL namespace is a subpackage of the RAIL package, used to organize objects
and algorithms. A namespace package's modules and content belong to the same
section of functionality, and serve the same purpose. For example, the
``estimation.algos`` namespace contains modules of different estimation
algorithms. The following namespaces are in RAIL.

.. table
.. TODO: rail_calib package

+-----------------------+----------------------------------------------------------------+
| Namespace             | Description                                                    |
+=======================+================================================================+
| creation              | create and degrade synthetic photometric data                  |
+-----------------------+----------------------------------------------------------------+
| creation.engines      | algorithms to generate synthetic photometric data              |
+-----------------------+----------------------------------------------------------------+
| creation.degraders    | algorithms to apply degradations to synthetic photometric data |
+-----------------------+----------------------------------------------------------------+
| estimation            | derive redshift information from photometric data              |
+-----------------------+----------------------------------------------------------------+
| estimation.algos      | algorithms to estimate per-galaxy photo-z PDFs                 |
+-----------------------+----------------------------------------------------------------+
| evaluation            | evaluate photo-z estimator performance                         |
+-----------------------+----------------------------------------------------------------+
| evaluation.metrics    | metrics for evaluation of redshift estimation                  |
+-----------------------+----------------------------------------------------------------+
| utils                 | utility functions, e.g. catalog, testing                       |
+-----------------------+----------------------------------------------------------------+
| tools                 | utility stages, e.g. photometry, tables                        |
+-----------------------+----------------------------------------------------------------+
| pipelines             | create 'mini runner' pipelines                                 |
+-----------------------+----------------------------------------------------------------+
| pipelines.degradation | pre-defined degradation pipelines                              |
+-----------------------+----------------------------------------------------------------+
| pipelines.estimation  | pre-defined estimation pipelines                               |
+-----------------------+----------------------------------------------------------------+
| cli                   | utility functions for the command line                         |
+-----------------------+----------------------------------------------------------------+

For the API documentation, refer to the :ref:`namespaces` page.

========
Cookbook
========

.. cookbook section, many will be pointers to notebooks, roadmap for own page if it becomes large

This cookbook contains tutorials for a variety of interactive mode RAIL use
cases.