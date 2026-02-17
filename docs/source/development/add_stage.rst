.. _page-add-stage:

********************************
Add a new algorithm / RAIL stage
********************************

=============
New Algorithm
=============

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
packages config <https://github.com/LSSTDESC/rail/blob/main/rail_packages.yml>`_. You should also 
run the ``create_interactive_structure.py`` script in ``rail_base`` and do a PR. This will add in the necessary 
``*.pyi`` files so that the interactive mode will see your new algorithm.


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

   class ColumnMapper (RailStage):
       """Utility stage that remaps the names of columns.

       Notes
       -----
       1. This operates on pandas dataframes in parquet files.

       2. In short, this does:
       `output_data = input_data.rename(columns=self.config.columns, inplace=self.config.inplace)`

       """
       name = 'ColumnMapper'
       entrypoint_function = "__call__"  # the "work" function of this class
       interactive_function = "column_mapper" # what the interative function should be called that wraps this class

       config_options = RailStage.config_options.copy()
       config_options.update(
           columns=Param(dict, required=True, msg="Map of columns to rename"),
           inplace=Param(bool, default=False, msg="Update file in place"),
       )

       inputs = [('input', PqHandle)]
       outputs = [('output', PqHandle)]

       extra_interactive_documentation = """
       Examples
       --------
       Provide examples of interactive usage here
       """

       def run(self):
           data = self.get_data('input', allow_missing=True)
           out_data = data.rename(columns=self.config.columns, inplace=self.config.inplace)
           if self.config.inplace:  #pragma: no cover
               out_data = data
           self.add_data('output', out_data)

       def __call__(self, data: pd.DataFrame) -> PqHandle:
           """Return a table with the columns names changed

           Parameters
           ----------
           sample : pd.DataFrame
               The data to be renamed

           Returns
           -------
           PqHandle
               The degraded sample
           """
           self.set_data('input', data)
           self.run()
           return self.get_handle('output')


.. _term-entrypoint-function:

The required pieces, in the order that they appear are:

#. The ``ColumnMapper (RailStage):`` defines a class called ``ColumnMapper`` and
   specifies that it inherits from ``RailStage``.
#. The ``name`` attribute is used for Pipeline Mode, to interface with ``ceci``, and
   must match exactly the defined name of the class (for ``rail.interactive``)
#.  The ``entrypoint_function`` line provides the name of the main function that
   the user should call to use this class as a string, for use in the interactive
   module. This should be the *only* function required in order to perform this stage,
   after ``make_stage`` (inherited from ``RailStage``).
#. The ``interactive_function`` line provides the name that will be given to this stage
   in the interactive module. Typically this should be a `snake case
   <https://peps.python.org/pep-0008/#function-and-variable-names>`_ version of the
   class name.
#. The ``config_options`` lines define the configuration parameters for this
   class, as well as their default values.  Note that here we are copying the
   configuration parameters from the ``RailStage`` as well as defining some new
   ones.
#. The ``run()`` method does the actual work.

Additionally, the docstring of the ``entrypoint_function`` in this case ``__call__``
must follow `numpydoc guidelines
<https://numpydoc.readthedocs.io/en/latest/format.html>`_. While these are good practice
everywhere, they are required in these functions, so that the contents can be parsed and
re-formatted for the interactive module. Not all of the numpydoc requirements must be
met, so a custom test is provided to check the necessary items. This test can be run as
part of the general test suite, or with the ``wumpydoc.py`` script in ``rail_base``
which can be called against a specific function: ``python wumpydoc.py
rail.estimation.algos.random_gauss.RandomGaussEstimator.estimate`` to validate a single
entrypoint function.

The entrypoint function also takes an unused ``**kwargs``. This is another necessary
modification in order to adapt to the ``rail.interactive`` interface, in which
parameters cannot be distinguished between belonging to ``make_stage`` (i.e., being used
for ``config_option``) and belonging to the entrypoint function itself. Again, this is
tested for in the interactive module test suite.

The ``extra_interactive_documentation`` attribute in the example class shows above is an
optional property for RAIL stages. The contents of this attribute (if provided) will be
appended to the docstring generated for the interactive module. It is recommended to use
this as a location to showcase examples.

.. note::
    Note that contents of both the entrypoint function and the stage class docstrings will
    be used in the docstring of the generated interactive function wrapping each class.
    These docstrings should thus refer as little as possible to the class-specific elements
    of RAIL.

    For example, description for the ``Returns`` section of the docstring for the entrypoint
    function should not detail the format of the data (typically a
    :py:class:`rail.core.DataHandle`), but instead the *contents* of that DataHandle.

----------------
Advanced Example
----------------

Here is an example of a slightly more complicated ``RailStage``.


.. code-block:: python

   class NaiveStackSummarizer(PZSummarizer):
       """Summarizer which simply histograms a point estimate
       """

       name = 'NaiveStack'
       entrypoint_function = "summarize"  # the user-facing science function for this class
       interactive_function = "naive_stack_summarizer"

       config_options = PZSummarizer.config_options.copy()
       config_options.update(zmin=SharedParams.copy_param("zmin"),
                             zmax=SharedParams.copy_param("zmax"),
                             nzbins=SharedParams.copy_param("nzbins"),
                             seed=Param(int, 87, msg="random seed"),
                             nsamples=Param(int, 1000, msg="Number of sample distributions to create"))
       outputs = [('output', QPHandle), ('single_NZ', QPHandle)]

       def __init__(self, args, **kwargs):
           super().__init__(self, args, **kwargs)
           self.zgrid = None

       def summarize(
           self, input_data: qp.Ensemble, **kwargs
       ) -> QPHandle | dict[str, QPHandle]:
           """Summarizer for NaiveStack which returns multiple items

           Parameters
           ----------
           input_data : qp.Ensemble
               Per-galaxy p(z), and any ancillary data associated with it

           Returns
           -------
           QPHandle | dict[str, QPHandle]
               Ensemble with n(z), and any ancillary data
               Return type depends on `output_mode`
           """
           self.set_data("input", input_data)
           self.run()
           self.finalize()
           if len(self.outputs) == 1 or self.config.output_mode != "return":
               results = self.get_handle("output")
           # if there is more than one output and output_mode = return, return them all as a dictionary
           elif len(self.outputs) > 1 and self.config.output_mode == "return":
               results = {}
               for output in self.outputs:
                   results[output[0]] = self.get_handle(output[0])
           return results

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
``PZSummarizer`` ``RailStage`` subclass.  A
:py:class:`rail.estimation.summarizer.PZSummarizer` will take an ensemble of p(z)
distributions for many objects, and summarize them into a single ``n(z)`` distribution
for that ensemble.

A few things to note:

#. We copy the configuration parameters for ``PZSummarizer`` and then add
   additional ones. In particular, some of the configuration parameters are copied
   from the ``SHARED_PARAMS`` dictionary using the ``SharedParams`` class. This
   copies over the existing Parameter including its default value and message.
   See :ref:`Shared Parameters` for a list of the existing Shared Parameters and
   more information on them.
#. While we define the ``outputs`` here, we just use the inputs as defined in
   ``PZSummarizer``.
#. Because the number of outputs does not match that of the parent class
   ``PZSummarizer``, we must re-define the entrypoint function ``summarize`` in order
   for the docstring to match the actual return, and for the case of ``output_mode =
   "return"`` (used for interactive mode), wherein all stage outputs are returned as a
   dictionary, instead of written to files. Were this not the case, the ``summarize``
   method could simply be inherited from ``PZSummarizer``
