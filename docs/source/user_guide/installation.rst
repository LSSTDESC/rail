************
Installation
************

============
Easy Install
============

For a basic user installation, we provide the RAIL setup script. This script can be
downloaded from the `RAIL
Setup <https://github.com/lsstdesc/rail_setup/releases/latest>`_ repository.

This script will create a new virtual environment on your machine, and install the
mininum set of required packages to use RAIL, along with any additional RAIL packages
you specify.

Note that even with this script, some RAIL algorithm packages may require additional
setup steps. See the :ref:`section-installation-troubleshooting` section for more details.

================
Docker Container
================

If you wish to run RAIL in a containerized environment, we provide a `Docker image
<https://github.com/LSSTDESC/rail_setup/pkgs/container/desc-rail>`_ in the LSSTDESC
Container Repository. This Docker image provides a pre-activated Mamba (Conda)
environment with all RAIL packages pre-installed, along with some other useful software
such as Jupyter.

==============
Manual Install
==============

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

-----------
Exploration
-----------

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

To install RAIL for development, refer to the :ref:`developer installation
instructions` page.

=============================
Adding your kernel to jupyter
=============================

If you want to use the kernel that you have just created to run RAIL example demos, then
you may need to explicitly add an ipython kernel. You may need to first install
ipykernel with ``conda install ipykernel``. You can then add your kernel with the
following command, making sure that you have the conda environment that you wish to add
activated. From your environment, execute the command: ``python -m ipykernel install
--user --name [name_to_call_new_kernel]`` (you may or may not need to prepend ``sudo``
depending on your permissions). When you next start up Jupyter you should see a kernel
with your new name as an option, including using the Jupyter interface at NERSC.

.. _section-installation-troubleshooting:

=========================================================
Troubleshooting: Algorithm / Architecture Specific Issues
=========================================================

Before installing a specific algorithm, please make sure to first install pz-rail-base
via

.. code-block:: bash

    pip install pz-rail-base


Installing bpz_lite
-------------------

For bpz_lite, you should be able to just do

.. code-block:: bash

    pip install pz-rail-bpz

But if you run into problems you might need to:

- cd to a directory where you wish to clone the DESC_BPZ package and run ``git clone
  https://github.com/LSSTDESC/DESC_BPZ.git``
- cd to the DESC_BPZ directory and run ``python setup.py install`` (add ``--user`` if
  you are on a shared system such as NERSC)
- try ``pip install pz-rail-bpz`` again.


Installing Delight
------------------

.. tabs::

   .. tab:: General

      For Delight you should be able to just do:

      .. code-block:: bash

          pip install pz-rail-delight


   .. tab:: Mac

      For Delight you should be able to just do:

      .. code-block:: bash

          pip install pz-rail-delight

      However, the particular estimator ``Delight`` is built with ``Cython`` and uses
      ``openmp``.  Mac has dropped native support for ``openmp``, which will likely
      cause problems when trying to run the ``DelightEstimator`` estimation code in
      RAIL.  See the notes below for instructions on installing Delight if you wish to
      use this particular estimator.

      If you are installing RAIL on a Mac, as noted above the ``DelightEstimator``
      estimator requires that your machine's ``gcc`` be set up to work with ``openmp``.
      If you are installing on a Mac and do not plan on using ``DelightEstimator``, then
      you can simply install RAIL with ``pip install .[base]`` rather than ``pip install
      .[all]``, which will skip the Delight package.  If you are on a Mac and *do*
      expect to run ``DelightEstimator``, then `follow the instructions here
      <https://github.com/LSSTDESC/Delight/blob/master/Mac_installation.md>`_ to install
      Delight before running ``pip install .[all]``.


Installing FlexZBoost
---------------------

For FlexZBoost, you should be able to just do

.. code-block:: bash

    pip install pz-rail-flexzboost

But if you run into problems you might need to:

- install ``xgboost`` with the command ``pip install xgboost==0.90.0``
- install FlexCode with ``pip install FlexCode[all]``

Installing fsps
---------------

The fsps package available on PyPI does not include the Fortran-based libraries that are
actually needed. After you install `pz-rail-fsps`, upon running any fsps-based
algorithms for the first time, you will see a message indicating the specific
instructions for properly setting up fsps.

The cause of this is the use of Git submodules in the `python-fsps` package, which are
not handled by `pip`.

Using GPU-optimization for pzflow
---------------------------------

Note that the Creation Module depends on pzflow, which has an optional GPU-compatible
installation. For instructions, see the `pzflow Github repo
<https://github.com/jfcrenshaw/pzflow/>`_.

On some systems that are slightly out of date, e.g. an older version of python's
``setuptools``, there can be some problems installing packages hosted on GitHub rather
than PyPi. We recommend that you update your system; however, some users have still
reported problems with installation of subpackages necessary for ``flexzboost`` and
``bpz_lite``. If this occurs, try the following procedure:

Once you have installed RAIL, you can import the package (via ``import rail``) in any of
your scripts and notebooks. For examples demonstrating how to use the different pieces,
see the notebooks in the ``examples/`` directory.



..  LocalWords:  jupyter environment.yml rail_packages.yml pypi numpy
..  LocalWords:  conda-reqs.txt conda-forge pz-rail-som pz-rail-base
..  LocalWords:  scipy rail_bpz rail_flexzboost pz-rail alogrithm bpz
..  LocalWords:  setup.py pz-rail-delight Cython openmp openmp pzflow
..  LocalWords:  pz-rail-flexzboost xgboost xgboost bpz_lite ipython
..  LocalWords:  pz-rail-bpz Goldenspike bpz_lite.py setuptools
..  LocalWords:  subpackages ipykernel ipykernel nametocallnewkernel
