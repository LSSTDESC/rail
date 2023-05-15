************
Installation
************

RAIL is actually distributed as several software packages.   However, depending on your use case it is likely that you will be working directly with one of the packages.

RAIL has multiple dependencies that are sensitive to out-of-date code versions, therefore it is strongly recommended that you create a new dedicated virtual environment for RAIL to avoid problems with pip/conda failing to update some packages that you have previously installed during installation of RAIL.  Also, having multiple version of RAIL in your path can cause difficult to diagnose probems, so we encourage you to make sure that you don't have an existing version of RAIL installed in your `.local` area or in your base conda environment.

RAIL packages
=============

Depending on how you want to use RAIL you will be installing one or more RAIL packages.  So, first let's clarify the
RAIL packages structure.

1. `RAIL <https://github.com/LSSTDESC/RAIL/>`_ (pz-rail on pypi): includes the core RAIL functionality and many algorithms that do not have complicated dependencies.
2. rail_<algorithm> (for now this includes `rail_delight <https://github.com/LSSTDESC/rail_delight>`_, `rail_bpz <https://github.com/LSSTDESC/rail_bpz>`_ and `rail_flexzboost <https://github.com/LSSTDESC/rail_flexzboost>`_)  (pz-rail-<algorithm> on pypi): these are small packages that split out algorithms that do have complicated dependencies.  They are all independent of each other, but each one does depend on RAIL.
3. `rail_hub <https://github.com/LSSTDESC/rail_hub/>`_ (pz-rail-hub on pypi): is the umbrella package that pulls together RAIL and the various rail_<algorithm> packages.
4. `rail_pipelines <https://github.com/LSSTDESC/rail_pipelines/>`_ (pz-rail-pipelines on pypi): is the package where we develop data analysis pipelines that use the various algorithms.

Note that the various RAIL packages all populate the `rail` namespace in python.   I.e., in python you will be importing from `rail` or `rail.pipelines` or `rail.estimation.algos`, not `rail_<alogrithm>` or `rail_pipelines`. 
   
Installing any of the RAIL packages should automatically install all of the dependent RAIL packages.  However, in some cases you might find that you explicitly need to modify the source code in more than one package, in which case you will want to install multiple packages from source.

To create a conda environment named "[name-for-your-env]" that has a specific version of python (in this case 3.9) and pip (and we have found that it is eaiser to use conda to install h5py, so we do that as well), run the command:

.. code-block:: bash

    conda create -n [name-for-your-env] pip python=3.9 h5py
    
Where you have replaced [name-for-your-env] with whatever name you wish to use, e.g. `rail`.
You can then run the command

.. code-block:: bash

    conda activate [name-for-your-env]

To activate this environment.  We are now ready to install RAIL.

Now you need to decide which RAIL packages to install and if you want to install from source, or just install the packages.

If you want to add the conda environment that you are about to create as a kernel that you can use in a Jupyter notebook, see the `Adding your kernel to jupyter` section further down on this page.


Installing with pip
-------------------

All you have to do is:

.. code-block:: bash

    pip install <package>


Installing from source
----------------------

To install RAIL from source, you will `Clone this repo <https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository>`_ to your local workspace.  Specifically:

.. code-block:: bash

    git clone https://github.com/LSSTDESC/RAIL.git  # (or whichever packages you need)
    cd RAIL
    pip install -e .[all] # (or pip install -e '.[all]' if you are using zsh, note the single quotes). 


If you only want to install the dependencies for a specific piece of RAIL, you can change the install option. E.g. to install only the dependencies for the Creation Module or the Estimation Module, run `pip install .[creation]` or `pip install .[estimation]` respectively. For other install options, look at the keys for the `extras_require` dictionary at the top of `setup.py`.



Algorithm / architecture specific issues
========================================


Installing Delight
------------------

For Delight you should be able to just do:

.. code-block:: bash

    pip install pz-rail-delight

