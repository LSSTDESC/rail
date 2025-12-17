.. _contributor-concepts:

********************
Contributor Concepts
********************

.. introduction

=============
Data Concepts
=============

.. introduction

------------
Data Handles
------------

.. format and check content

One particularity of `RAIL` is that we wrap data in
:py:class:`rail.core.DataHandle` objects rather than passing the data directly
to functions.  There are a few reasons for this.

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Potentially large data volume
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One of the challenges that `RAIL` must address is the potentially very large
datasets that we use.  At times we will be dealing with billions of objects, and
will not be able to load the object tables into the memory of a single
processor.

^^^^^^^^^^^^^^^^^^^
Parallel processing
^^^^^^^^^^^^^^^^^^^

.. section left blank by rail team

^^^^^^^^^^^^^^^^
DataHandle Class
^^^^^^^^^^^^^^^^

:py:class:`rail.core.DataHandle` is the class that lets users connect data to
RAIL.

.. autoclass:: rail.core.DataHandle
    :noindex:

^^^^^^^^^^^^^^^^^^^^^^^^^^
Basic file-like operations
^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.DataHandle.open
    :noindex:

.. automethod:: rail.core.DataHandle.close
    :noindex:

.. automethod:: rail.core.DataHandle.read
    :noindex:

.. automethod:: rail.core.DataHandle.write
    :noindex:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Operations for parallelized access to data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.DataHandle.iterator
    :noindex:

.. automethod:: rail.core.DataHandle.size
    :noindex:

.. automethod:: rail.core.DataHandle.data_size
    :noindex:

.. automethod:: rail.core.DataHandle.initialize_write
    :noindex:

.. automethod:: rail.core.DataHandle.write_chunk
    :noindex:

.. automethod:: rail.core.DataHandle.finalize_write
    :noindex:

.. automethod:: rail.core.DataHandle.iterator
    :noindex:

.. automethod:: rail.core.DataHandle.size
    :noindex:

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Functions for working with DataHandles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.DataHandle.set_data
    :noindex:

.. automethod:: rail.core.DataHandle.make_name
    :noindex:

---------------------
Ephemeral Data Stores
---------------------

.. format and check content

:py:class:`rail.core.DataStore` is the class that lets users import data into
RAIL.

.. autoclass:: rail.core.DataStore
    :noindex:

^^^^^^^^^^^^^^^^^^^^^^^
DataStore Functionality
^^^^^^^^^^^^^^^^^^^^^^^

.. automethod:: rail.core.DataStore.add_handle
    :noindex:

.. automethod:: rail.core.DataStore.read_file
    :noindex:

.. automethod:: rail.core.DataStore.read
    :noindex:

.. automethod:: rail.core.DataStore.open
    :noindex:

.. automethod:: rail.core.DataStore.write
    :noindex:

.. automethod:: rail.core.DataStore.write_all
    :noindex:

-----------------
Shared Parameters
-----------------

.. format and check content


`RAIL` is designed to be used with a variety of different data.  Depending on
the data in question, things like the names of the columns associated to the
particular quantities like the true redshift of a simulated object, or the names
of the columns with the various observed magnitudes in different filters, will
vary.  By enforcing consistency in naming conventions between different
`RailStage` sub-classes we have made it simple configure `RAIL` to read data
from a particular source, rather than having to edit the configurations for many
different `RailStages`.

When using a single stage (e.g. testing an algorithm in a Jupyter notebook), it
is also possible to overwrite the default settings for the input data directly
for the stage, without involving the shared parameters, by simply specifying
catalog information in the `make_stage` step. For example, your input catalog
may have band names like "{band}_gaap1p0Mag", which is different from the
default values in RAIL. To set this in `MyFavouriteInformer`, do
`MyFavouriteEstimator.make_stage(band = [f"{band}_gaap1p0Mag" for band in
"ugrizy"])`.  Note that typically a stage may require changes in multiple input
parameters (e.g. `err_bands` and `ref_bands` needs to be changed accordingly).
Note also that if the user wants to run `MyFavouriteEstimator` next, they will
need to repeat this for the `make_stage` for the estimator. This is why, in case
the user is running many stages, using shared parameters below are preferred.

.. autoclass:: rail.core.common_params.SharedParams
   :members:
   :undoc-members:
   :show-inheritance:

------------
Catalog Tags
------------

.. format and check content

:py:class:`rail.util.catalog_utils.CatalogConfigBase` provides an interface to
switch between different input catalogs.

.. autoclass:: rail.utils.catalog_utils.CatalogConfigBase
    :noindex:

.. automethod:: rail.utils.catalog_utils.CatalogConfigBase.apply
    :noindex:

.. automethod:: rail.utils.catalog_utils.CatalogConfigBase.active_class
    :noindex:

.. automethod:: rail.utils.catalog_utils.CatalogConfigBase.active_tag
    :noindex:

=================================
Developing the Interactive Module
=================================

.. introduction

------------------------------------
Connecting to the Interactive Module
------------------------------------

.. probably goes with algos/stages

-------
Testing
-------

.. developer tooling / pre-commit

