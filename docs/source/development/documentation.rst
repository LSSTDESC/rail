***************************
Contribute to documentation
***************************

All of the documentation on this site is built as part of the `RAIL Package
<https://github.com/lsstdesc/rail>`_, and the configuration and skeleton for the
documentation live in the ``rail/docs`` directory.

The documentation skeleton is set up to work with whatever RAIL packages are
installed, e.g., if you are just working on one of the algorithms, you can just
install that algorithm in addition to ``rail_base`` and ``rail`` and when you
generate the docs you will just get the docs for ``rail_base`` and that package.

The documentation uses `sphinx <https://www.sphinx-doc.org/en/master/>`_ to
automatically generate some content from the source code, this requires being
very careful with docstring formatting.

The documentation tools are configured to use the `numpy docstring style
<https://numpydoc.readthedocs.io/en/latest/format.html>`_

The documentation uses ``RAIL`` introspection tooling to find all the ``RAIL`` code
in your current python environment.  :py:mod:`rail.core.introspection`.

=======================================
Building the RAIL documentation locally
=======================================

Once you have installed ``rail``` from source you can build all the documentation
locally very easily. Note that this will also build the documentation for any
and all installed ``rail_algorithms`` packages.

You may have to install the documentation requirements in RAIL first by running 
the following in the ``rail`` directory:

.. code-block:: bash

    pip install .[docs]

To make the documentation, run the following:

.. code-block:: bash

    cd rail/docs 
    make html

This will generate the documentation tree in ``rail/docs/_build/html``.

You can then point a browser at the local file, e.g.,
``rail/docs/_build/html/index.html`` to explore the documentation.

========================
RAIL Introspection tools
========================

The ``RailEnv`` class provides tools to discover and organize all the available
RAIL code.

.. autoclass:: rail.core.RailEnv
    :noindex:

----------------------------------------
Functions to set up the RAIL environment
----------------------------------------

.. automethod:: rail.core.RailEnv.import_all_packages
    :noindex:

.. automethod:: rail.core.RailEnv.attach_stages
    :noindex:

-----------------------------------------
Functions to explore the RAIL environment
-----------------------------------------

.. automethod:: rail.core.RailEnv.list_rail_packages
    :noindex:

.. automethod:: rail.core.RailEnv.print_rail_packages
    :noindex:

.. automethod:: rail.core.RailEnv.list_rail_namespaces
    :noindex:

.. automethod:: rail.core.RailEnv.print_rail_namespaces
    :noindex:

.. automethod:: rail.core.RailEnv.list_rail_modules
    :noindex:

.. automethod:: rail.core.RailEnv.print_rail_modules
    :noindex:

.. automethod:: rail.core.RailEnv.build_rail_namespace_tree
    :noindex:

.. automethod:: rail.core.RailEnv.print_rail_namespace_tree
    :noindex:

.. automethod:: rail.core.RailEnv.print_rail_stage_dict
    :noindex:

-------------------------------------------------------
Functions to build table of contents for sphinx autodoc
-------------------------------------------------------

.. automethod:: rail.core.RailEnv.do_api_rst
    :noindex:

.. automethod:: rail.core.RailEnv.do_stage_type_api_rst
    :noindex:
