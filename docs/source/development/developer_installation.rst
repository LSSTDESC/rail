***********************************
Developer Installation Instructions
***********************************

.. format and check content

Here we will be installing the source code from `rail
<https://github.com/LSSTDESC/rail>`_ to access all of the demonstration
notebooks, and using that to install all of the other algorithms.

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
