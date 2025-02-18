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
