**********
Start Here
**********

======================================
I've never used RAIL, what does it do?
======================================

.. describe here

RAIL is a software library that can produce and test photometric
redshifts (photo-zs) from many different codes at scale. With RAIL, users can:

* create realistic sample galaxy photometric data for testing against photo-z codes
* estimate photo-z distributions for single galaxies or entire populations, given either real or simulated data
* evaluate the accuracy of the photo-zs against their ground truth

==============================
How do I install RAIL quickly?
==============================

.. direct to Docker container, point to installation page

There are two methods of installing RAIL quickly for use on your computer.

The first method is via the easy install script, which can be found in `the
releases page of the RAIL setup repository
<https://github.com/LSSTDESC/rail_setup/releases>`_. Download and run the Python script,
which will do an interactive question-based installation.

.. code-block:: bash

    wget https://github.com/LSSTDESC/rail_setup/releases/latest/download/install_rail.py
    python install_rail.py

Follow the prompts for installation. This script installs RAIL in a conda
environment ``[env]`` (the name you enter when prompted), which is activated via

.. code-block:: bash

    conda activate [env]

The second method is via running within a Docker container with RAIL installed.
The RAIL image can be found on the `LSSTDESC packages page
<https://github.com/LSSTDESC/rail_setup/pkgs/container/desc-rail>`_.
Pull the image, then build and run your container.


For more detailed instructions, visit the :ref:`installation` page.

=========================
I've installed, now what?
=========================

Take a look at some of the examples to play with in the :ref:`interactive-notebooks`, 
including how to estimate the photometric redshift of a galaxy with known photometry 
across multiple photo-z codes.

=============================================
I want to learn more, where should I go next?
=============================================

To learn more about RAIL and its stages, visit the RAIL Stages section, starting
with the :ref:`rail-stages` page.

To learn how to contribute, visit the :ref:`contributor concepts` page.

===================================
I've used RAIL, how do I credit it?
===================================

To learn how to cite RAIL, visit the :ref:`citations` page.
