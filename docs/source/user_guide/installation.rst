************
Installation
************

.. do we want to keep this intro?

RAIL is actually distributed as several software packages. However, depending
on your use case it is likely that you will be working directly with one of the
packages.

Some of the RAIL algorithms have dependencies that are sensitive to out-of-date
code versions, therefore it is strongly recommended that you create a new
dedicated virtual environment for RAIL to avoid problems with pip/conda failing
to update some packages that you have previously installed during installation
of RAIL.  Also, having multiple versions of RAIL in your path can cause difficult
to diagnose problems, so we encourage you to make sure that you don't have an
existing version of RAIL installed in your ``.local`` area or in your base conda
environment.

.. note::
    In the following instructions you will see the use of both ``pip`` and ``conda``.
    We have found that ``conda`` is particularly good at creating virtual environments
    and installing packages that have compiled libraries. Thus we prefer it over
    ``pip`` and ``venv`` for those purposes.

    Additionally, we use ``pip`` to build and install RAIL code from source
    because ``conda`` does not provide that functionality.

.. tip::
    Throughout the installation documentation we make reference to ``conda`` as a tool
    to create a RAIL virtual environment and install compiled dependencies we
    acknowledge that it can be potentially very slow. Using ``mamba`` can be
    significantly faster, but it is not as widely adopted in the community.

    If you would like to experiment with ``mamba`` it can be installed with
    ``conda install mamba -n base -c conda-forge``. The `mamba documentation is
    here <https://mamba.readthedocs.io/>`_.

============
Easy Install
============

.. python script

================
Docker Container
================

.. 

==============
Manual Install
==============

-----------
Exploration
-----------

.. format and check content

Here we will be installing the source code from `rail
<https://github.com/LSSTDESC/rail>`_ to access all of the demonstration
notebooks, and use that to install all of the other algorithms. 

We have included an ``environment.yml`` that makes it easy to create a virtual
environment named "[env]" that uses conda to install some packages that have
compiled libraries.

.. tabs::

   .. group-tab:: General

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e .[dev]


      If for some reason the ``pip install .[dev]`` fails (e.g.,because of a problem in
      building the dependencies for one of the algorithms) you can run a more
      fault-tolerant installation using a rail script:

      .. code-block:: bash

          pip install -e .
          rail dev install --package-file rail_packages.yml


      At that point you should be able to run the demonstration notebooks, e.g.;

      .. code-block:: bash

          jupyter-notebook examples/estimation_examples/RAIL_estimation_demo.ipynb


   .. group-tab:: zsh (e.g., Mac M1+ default)

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda env create -f environment.yml -n [env]  # or mamba env create, which is much faster
          conda activate [env]
          pip install -e '.[dev]'


      If for some reason the ``pip install '.[dev]'`` fails (e.g.,because of a problem
      in building the dependencies for one of the algorithms) you can run a more
      fault-tolerant installation using a rail script:

      .. code-block:: bash

          pip install -e .
          rail dev install --package-file rail_packages.yml


      At that point you should be able to run the demonstration notebooks, e.g.;

      .. code-block:: bash

          jupyter-notebook examples/estimation_examples/RAIL_estimation_demo.ipynb

----------
Production
----------

.. format and check content

Here we will be installing all of the RAIL algorithms into an existing virtual
environment "[env]". To do this we recommend that you install ``rail`` from
source, to be sure to get the latest version of the ``conda-reqs.txt`` file.

.. tabs::

   .. group-tab:: General

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda activate [env]
          conda install -n [env] -c conda-forge --file conda-reqs.txt  # or mamba install, which is much faster
          pip install .[algos]


      Again, if for some reason the ``pip install .[algos]`` fails (e.g.,because of a
      problem in building the dependencies for one of the algorithms) you can run a more
      fault-tolerant installation using a rail script:

      .. code-block:: bash

          pip install .
          rail dev install --package-file rail_packages.yml


   .. group-tab:: zsh (e.g., Mac M1+ default)

      .. code-block:: bash

          git clone https://github.com/LSSTDESC/rail.git
          cd rail
          conda activate [env]
          conda install -n [env] -c conda-forge --file conda-reqs.txt  # or mamba install, which is much faster
          pip install '.[algos]'


      Again, if for some reason the `pip install '.[algos]'` fails (e.g.,because of a
      problem in building the dependencies for one of the algorithms) you can run a more
      fault-tolerant installation using a rail script:

      .. code-block:: bash

          pip install .
          rail dev install --package-file rail_packages.yml

=================
Developer Install
=================

.. link to actual content in contributing section