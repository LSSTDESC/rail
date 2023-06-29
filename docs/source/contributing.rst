************
Contributing
************

RAIL is a constellation of multiple packages developed publicly on GitHub and 
welcomes all interested developers, regardless of DESC membership or LSST data rights.

If you're interested in contributing, but don't know where to start, take a look 
at the list of good first issues from all RAIL repositories 
`here <https://github.com/orgs/LSSTDESC/projects/6/views/20>`_.
Or, create a new issue `here <https://github.com/LSSTDESC/rail/issues/new>`_ to 
suggest a change, and the team will route it to the appropriate repository.

In addition to GitHub, the RAIL team uses the LSSTC Slack workspace for organization.
Professional astronomers (including students!) based in the US, Chile, or a 
French IN2P3 institution are encouraged to 
`join the LSST-DESC <https://lsstdesc.org/pages/apply.html>`_ to gain access to 
the `\#desc-pz-rail <https://lsstc.slack.com/archives/CQGKM0WKD>`_ channel on 
the LSSTC Slack workspace.

Those without data rights who wish to gain access to the Slack channel should 
`create an Issue <https://github.com/LSSTDESC/RAIL/issues/new>`_ to request that 
the team leads initiate the process for adding a DESC External Collaborator.


Where to contribute: RAIL packages
==================================

RAIL functionality is split among several GitHub repositories to make it easier 
to manage ever-changing dependencies. 
Most contain the few stages sharing a particular challenging dependency, with 
the exception of three meta-repositories:

* ``rail`` is the portal for users who want to access all of RAIL's functionality across all the repositories. 

* ``rail_base`` is where the superclasses and underlying infrastructure used by all the standalone repositories are defined.

* ``rail_pipelines`` is a place for users to share the pipelines they build with RAIL so others can call them directly or adapt them to their needs.

Overall, you may find yourself contributing to one or more of these repositories and/or making a new one.

Similar to the installation process, depending on how you want to contribute to 
RAIL, you will be contributing to one or more of the RAIL packages.

In all cases, begin by following the developer installation instructions 
:ref:`Developer Installation` and follow the contribution workflow instructions below.


Contribution workflow
---------------------

The ``rail`` and ``rail_<xxx>`` repositories use an issue-branch-review workflow, 
similar to the standard `GitHub Flow <https://docs.github.com/en/get-started/quickstart/github-flow>`_.

Issue
.....

When you identify something that should be done, `make an issue <https://github.com/LSSTDESC/rail/issues/new>`_
for it -- the admins can move it to the appropriate repository if necessary, but 
if you know the specific ``rail_<xxx>`` package that the issue applies to, please 
do make the issue in that repository.


Branch
......

See :ref:`Developer Installation` for installation instructions.

While developing in a branch, don't forget to pull from `main` regularly (at 
least daily) to make sure your work is compatible with other recent changes.

When you're ready to merge your branch into the `main` branch, create a pull request
("PR") in the rail repository you cloned from. GitHub has instructions 
`here <https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request>`_.

Several continuous integration checks will be performed for new pull requests. 
If any of these automatic processes find issues with the code, you should address 
them in the branch before sending for review. These include unit tests (does the 
code function correctly), pylint (code style), or coverage (how much code is 
exercised in unit tests).

Once you are satisfied with your PR, request that other team members review and 
approve it. You could send the request to someone whom you've worked with on the 
topic, or one of the core maintainers of rail.


Merge
.....

Once the changes in your PR have been approved, these are your next steps:

1. the author merges the change by selecting "Squash and merge" on the approved pull request
2. enter `closes #[#]` in the comment field to close the resolved issue
3. delete your branch using the button on the merged pull request.

Reviewing a PR
..............

To review a pull request, it's a good idea to start by pulling the changes and 
running the unit tests locally. If the continuous integration tests have run 
successfully, there is good hope that the unit tests will run locally as well! 

Check the code for complete and accurate docstrings, sufficient comments, and 
ensure any instances of `#pragma: no cover` (excluding the code from unit test 
coverage accounting) are extremely well-justified.

Feel free to mark the PR with “Request changes” for necessary changes. e.g. 
writing an exception for an edge case that will break the code, updating names 
to adhere to the naming conventions, etc.

It is also considered good practice to make suggestions for optional improvements, 
such as adding a one-line comment before a clever block of code or including a 
demonstration of new functionality in the example notebooks.

Naming conventions
------------------

We follow the `pep8 <https://peps.python.org/pep-0008/#descriptive-naming-styles>`_ 
recommendations for naming new modules and ``RailStage`` classes within them 

Modules
.......

Modules should use all lowercase, with underscores where it aids the readability
of the module name. If the module performs only one of p(z) or n(z) calculations,
it is convenient to include that in the module name.

e.g. 

*  ``simple_neurnet`` is a module name for algorithms that use simple neural networks from sklearn to compute p(z) or n(z)
*  ``random_pz`` is an algorithm that computes p(z)


Stages
......

