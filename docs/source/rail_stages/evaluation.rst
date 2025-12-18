**********
Evaluation
**********

.. quick summary
.. comparing the estimated photometric redshifts to known true values, in order to assess the performance of the estimation algorithm

Evaluation is a type of RAIL stage which compares estimated photometric
redshifts to known true values, in order to assess the performance of the
estimation algorithm.

.. flowchart

.. contents:: Table of Contents
   :backlinks: top
   :local:

==========
Evaluators 
==========

Evaluators evaluate the performance of a photo-z estimator against reference
point estimate.

------------
Dist to Dist
------------

RAIL Package: https://github.com/LSSTDESC/rail_base

Evaluate the performance of a photo-z estimator against reference PDFs.

.. autoclass:: rail.evaluation.dist_to_dist_evaluator.DistToDistEvaluator
    :noindex:
    
-------------
Dist to Point
-------------

RAIL Package: https://github.com/LSSTDESC/rail_base

Evaluate the performance of a photo-z estimator against reference point
estimate.

.. autoclass:: rail.evaluation.dist_to_point_evaluator.DistToPointEvaluator
    :noindex:
   
--------------
Point to Point
--------------

RAIL Package: https://github.com/LSSTDESC/rail_base

Evaluate the performance of a photo-z estimator against reference point
estimate.

.. autoclass:: rail.evaluation.point_to_point_evaluator.PointToPointEvaluator
    :noindex:
   
------
Single
------

RAIL Package: https://github.com/LSSTDESC/rail_base

.. autoclass:: rail.evaluation.single_evaluator.SingleEvaluator
    :noindex: