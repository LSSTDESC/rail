************
Contributing
************

RAIL is developed publicly on GitHub and welcomes all interested developers, regardless of DESC membership or LSST data rights.
The best way to get involved is to comment on `Issues <https://github.com/LSSTDESC/RAIL/issues?q=>`_ and `make Pull Requests <https://github.com/LSSTDESC/RAIL/compare>`_ for your contributions.

Professional astronomers (including students!) based in the US, Chile, or a French IN2P3 institution are encouraged to `join the LSST-DESC <https://lsstdesc.org/pages/apply.html>`_ to gain access to the `\#desc-pz-rail <https://lsstc.slack.com/archives/CQGKM0WKD>`_ channel on the LSSTC Slack workspace.
Those without data rights who wish to gain access to the Slack channel should `create an Issue <https://github.com/LSSTDESC/RAIL/issues/new/choose>`_ to request that the team leads initiate the process for adding a DESC External Collaborator.

Where to contribute: RAIL packages
==================================

Similar to the installation process, depending on how you want to contribute to RAIL, you will be contributing to one or more of the RAIL packages.  
Given the package structure we imagine three main use cases for contributions:

1. To contribute to the core codebase, including algorithms with no special dependencies, install RAIL from source, indicate what you aim to do in an Issue, and follow the Contribution workflow below.
2. To contribute a new algorithm or engine that depends on packages beyond numpy and scipy, you will probably be making a new rail_<algorithm> repository, and eventually rail_hub.
3. To contribute analysis pipelines you built with RAIL Stages, clone `rail_pipelines` from source and follow the Contribution workflow instructions below.



Contribution workflow
---------------------

The RAIL and rail_<xxx> repositories use an issue-branch-review workflow.
When you identify something that should be done, `make an issue <https://github.com/LSSTDESC/RAIL/issues/new>`_
for it.   
We ask that if applicable and you are comfortable doing so, you add labels to the issue to
mark what part of the code base it relates to, its priority level, and if it's well-suited to newcomers, as opposed to requiring more familiarity with the code or technical expertise.   


To contribute, isolate `an issue <https://github.com/LSSTDESC/RAIL/issues>`_ to work on, assign yourself, and leave a comment on
the issue's discussion page to let others know you're working on it. 
Then, make a branch with a name of the
form `issue/[#]/brief-description` and make changes in your branch. 
While developing in a branch, don't forget to pull from `main` regularly to make sure your work is compatible with other recent changes.

Before you make a pull request we ask that you do two things:
   1. Run `pylint` and clean up the code accordingly.  You may need to
      install `pylint` to do this.
   2. Add unit tests and make sure that the new code is fully
      `covered` (see below).   You make need to install `pytest` and `pytest-cov`
      to do this.  You can use the `do_cover.sh` script in the top
      level directory to run `pytest` and generate a coverage report.

As regards `full coverage`, the automatic tests will require that 100% of the lines are covered by the tests.  However, do note that you can use the comment `#pragma: no cover` to skip bits of code, e.g., a line of code that raises an exception if an input file is missing, rather than test every possible failure mode.

When you're ready to merge your branch into the `main` branch,
`make a pull request <https://github.com/LSSTDESC/RAIL/compare>`_, and request that other team members review it if you have any in mind, for example, those who have consulted on some of the work.
Once the changes have been approved, 1. select "Squash and merge" on the approved pull request, 2. enter `closes #[#]` in the comment field to close the resolved issue, and 3. delete your branch using the button on the merged pull request.

To review a pull request, it's a good idea to start by pulling the changes and running the unit tests (see above). 
Check the code for complete and accurate docstrings, sufficient comments, and to ensure any instances of `#pragma: no cover` (excluding the code from unit test coverage accounting) are extremely well-justified.
Necessary changes to request may include, e.g. writing an exception for an edge case that will break the code, separating out code that's repeated in multiple places, etc.
You may also make suggestions for optional improvements, such as adding a one-line comment before a clever block of code or including a demonstration of new functionality in the example notebooks.



Adding a new Rail Stage
=======================

To make it easier to eventually run RAIL algorithms at scale, all of the various algorithms are implemented as `RailStage` python classes.   A `RailStage` is intended to take a particular set of inputs and configuration parameters, run a single bit of analysis, and produce one or more output files.  The inputs, outputs
and configuration parameters are all defined in particular ways to allow `RailStage` objects to be integrated into larger data analysis pipelines.

Here is an example of a very simple `RailStage`.


.. code-block:: python

    class ColumnMapper(RailStage):
        """Utility stage that remaps the names of columns.

	Notes
	-----
        1. This operates on pandas dataframs in parquet files.

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

	    
This particular example has all of the required pieces and almost nothing else.  The required pieces, in the order that
they appear are:

1.  The `ColumnMapper(RailStage):` defines a class called `ColumnMapper` and specifies that it inherits from `RailStage`.

2.  The `name = ColumnMapper` is required, and should match the class name.

3.  The `config_options` lines define the configuration parameters for this class, as well as their default values.  Note that here we are copying the configuration parameters from the `RailStage` as well as defining some new ones.

4.  The `inputs = [('input', PqHandle)]` and `outputs = [('output', PqHandle)]`  define the inputs and outputs, and the expected data types for those, in this case Parquet files.

5.  The `__init__` method does any class-specific initialization.  In this case there isn't any and the method is superflous.

6.  The `run()` method does the actual work, note that it doesn't take any arguments, that it uses methods `self.get_data()` and `self.add_data()` to access the input data and set the output data, and that it uses `self.config` to access the configuration parameters.

7.  The `__call__()` method provides an interface for interactive use.  It provide a way to pass in data (and in other cases configuraiton parameters) to the class so that they can be used in the run method.


Here is an example of a slightly more complicated `RailStage`.


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


The main difference with this new class is that it inherit from the `PZSummarizer` `RailStage` sub-class.  A `PZSummarizer` will take an
ensemble of p(z) distributions for many objects, and summarize them into a single `n(z)` distribution for that ensemble.

A few things to note:

1.   We copy the configuration parameters for `PZSummarizer` and then add addtional ones.

2.   The `run()` method is implemented here, but the function for interactive use `summarize()` is actually defined in `PZSummarizer`.

3.   While we define the `outputs` here, we just use the inputs as defined in `PZSummarizer`.



Adding a new Rail Pipeline
==========================

Here is an example of the first part of the `goldenspike` pipeline defintion.



.. code-block:: python

    class GoldenspikePipeline(RailPipeline):

        def __init__(self):
            RailPipeline.__init__(self)

            DS = RailStage.data_store
            DS.__class__.allow_overwrite = True
            bands = ['u','g','r','i','z','y']
            band_dict = {band:f'mag_{band}_lsst' for band in bands}
            rename_dict = {f'mag_{band}_lsst_err':f'mag_err_{band}_lsst' for band in bands}

            self.flow_engine_train = FlowEngine.build(
                flow=flow_file,
                n_samples=50,
                seed=1235,
                output=os.path.join(namer.get_data_dir(DataType.catalog, CatalogType.created), "output_flow_engine_train.pq"),
            )

            self.lsst_error_model_train = LSSTErrorModel.build(
                connections=dict(input=self.flow_engine_train.io.output),    
                bandNames=band_dict, seed=29,
                output=os.path.join(namer.get_data_dir(DataType.catalog, CatalogType.degraded), "output_lsst_error_model_train.pq"),
            )

            self.inv_redshift = InvRedshiftIncompleteness.build(
                connections=dict(input=self.lsst_error_model_train.io.output),
                pivot_redshift=1.0,
                output=os.path.join(namer.get_data_dir(DataType.catalog, CatalogType.degraded), "output_inv_redshift.pq"),
            )

            self.line_confusion = LineConfusion.build(
                connections=dict(input=self.inv_redshift.io.output),
                true_wavelen=5007., wrong_wavelen=3727., frac_wrong=0.05,
                output=os.path.join(namer.get_data_dir(DataType.catalog, CatalogType.degraded), "output_line_confusion.pq"),
            )

What this is doing is:

1.  Defining a class `GoldenspikePipeline` to encapsulate the pipeline and setting up that pipeline.

2.  Set up the rail `DataStore` for interactive use, allowing you to overwrite output files, (say if you re-run the pipeline in a notebook cell).

3.  Defining some common parameters, e.g., `bands`, `bands_dict` for the pipeline.

4.  Defining four stages, and adding them to the pipeline, note that for each stage the syntax is more or less the same.  We have to define,

    1.  The name of the stage, i.e., `self.flow_engine_train` will make a stage called `flow_engine_train` through some python cleverness.
 
    2.  The class of the stage, which is specified by which type of stage we ask to build, `FlowEngine.build` will make a `FlowEngine` stage.

    3.  Any configuration parameters, which are specified as keyword argurments, e.g., `n_samples=50`.

    4.  Any input connections from other stages, e.g., `connections=dict(input=self.flow_engine_train.io.output),` in the `self.lsst_error_model_train` block will connect the `output` of self.flow_engine_train to the `input` of `self.lsst_error_model_train`.  Later in that example we can see how to connect multiple inputs, e.g., one named `input` and another named `model`, as required for an estimator stage.

    5.  We use the `namer` class and enumerations to ensure that the data end up following our location convenctions.
