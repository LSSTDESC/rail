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
:ref:`interactive mode notebooks`.

To see the interactive mode API reference, visit the
:ref:`page-interactive-api<Interactve API>`.

To learn how to run RAIL in pipeline mode, visit :ref:`pipeline usage`.

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


--------------------------------------------
Running a RAIL algorithm in interactive mode
--------------------------------------------

>>> import rail.interactive as ri
>>> import tables_io
>>> from rail.utils.path_utils import find_rail_file
>>> training_data_file = find_rail_file("examples_data/testdata/test_dc2_training_9816.hdf5")
>>> training_data = tables_io.read(calibration_data_file)
>>> ri.estimation.algos.k_nearneigh.k_near_neigh_informer(training_data=training_data)


----------------------------------------
Running RAIL with different column names
----------------------------------------

RAIL stages typically expect a certain default set of column names for photometry and error columns. These are just supplied by 
default arguments to some common configuration parameters, and can be easily overridden by providing your own arguments to those 
parameters to tell the code to expect the columns that your data has. Depending on the stage, you may only need some of these values,
but often supplying all of these values to every stage will not provide issues, as additional unnecessary arguments are just ignored. 

For example, if you are using a data table that is a Pandas dataframe with the following column names: ``["u", "g", "r", "i", "z", "y", "J", "H"]``, 
then you need to provide the following parameters as shown in the example below.

* ``hdf5_groupname``
* ``bands``
* ``err_bands``
* ``mag_limits``
* ``ref_band``

First we set up the ``bands``, ``err_bands``, and ``mag_limits`` parameters, which all rely on each other:

>>> bands = ["u", "g", "r", "i", "z", "y", "J", "H"]
>>> errbands = []
>>> maglims = {}
>>> limvals = [27.8, 29.0, 29.1, 28.6, 28.0, 27.0, 26.4, 26.4]
>>> for band, limval in zip(bands, limvals):
>>>     errbands.append(f"{band}_err")
>>>     maglims[band] = limval
>>> print(bands)
>>> print(errbands)
>>> print(maglims)
['u', 'g', 'r', 'i', 'z', 'y', 'J', 'H']
['u_err', 'g_err', 'r_err', 'i_err', 'z_err', 'y_err', 'J_err', 'H_err']
{'u': 27.8, 'g': 29.0, 'r': 29.1, 'i': 28.6, 'z': 28.0, 'y': 27.0, 'J': 26.4, 'H': 26.4}

Now that we have these set up, we can put them into a dictionary with the other two parameters we need:

>>> columns_dict = dict(hdf5_groupname="", bands=bands, err_bands=errbands, 
>>>                     mag_limits=maglims, ref_band="i")
{'hdf5_groupname': '', 'bands': ['u', 'g', 'r', 'i', 'z', 'y', 'J', 'H'], 
'err_bands': ['u_err', 'g_err', 'r_err', 'i_err', 'z_err', 'y_err', 'J_err', 'H_err'], 
'mag_limits': {'u': 27.8, 'g': 29.0, 'r': 29.1, 'i': 28.6, 'z': 28.0, 'y': 27.0, 'J': 26.4, 'H': 26.4}, 
'ref_band': 'i'}

Now we can pass this dictionary into any of the RAIL stages (using ``**columns_dict`` as the last argument), and it should allow you to run the stage without issue. 


----------------
Renaming columns 
----------------

RAIL also has a utility for renaming the columns in your table, which you could use to make your column names match the expected versions, for example:

>>> rename_dict = {band: f"mag_{band}_lsst" for band in bands}
>>> print(rename_dict)
{'u': 'mag_u_lsst',
 'g': 'mag_g_lsst',
 'r': 'mag_r_lsst',
 'i': 'mag_i_lsst',
 'z': 'mag_z_lsst',
 'y': 'mag_y_lsst',
 'J': 'mag_J_lsst',
 'H': 'mag_H_lsst'}

You can then use this dictionary to rename the columns in your Pandas dataframe or Parquet file:
>>> train_data_pq = ri.tools.table_tools.column_mapper(data=train_data_cut["output"], columns=rename_dict)
>>> print(train_data_pq["output"].columns)
Index(['mag_u_lsst', 'mag_g_lsst', 'mag_r_lsst', 'mag_i_lsst', 'mag_z_lsst',
       'mag_y_lsst', 'mag_J_lsst', 'mag_H_lsst'],
      dtype='object')


----------------------------------
Converting tables to other formats 
----------------------------------

>>> train_data = ri.tools.table_tools.table_converter(data=train_data_pq["output"], output_format="numpyDict")
>>> type(train_data["output"])
collections.OrderedDict


------------------------------------
Saving the outputs of stages to file 
------------------------------------

Inform stages typically output 'models', which can be different kinds of objects depending on the algorithm. If you want to save these to a file to speed up later workflows, 
we recommend pickling them. For example: 

>>> import pickle
>>> with open("./knn_model.pkl", "wb") as fout:
>>>    pickle.dump(obj=knn_inform["model"], file=fout, protocol=pickle.HIGHEST_PROTOCOL)

Most estimate stages output qp `Ensembles`, which have their own write and read methods:

>>> import qp
>>> ens = qp.hist.create_ensemble()
>>> ens.write_to("output_ensemble.hdf5")