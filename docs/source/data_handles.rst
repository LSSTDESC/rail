***************************
Data Handles and Data Store
***************************

One particularity of `RAIL` is that we wrap data in
:py:class:`rail.core.DataHandle` objects rather than
passing the data directly to functions.  There are a few
reasons for this.  
    
=============================
Potentially large data volume
=============================

One of the challenges that `RAIL` must address is the potentially
very large datasets that we use.  At times we will be dealing
with billions of objects, and will not be able to load the
object tables into the memory of a single processor.

===================
Parallel processing
===================



============
Data Handles
============

:py:class:`rail.core.DataHandle` is the class that lets users connect
data to RAIL.


.. autoclass:: rail.core.DataHandle
    :noindex:

=======================
DatHandle Functionality
=======================


Basic file-like operations
--------------------------


.. automethod:: rail.core.DataHandle.open
    :noindex:

.. automethod:: rail.core.DataHandle.close		
    :noindex:

.. automethod:: rail.core.DataHandle.read
    :noindex:

.. automethod:: rail.core.DataHandle.write
    :noindex:


Operations for parallized access to data
----------------------------------------

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

       
Functions for working with DataHandles 
---------------------------------------
       
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
       
