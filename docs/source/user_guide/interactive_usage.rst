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

To see the interactive mode API reference, visit the :ref:`Interactive API <page-interactive-api>`.

To learn how to run RAIL in pipeline mode, visit :ref:`pipeline usage`.

.. note::
    When using the interactive module in certain code editors, tab completion may
    suggest that functions and submodules are present which cannot actually be used.

    If you encounter a function which you would like to run, but find yourself unable,
    use the information in the docstring to identify which RAIL package defines the
    related ``RailStage``, and install it.

============================
Finding your way around RAIL
============================

The below table shows the large-scale structure of the RAIL package.

These hierarchical namespaces used to organize objects and algorithms. A namespace
package's modules and content belong to the same section of functionality, and serve the
same purpose. For example, the ``estimation.algos`` namespace contains modules of
different estimation algorithms.


+---------------------------------+-------------------------------------------------------------------------+
| Namespace                       | Description                                                             |
+=================================+=========================================================================+
| :py:mod:`creation`              | create and degrade synthetic photometric data                           |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`creation.engines`      | algorithms to generate synthetic photometric data                       |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`creation.degraders`    | algorithms to apply degradations to synthetic photometric data          |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`estimation`            | derive redshift information from photometric data                       |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`estimation.algos`      | algorithms to estimate per-galaxy photo-z PDFs                          |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`evaluation`            | evaluate photo-z estimator performance                                  |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`evaluation.metrics`    | metrics for evaluation of redshift estimation                           |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`utils`                 | utility functions, e.g. catalog, testing                                |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`tools`                 | utility stages, e.g. photometry, tables                                 |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`pipelines`             | create 'mini runner' pipelines                                          |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`pipelines.degradation` | pre-defined degradation pipelines                                       |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`pipelines.estimation`  | pre-defined estimation pipelines                                        |
+---------------------------------+-------------------------------------------------------------------------+
| :py:mod:`cli`                   | utility functions for the command line                                  |
+---------------------------------+-------------------------------------------------------------------------+


The interactive module mirrors the same import structure as Pipeline Mode RAIL, but with
'interactive' inserted into the path. Thus a ``RailStage`` typically imported from
:py:mod:`rail.estimation.algos.random_gauss`` will have an interactive function defined in
:py:func:`rail.interactive.estimation.algos.random_gauss`.

========
Cookbook
========

.. cookbook section, many will be pointers to notebooks, roadmap for own page if it becomes large

This cookbook contains tutorials for a variety of interactive mode RAIL use
cases.


--------------------------------------------
Running a RAIL algorithm in interactive mode
--------------------------------------------

To run a RAIL stage in interactive mode, you run the corresponding interactive function.
Here's an example of running the *inform* stage of the 
`K-Nearest Neighbours <https://rail-hub.readthedocs.io/en/latest/source/rail_stages/estimation.html#k-nearest-neighbor>`_ 
estimation algorithm. First we use ``find_rail_file`` and `tables_io <https://tables-io.readthedocs.io/en/latest/index.html>`_ 
to read in the input data file we need:

>>> import rail.interactive as ri #import all rail interactive functions
>>> import tables_io #for reading and writing data 
>>> from rail.utils.path_utils import find_rail_file #for getting our training data 
>>> training_data_file = find_rail_file("examples_data/testdata/test_dc2_training_9816.hdf5")
>>> training_data = tables_io.read(calibration_data_file) #read in training data file 

Then we can just run the ``k_near_neigh_informer`` function, giving it the required ``training_data`` argument
(we've not included the output from the actual function running since it's a bit long). We'll take 
a look at the output it returns:

>>> knn_model = ri.estimation.algos.k_nearneigh.k_near_neigh_informer(training_data=training_data)
>>> print(knn_model) #output is returned as a dictionary
{'model': {'kdtree': <sklearn.neighbors._kd_tree.KDTree object at 0x5d6fbc75d130>, 
    'bestsig': np.float64(0.023333333333333334), 'nneigh': 7, 
    'truezs': array([0.02043499, 0.01936132, 0.03672067, ..., 2.97927326, 2.98694714,
    2.97646626], shape=(10225,)), 'only_colors': False}}

