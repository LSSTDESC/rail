***********************
Adding a new Rail Stage
***********************

To make it easier to eventually run RAIL algorithms at scale, all of the various algorithms 
are implemented as subclasses of the :py:class:`rail.core.stage.RailStage` class.
A ``RailStage`` is intended to take a particular set of inputs and configuration parameters, 
run a single bit of analysis, and produce one or more output files.  The inputs, outputs
and configuration parameters are all defined in particular ways to allow ``RailStage``
objects to be integrated into larger data analysis pipelines.

Simple Example
==============

The following example has all of the required pieces of a ``RailStage`` and almost nothing else.

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
  
       config_options = RailStage.config_options.copy()
       config_options.update(chunk_size=100_000, columns=dict, inplace=False)

   inputs = [('input', PqHandle)]
       outputs = [('output', PqHandle)]

       def __init__(self, args, comm=None):
           RailStage.__init__(self, args, comm=comm)

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

#. The ``ColumnMapper(RailStage):`` defines a class called ``ColumnMapper`` and specifies that it inherits from ``RailStage``.

#. The ``name = ColumnMapper`` is required, and should match the class name.

#. The ``config_options`` lines define the configuration parameters for this class, as well as their default values.  Note that here we are copying the configuration parameters from the ``RailStage`` as well as defining some new ones.

#. The ``inputs = [('input', PqHandle)]`` and ``outputs = [('output', PqHandle)]``  define the inputs and outputs, and the expected data types for those, in this case Parquet files.

#. The ``__init__`` method does any class-specific initialization.  In this case there isn't any and the method is superfluous.

#. The ``run()`` method does the actual work, note that it doesn't take any arguments, that it uses methods ``self.get_data()`` and ``self.add_data()`` to access the input data and set the output data, and that it uses ``self.config`` to access the configuration parameters.

#. The ``__call__()`` method provides an interface for interactive use.  It provide a way to pass in data (and in other cases configuration parameters) to the class so that they can be used in the run method.

Advanced Example
================

Here is an example of a slightly more complicated ``RailStage``.


.. code-block:: python
      
   class NaiveStack(PZSummarizer):
       """Summarizer which simply histograms a point estimate
       """

       name = 'NaiveStack'
       config_options = PZSummarizer.config_options.copy()
       config_options.update(zmin=Param(float, 0.0, msg="The minimum redshift of the z grid"),
                             zmax=Param(float, 3.0, msg="The maximum redshift of the z grid"),
                             nzbins=Param(int, 301, msg="The number of gridpoints in the z grid"),
                             seed=Param(int, 87, msg="random seed"),
                             nsamples=Param(int, 1000, msg="Number of sample distributions to create"))
       outputs = [('output', QPHandle),
                  ('single_NZ', QPHandle)]

       def __init__(self, args, comm=None):
           PZSummarizer.__init__(self, args, comm=comm)
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


The main difference with this new class is that it inherits from the ``PZSummarizer`` ``RailStage`` subclass.  A ``PZSummarizer`` will take an
ensemble of p(z) distributions for many objects, and summarize them into a single ``n(z)`` distribution for that ensemble.

A few things to note:

#. We copy the configuration parameters for ``PZSummarizer`` and then add additional ones.

#. The ``run()`` method is implemented here, but the function for interactive use ``summarize()`` is actually defined in ``PZSummarizer``.

#. While we define the ``outputs`` here, we just use the inputs as defined in ``PZSummarizer``.
