*******************************
Configuring RAIL for input data
*******************************

====================================
Variation in input catalog structure
====================================

`RAIL` is designed to be used with a variety of different data.
Depending on the data in question, things like the names of the
columns associted to the particular quantities like the true redshift
of a simulated object, or the names of the columns with the various
observed magnitudes in different filters, will vary.  By enforcing
consistency in naming conventions between different `RailStage`
sub-classes we have made it simple configure `RAIL` to read data from
a particular source, rather than having to edit the configurations
for many different `RailStages`.

When using a single stage (e.g. testing an algorithm in a Jupyter notebook), 
it is also possible to overwrite the default settings for the input data. 
In the `make_stage` step, simply specify catalog information. An simple example is 
changing the band names of the input catalog from the default values to Gaap magnitudes, in `MyFavouriteEstimator`. This can be done by simply setting `MyFavouriteEstimator.make_stage(band = [f"{band}_gaap1p0Mag" for band in "ugrizy"])`. Note that typically a stage may require changes in multiple input parameters (e.g. `err_bands` and `ref_bands` needs to be changed accordingly.

=================
Shared Parameters
=================

.. autoclass:: rail.core.common_params.SharedParams
   :members:
   :undoc-members:
   :show-inheritance:


============
Catalog Tags
============

:py:class:`rail.util.catalog_utils.CatalogConfigBase` provides an
interface to switch between different input catalogs.

.. autoclass:: rail.utils.catalog_utils.CatalogConfigBase
    :noindex:

.. automethod:: rail.utils.catalog_utils.CatalogConfigBase.apply
    :noindex:
       
.. automethod:: rail.utils.catalog_utils.CatalogConfigBase.active_class
    :noindex:

.. automethod:: rail.utils.catalog_utils.CatalogConfigBase.active_tag
    :noindex:
