
**********************
Adding a new algorithm
**********************

To add new functionality that adds a new dependency, you should create a new package that users 
will access through RAIL's common API. 

Create a new github repository using the 
`RAIL-project-template <https://github.com/LSSTDESC/RAIL-project-template>`_. 
This template makes use of ``copier`` to create a new repository that will use the ``rail`` namespace. 
The README for that project contains a few more steps you should take on your 
repository to include the same best practices across all rail packages.

Wrap your algorithm in rail stages, using the documentation in :ref:`Adding a new Rail Stage` as a guide.

Once you have created a new package that is released through pypi 
(don't worry - this packaging is included in the template), you should create a PR against the ``rail``
package to add your package as a dependency. Include your new package name in 
`the rail packages config <https://github.com/LSSTDESC/rail/blob/main/rail_packages.yml>`_.


TODO: add demo then continue to adding a new rail stage section above