In general, these functions return outputs as a dictionary, with the relevant data tables or objects as 
values in the dictionary. 

.. tip::

    If you'd like a more detailed example of using RAIL interactive functions, take a look at the 
    `introduction to RAIL interactive notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/interactive_examples/rendered/core_examples/Estimating_Redshifts_and_Comparing_Results_for_Different_Parameters.html>`_


----------------------------------------
Running RAIL with different column names
----------------------------------------

RAIL stages typically expect a certain default set of column names for photometry and error columns. 
These are just supplied by default arguments to some common configuration parameters, and can be easily 
overridden by providing your own arguments to those parameters to tell the code to expect the columns 
that your data has. Depending on the stage, you may only need some of these values, but often supplying 
all of these values to every stage will not provide issues, as additional unnecessary arguments are just 
ignored. 

For example, if you are using a data table that is a pandas DataFrame with the following column names: 
``["u", "g", "r", "i", "z", "y", "J", "H"]``, then you need to provide the following parameters as 
shown in the example below.

* ``hdf5_groupname``
* ``bands``
* ``err_bands``
* ``mag_limits``
* ``ref_band``

First we set up the ``bands``, ``err_bands``, and ``mag_limits`` parameters, which all rely on each other:

>>> bands = ["u", "g", "r", "i", "z", "y", "J", "H"] #the column names of our photometry bands
>>> errbands = [] 
>>> maglims = {}
>>> limvals = [27.8, 29.0, 29.1, 28.6, 28.0, 27.0, 26.4, 26.4] #magnitude limits for the bands
>>> for band, limval in zip(bands, limvals): #populate the empty errbands and maglims 
>>>     errbands.append(f"{band}_err")
>>>     maglims[band] = limval
>>> print(bands)
>>> print(errbands)
>>> print(maglims)
['u', 'g', 'r', 'i', 'z', 'y', 'J', 'H']
['u_err', 'g_err', 'r_err', 'i_err', 'z_err', 'y_err', 'J_err', 'H_err']
{'u': 27.8, 'g': 29.0, 'r': 29.1, 'i': 28.6, 'z': 28.0, 'y': 27.0, 'J': 26.4, 'H': 26.4}

Now that we have these set up, we can put them into a dictionary with the other two parameters we need.
``hdf5_groupname`` tells the code what key it needs to access the data table from a dictionary, or if there is 
no key needed, just give it an empty string. The ``ref_band`` parameter identifies one of the photometry bands 
to use as a reference, so you just need to provide it with the column name of that band:

>>> columns_dict = dict(hdf5_groupname="", bands=bands, err_bands=errbands, 
>>>                     mag_limits=maglims, ref_band="i")
{'hdf5_groupname': '', 'bands': ['u', 'g', 'r', 'i', 'z', 'y', 'J', 'H'], 
    'err_bands': ['u_err', 'g_err', 'r_err', 'i_err', 'z_err', 'y_err', 'J_err', 'H_err'], 
    'mag_limits': {'u': 27.8, 'g': 29.0, 'r': 29.1, 'i': 28.6, 'z': 28.0, 'y': 27.0, 'J': 26.4, 
    'H': 26.4}, 'ref_band': 'i'}

Now we can pass this dictionary into any of the RAIL stages, along with any of the required parameters. 
Here we're assuming that we have a data table with the column names in ``columns_dict`` called ``training_data``:

>>> ri.estimation.algos.k_nearneigh.k_near_neigh_informer(training_data=training_data, **columns_dict)

The function should run as normal, and return to you any output with the same column names as what you input. 

.. tip::

    Take a look at the `Running with different data notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/interactive_examples/latest/rendered/estimation_examples/16_Running_with_different_data.html>`_ 
    for a bit more detailed example of this.


----------------
Renaming columns 
----------------