However, the particular estimator `Delight` is built with `Cython` and uses `openmp`.  Mac has dropped native support for `openmp`, which will likely cause problems when trying to run the `delightPZ` estimation code in RAIL.  See the notes below for instructions on installing Delight if you wish to use this particular estimator.

If you are installing RAIL on a Mac, as noted above the `delightPZ` estimator requires that your machine's `gcc` be set up to work with `openmp`. If you are installing on a Mac and do not plan on using `delightPZ`, then you can simply install RAIL with `pip install .[base]` rather than `pip install .[all]`, which will skip the Delight package.  If you are on a Mac and *do* expect to run `delightPZ`, then follow the instructions `here <https://github.com/LSSTDESC/Delight/blob/master/Mac_installation.md>`_ to install Delight before running `pip install .[all]`.

    
Installing FZBoost
------------------

For FZBoost, you should be able to just do

.. code-block:: bash

    pip install pz-rail-flexzboost

But if you run into problems you might need to:

- install `xgboost` with the command `pip install xgboost==0.90.0`
- install FlexCode with `pip install FlexCode[all]`


Installing bpz_lite
-------------------

For bpz_lite, you should be able to just do

.. code-block:: bash

    pip install pz-rail-bpz

But if you run into problems you might need to:

- cd to a directory where you wish to clone the DESC_BPZ package and run `git clone https://github.com/LSSTDESC/DESC_BPZ.git`
- cd to the DESC_BPZ directory and run `python setup.py install` (add `--user` if you are on a shared system such as NERSC)
- try `pip install pz-rail-bpz` again.

If you've installed rail and bpz to different directories (most commonly, you've installed rail from 
source and bpz from PyPI), you may run into an issue where rail cannot locate a file installed by bpz 
(usually encountered when running the estimation step in Goldenspike). 

To fix this, find your test_bpz.columns file in your bpz directory (`or grab a new one here on 
GitHub <https://github.com/LSSTDESC/rail_bpz/blob/main/src/rail/examples/estimation/configs/test_bpz.columns>`_) 
and copy it into your rail directory to `/RAIL/src/rail/examples/estimation/configs/test_bpz.columns`.

Alternatively, if you don't want to move files, you should be able to replace the configured paths with 
your actual `test_bpz.columns` path:

* inform stage: `bpz_lite.py L89 <https://github.com/LSSTDESC/rail_bpz/blob/65870ffd93ba35356a1af44104a0a78530085789/src/rail/estimation/algos/bpz_lite.py#L89>`_

* estimation: `bpz_lite.py L259 <https://github.com/LSSTDESC/rail_bpz/blob/65870ffd93ba35356a1af44104a0a78530085789/src/rail/estimation/algos/bpz_lite.py#L259>`_



Using GPU-optimization for pzflow
---------------------------------

Note that the Creation Module depends on pzflow, which has an optional GPU-compatible installation.
For instructions, see the `pzflow Github repo <https://github.com/jfcrenshaw/pzflow/>`_.

On some systems that are slightly out of date, e.g. an older version of python's `setuptools`, there can be some problems installing packages hosted on GitHub rather than PyPi.  We recommend that you update your system; however, some users have still reported problems with installation of subpackages necessary for `FZBoost` and `bpz_lite`.  If this occurs, try the following procedure:

Once you have installed RAIL, you can import the package (via `import rail`) in any of your scripts and notebooks.
For examples demonstrating how to use the different pieces, see the notebooks in the `examples/` directory.


Adding your kernel to jupyter
=============================
If you want to use the kernel that you have just created to run RAIL example demos, then you may need to explicitly add an ipython kernel.  You may need to first install ipykernel with `conda install ipykernel`.  You can do then add your kernel with the following command, making sure that you have the conda environment that you wish to add activated.  From your environment, execute the command:
`python -m ipykernel install --user --name [nametocallnewkernel]`
(you may or may not need to prepend `sudo` depending on your permissions).  When you next start up Jupyter you should see a kernel with your new name as an option, including using the Jupyter interface at NERSC.

