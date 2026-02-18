***********************************
Developer Installation Instructions
***********************************


Here we will be installing the source code from `rail
<https://github.com/LSSTDESC/rail>`_ to access all of the demonstration
notebooks, and using that to install all of the other algorithms.

We have included an ``environment.yml`` that makes it easy to create a virtual
environment named "[env]" that uses conda to install some packages that have
compiled libraries.

Since this will install multiple subdirectories, we recommend creating a 
directory for all the RAIL code to live in and performing the following installation 
within that directory. 

.. tabs::

   .. group-tab:: General

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e .
          rail dev clone-source --package-file rail_packages.yml
          rail dev install --package-file rail_packages.yml --from-source


   .. group-tab:: zsh (e.g., Mac M1+ default)

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e .
          rail dev clone-source --package-file rail_packages.yml
          rail dev install --package-file rail_packages.yml --from-source


RAIL Command Line Utility
=========================

RAIL provides a command line utility to help with installation and maintenance of RAIL.
The command line utility is called ``rail``. You can see the available commands by
running ``rail --help``.

The most useful commands are:

- ``rail install``: install RAIL packages from pypi or from source.
- ``rail update-source``: update RAIL packages from source.

.. tip::
    To update all your rail packages, in the current environment, use:
    ``rail update-source --package-file rail_packages.yml`` from the root of rail.
