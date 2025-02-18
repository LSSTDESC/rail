***************************
Data Handles and Data Store
***************************

=============================
Potentially large data volume
=============================
       
===================
Parallel processing
===================

============
Data Handles
============

:py:class:`rail.core.DataHandle` is the class that lets users connect
data to RAIL stages.

.. autoclass:: rail.core.DataHandle
    :noindex:

=======================
DatHandle Functionality
=======================


.. automethod:: rail.core.DataHandle.open
    :noindex:

.. automethod:: rail.core.DataHandle.close		
    :noindex:

.. automethod:: rail.core.DataHandle.read
    :noindex:

.. automethod:: rail.core.DataHandle.write
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

.. automethod:: rail.core.DataHandle.data_size
    :noindex:

.. automethod:: rail.core.DataHandle.set_data
    :noindex:
       
.. automethod:: rail.core.DataHandle.make_name
    :noindex:



==========
Data Store
==========


:py:class:`rail.core.DataStore` is the class that lets users import
data into RAIL.

.. autoclass:: rail.core.DataStore
    :noindex:


=======================
DataStore Functionality
=======================

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
       
