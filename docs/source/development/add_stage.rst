********************************
Add a new algorithm / RAIL stage
********************************

=============
New Algorithm
=============

.. format and check content
.. maybe merge into appropriate section in page

To add new functionality that adds a new dependency, you should create a new package
that users will access through RAIL's common API.

Create a new github repository using the `RAIL-project-template
<https://github.com/LSSTDESC/RAIL-project-template>`_. This template makes use of
``copier`` to create a new repository that will use the ``rail`` namespace. The README
for that project contains a few more steps you should take on your repository to include
the same best practices across all rail packages.

Wrap your algorithm in rail stages, using the documentation below in :ref:`New RAIL Stage` as a guide.

Once you have created a new package that is released through PyPI (don't worry - this
packaging is included in the template), you should create a PR against the ``rail``
package to add your package as a dependency. Include your new package name in `the rail
packages config <https://github.com/LSSTDESC/rail/blob/main/rail_packages.yml>`_.


**TODO: add demo then continue to adding a new rail stage section above**

==============
New RAIL Stage
==============

To make it easier to eventually run RAIL algorithms at scale, all of the various
algorithms are implemented as subclasses of the
:py:class:`rail.core.stage.RailStage` class.  A ``RailStage`` is intended to
take a particular set of inputs and configuration parameters, run a single bit
of analysis, and produce one or more output files.  The inputs, outputs and
configuration parameters are all defined in particular ways to allow
``RailStage`` objects to be integrated into larger data analysis pipelines.

--------------
Simple Example
--------------

The following example has all of the required pieces of a ``RailStage`` and
almost nothing else.

.. code-block:: python

   class ColumnMapper(RailStage):
       """Utility stage that remaps the names of columns.

   Notes
   -----
       1. This operates on pandas dataframes in parquet files.

       2. In short, this does:
       `output_data = input_data.rename(columns=self.config.columns, inplace=self.config.inplace)`

       """
       name = 'ColumnMapper'
       entrypoint_function = "__call__"  # the user-facing science function for this class
       config_options = RailStage.config_options.copy()
       config_options.update(
        columns=Param(dict, required=True, msg="Map of columns to rename"),
        inplace=Param(bool, default=False, msg="Update file in place"),
    )

   inputs = [('input', PqHandle)]
       outputs = [('output', PqHandle)]


       def run(self):
           data = self.get_data('input', allow_missing=True)
           out_data = data.rename(columns=self.config.columns, inplace=self.config.inplace)
           if self.config.inplace:  #pragma: no cover
               out_data = data
           self.add_data('output', out_data)

       def __call__(self, data: pd.DataFrame) -> pd.DataFrame:
           """Return a table with the columns names changed

           Parameters
           ----------
           sample : pd.DataFrame
               The data to be renamed

           Returns
           -------
           pd.DataFrame
               The degraded sample
           """
           self.set_data('input', data)
           self.run()
           return self.get_handle('output')


The required pieces, in the order that they appear are:

#. The ``ColumnMapper(RailStage):`` defines a class called ``ColumnMapper`` and
   specifies that it inherits from ``RailStage``.
#. The ``entrypoint_function`` line provides the name of the main function that 
   the user should call to use this class as a string, for use in the ``interactive`` 
   module.
#. The ``config_options`` lines define the configuration parameters for this
   class, as well as their default values.  Note that here we are copying the
   configuration parameters from the ``RailStage`` as well as defining some new
   ones.
#. The ``run()`` method does the actual work.


----------------
Advanced Example
----------------

Here is an example of a slightly more complicated ``RailStage``.


.. code-block:: python

   class NaiveStack(PZSummarizer):
       """Summarizer which simply histograms a point estimate
       """

       name = 'NaiveStack'
       entrypoint_function = "inform"  # the user-facing science function for this class
       config_options = PZSummarizer.config_options.copy()
       config_options.update(zmin=SharedParams.copy_param("zmin"),
                             zmax=SharedParams.copy_param("zmax"),
                             nzbins=SharedParams.copy_param("nzbins"),
                             seed=Param(int, 87, msg="random seed"),
                             nsamples=Param(int, 1000, msg="Number of sample distributions to create"))
       outputs = [('output', QPHandle),
                  ('single_NZ', QPHandle)]

       def __init__(self, args, **kwargs):
           super().__init__(self, args, **kwargs)
           self.zgrid = None

       def run(self):
           rng = np.random.default_rng(seed=self.config.seed)
           test_data = self.get_data('input')
           self.zgrid = np.linspace(self.config.zmin, self.config.zmax, self.config.nzbins + 1)
           pdf_vals = test_data.pdf(self.zgrid)
           yvals = np.expand_dims(np.sum(np.where(np.isfinite(pdf_vals), pdf_vals, 0.), axis=0), 0)
           qp_d = qp.Ensemble(qp.interp, data=dict(xvals=self.zgrid, yvals=yvals))

           bvals = np.empty((self.config.nsamples, len(self.zgrid)))
           for i in range(self.config.nsamples):
               bootstrap_draws = rng.integers(low=0, high=test_data.npdf, size=test_data.npdf)
               bvals[i] = np.sum(pdf_vals[bootstrap_draws], axis=0)
           sample_ens = qp.Ensemble(qp.interp, data=dict(xvals=self.zgrid, yvals=bvals))

           self.add_data('output', sample_ens)
           self.add_data('single_NZ', qp_d)


The main difference with this new class is that it inherits from the
``PZSummarizer`` ``RailStage`` subclass.  A ``PZSummarizer`` will take an
ensemble of p(z) distributions for many objects, and summarize them into a
single ``n(z)`` distribution for that ensemble.

A few things to note:

#. We copy the configuration parameters for ``PZSummarizer`` and then add
   additional ones. In particular, some of the configuration parameters are copied 
   from the ``SHARED_PARAMS`` dictionary using the ``SharedParams`` class. This 
   copies over the existing Parameter including its default value and message.
   See :ref:`Shared Parameters` for a list of the existing Shared Parameters and 
   more information on them.  
#. The ``run()`` method is implemented here, but the function for interactive
   use ``summarize()`` is actually defined in ``PZSummarizer``.
#. While we define the ``outputs`` here, we just use the inputs as defined in
   ``PZSummarizer``.

