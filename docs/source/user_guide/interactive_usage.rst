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

To see the interactive mode API reference, visit the :ref:`page-interactive-api` page.

To learn how to run RAIL in pipeline mode, visit the :ref:`pipeline usage` page.

.. note::
    When using the interactive module in certain code editors, tab completion may
    suggest that functions and submodules are present which cannot actually be used.

    If you encounter a function which you would like to run, but find yourself unable,
    use the information in the docstring to identify which RAIL package defines the
    related RailStage, and install it.

============================
Finding your way around RAIL
============================

The below table shows the large-scale structure of the RAIL package.

These hierarchical namespaces used to organize objects and algorithms. A namespace
package's modules and content belong to the same section of functionality, and serve the
same purpose. For example, the ``estimation.algos`` namespace contains modules of
different estimation algorithms.


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


The interactive module mirrors the same import structure as Pipeline Mode RAIL, but with
'interactive' inserted into the path. Thus a RailStage typically imported from
``rail.estimation.algos.random_gauss`` will have an interactive function defined in
``rail.interactive.estimation.algos.random_gauss``.

========
Cookbook
========

.. cookbook section, many will be pointers to notebooks, roadmap for own page if it becomes large

This cookbook contains tutorials for a variety of interactive mode RAIL use
cases.