RailStages are python classes and so should use CapWords convention. All rail 
stages using the same algorithm should use the same short, descriptive prefix, 
and the suffix is the type of stage.

e.g.

*  ``SimpleNNInformer`` is an informer using a simple neural network
*  ``SimpleNNEstimator`` is an estimator using a simple neural network

Possible suffixes include:

* Summarizer
* Informer
* Estimator
* Classifier
* Creator
* Degrader
* Evaluator
* Contribution Types


We anticipate a few types of contributions, and provide separate instructions 
for those workflows:

* Discrete Contributions to the existing codebase [TODO link]
* Adding a new RAIL stage without new dependencies [TODO link]
* Adding a new algorithm/engine (new package) [TODO link]
* Sharing a RAIL pipeline [TODO links]


Everything below here become new pages

Discrete contributions
======================

To contribute, isolate `an issue <https://github.com/LSSTDESC/rail/issues>`_ to work on, assign yourself, and leave a comment on
the issue's discussion page to let others know you're working on it. If you would like to contribute and you don’t have a specific issue in mind, take a look at the list of good first issues here: https://github.com/orgs/LSSTDESC/projects/6/views/20

Following the guide in the TODO: (link) `contribution workflow section`, make a branch with a name like `issue/[#]/brief-description` and make changes in your branch.
While developing in a branch, don't forget to pull from `main` regularly to make sure your work is compatible with other recent changes.


Adding a new Rail Stage
=======================

To make it easier to eventually run RAIL algorithms at scale, all of the various algorithms are implemented as subclasses of the TODO (link) `RailStage<https://github.com/LSSTDESC/rail_base/blob/main/src/rail/core/stage.py#L89>_` class.   A `RailStage` is intended to take a particular set of inputs and configuration parameters, run a single bit of analysis, and produce one or more output files.  The inputs, outputs
and configuration parameters are all defined in particular ways to allow `RailStage` objects to be integrated into larger data analysis pipelines.

Simple Example
The following example has all of the required pieces of a RailStage and almost nothing else.

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

1.  The `ColumnMapper(RailStage):` defines a class called `ColumnMapper` and specifies that it inherits from `RailStage`.

2.  The `name = ColumnMapper` is required, and should match the class name.

3.  The `config_options` lines define the configuration parameters for this class, as well as their default values.  Note that here we are copying the configuration parameters from the `RailStage` as well as defining some new ones.

4.  The `inputs = [('input', PqHandle)]` and `outputs = [('output', PqHandle)]`  define the inputs and outputs, and the expected data types for those, in this case Parquet files.

5.  The `__init__` method does any class-specific initialization.  In this case there isn't any and the method is superfluous.

6.  The `run()` method does the actual work, note that it doesn't take any arguments, that it uses methods `self.get_data()` and `self.add_data()` to access the input data and set the output data, and that it uses `self.config` to access the configuration parameters.

7.  The `__call__()` method provides an interface for interactive use.  It provide a way to pass in data (and in other cases configuration parameters) to the class so that they can be used in the run method.

Advanced Example
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


The main difference with this new class is that it inherits from the `PZSummarizer` `RailStage` subclass.  A `PZSummarizer` will take an
ensemble of p(z) distributions for many objects, and summarize them into a single `n(z)` distribution for that ensemble.

A few things to note:

1.   We copy the configuration parameters for `PZSummarizer` and then add additional ones.

2.   The `run()` method is implemented here, but the function for interactive use `summarize()` is actually defined in `PZSummarizer`.

3.   While we define the `outputs` here, we just use the inputs as defined in `PZSummarizer`.

Adding a new algorithm
======================

To add new functionality that adds a new dependency, you should create a new package that users will access through RAIL’s common API. 

Create a new github repository using the ` RAIL-project-template<https://github.com/LSSTDESC/RAIL-project-template>`_. This template makes use of ` copier` to create a new repository that will use the rail namespace. The README for that project contains a few more steps you should take on your repository to include the same best practices across all rail packages.


Wrap your algorithm in rail stages, using the documentation in [TODO - link to adding a new rail stage] as a guide.

Once you have created a new package that is released through pypi (don't worry - this packaging is included in the template), you should create a PR against the ` rail` package to add your package as a dependency. Include your new package name in ` the rail packages config<https://github.com/LSSTDESC/rail/blob/main/rail_packages.yml>`_.


TODO: add demo then continue to adding a new rail stage section above

Adding a new Rail Pipeline
==========================

Here is an example of the first part of the `goldenspike` pipeline definition.



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

   3.  Any configuration parameters, which are specified as keyword arguments, e.g., `n_samples=50`.

   4.  Any input connections from other stages, e.g., `connections=dict(input=self.flow_engine_train.io.output),` in the `self.lsst_error_model_train` block will connect the `output` of self.flow_engine_train to the `input` of `self.lsst_error_model_train`.  Later in that example we can see how to connect multiple inputs, e.g., one named `input` and another named `model`, as required for an estimator stage.

   5.  We use the `namer` class and enumerations to ensure that the data end up following our location conventions.


