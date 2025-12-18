***********
Style Guide
***********

.. format and check content

===============
Code formatting
===============

We encourage the use of the `Black <https://black.readthedocs.io>`__ and `isort
<https://pycqa.github.io/isort>`__ formatters for Python code, as well as the
`pre-commit <https://pre-commit.com/>`__ Git hook system to enforce this.

==================
Naming conventions
==================

We follow the `pep8 <https://peps.python.org/pep-0008/#descriptive-naming-styles>`_
recommendations for naming new modules and ``RailStage`` classes within them.

------------
Module Names
------------

Modules should use all lowercase, with underscores where it aids the readability of the
module name.

For example:

*  ``skl_neurnet`` is a module name for algorithms that use scikit-learn's simple neural
   network implementation to estimate p(z)
*  ``random_gauss`` is a module name for a p(z) estimation algorithm that assigns each
   galaxy a random Gaussian distribution

It's good for the module name to specify the source of the implementation of a
particularly common algorithm, e.g. ``minisom_som`` and ``somoclu_som`` are distinct.
Note that these names should not be identical to the name of the package the algorithm
came from, to avoid introducing namespace collisions for users who have imported the
original package as well, i.e. ``pzflow_nf`` is a safer name than ``pzflow``.

-----------
Stage Names
-----------

RailStages are python classes and so should use the CapWords convention. All rail stages
using the same algorithm should use the same short, descriptive prefix, and the suffix
is the type of stage.

e.g.

*  ``KNearNeighInformer`` is an informer using the k-nearest neighbors algorithm
*  ``KNearNeighEstimator`` is an estimator using the k-nearest neighbors algorithm

Possible suffixes include:

* Informer
* Estimator
* Summarizer
* Classifier
* Creator
* Degrader
* Evaluator