RAIL also has a utility for renaming the columns in your table, which you could use to make 
your column names match the expected versions, for example:

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

You can then use this dictionary to rename the columns in your pandas DataFrame:

>>> train_data_pq = ri.tools.table_tools.column_mapper(data=train_data["output"], columns=rename_dict)
>>> print(train_data_pq["output"].columns)
Index(['mag_u_lsst', 'mag_g_lsst', 'mag_r_lsst', 'mag_i_lsst', 'mag_z_lsst',
       'mag_y_lsst', 'mag_J_lsst', 'mag_H_lsst'],
      dtype='object')

.. tip::

    Check out the `introduction to RAIL interactive notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/interactive_examples/rendered/core_examples/Estimating_Redshifts_and_Comparing_Results_for_Different_Parameters.html>`_ 
    to see this RAIL utility being used in an example RAIL workflow. 


----------------------------------
Converting tables to other formats 
----------------------------------

RAIL has a stage that converts tabular RAIL data to different formats. This will 
not work on data in Ensemble format, or on models. The formats are those supported 
by `tables_io`, and you can see the `supported tabular formats <https://tables-io.readthedocs.io/en/latest/quickstart.html#supported-tabular-formats>`_ 
table for a list of the options. Just provide the "Tabular format name" to the 
function as shown here:

>>> train_data = ri.tools.table_tools.table_converter(data=train_data_pq["output"], 
>>>              output_format="numpyDict")
>>> type(train_data["output"])
collections.OrderedDict

In this case, "numpyDict" refers to an OrderedDict of numpy arrays, and we can see here 
that the data has in fact been converted to that format. 

.. tip::

    Check out the `Goldenspike notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/interactive_examples/rendered/goldenspike_examples/Goldenspike.html>`_ 
    to see this RAIL utility used in an example workflow. 

------------------------------------
Saving the outputs of stages to file 
------------------------------------

Inform stages typically output 'models', which can be different kinds of objects depending on 
the algorithm. If you want to save these to a file to speed up later workflows, 
we recommend pickling them. For example: 

>>> import pickle
>>> with open("./knn_model.pkl", "wb") as fout:
>>>    pickle.dump(obj=knn_inform["model"], file=fout, protocol=pickle.HIGHEST_PROTOCOL)

You can then provide the name of the file to the interactive functions.

.. tip::

    Take a look at the `Using Photometry to Estimate Photmetric Redshifts notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/interactive_examples/rendered/estimation_examples/Using_Photometry_to_Estimate_Photometric_Redshifts.html>`_ 
    to see more details and how saving a model file can be useful in a RAIL workflow.

Most estimate stages output qp Ensembles, which have their own write and read methods. 
The following will write an Ensemble to an HDF5 file:

>>> import qp
>>> estimate_output["output"].write_to("output_ensemble.hdf5")

To read the Ensemble back in, you can also use qp:

>>> import qp
>>> estimate_ens = qp.read("output_ensemble.hdf5")
>>> estimate_ens
Ensemble(the_class=hist,shape=(2, 50))

.. tip::

    Take a look at the `Using Photometry to Estimate Photmetric Redshifts notebook <https://rail-hub.readthedocs.io/projects/rail-notebooks/en/latest/interactive_examples/rendered/estimation_examples/Using_Photometry_to_Estimate_Photometric_Redshifts.html>`_ 
    for an introduction to Ensembles in RAIL and to see them being saved in a RAIL workflow. 

    For more details about how qp stores Ensembles in files, take a look at the notebook 
    on `Exploring the structure of an Ensemble file <https://qp.readthedocs.io/en/main/user_guide/cookbook/datamanipulation.html#exploring-the-structure-of-an-ensemble-file>`_


.. note::

    If you have any examples that you think should be added to this list, you can open an `issue <https://github.com/LSSTDESC/rail/issues/new/choose>`_ 
    in RAIL, or if you are a part of the LSST Slack, send a message in the `\#desc-pz-rail
    <https://lsstc.slack.com/archives/CQGKM0WKD>`_ Slack channel! 
