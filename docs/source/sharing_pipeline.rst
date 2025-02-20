***********************
Sharing a Rail Pipeline
***********************

Here is an example of the first part of the ``goldenspike`` pipeline definition.


.. code-block:: python

    from rail.utils.path_utils import RAILDIR
    flow_file = os.path.join(RAILDIR, 'rail/examples_data/goldenspike_data/data/pretrained_flow.pkl')
		
   class GoldenspikePipeline(RailPipeline):

        default_input_dict = dict(
            model=flow_file,
        )

   
       def __init__(self):
           RailPipeline.__init__(self)

           DS = RailStage.data_store
           DS.__class__.allow_overwrite = True	   
           bands = ['u','g','r','i','z','y']
           band_dict = {band:f'mag_{band}_lsst' for band in bands}
           rename_dict = {f'mag_{band}_lsst_err':f'mag_err_{band}_lsst' for band in bands}


        self.flow_engine_train = FlowCreator.build(
            model=flow_file,
            n_samples=50,
            seed=1235,
        )

        self.lsst_error_model_train = LSSTErrorModel.build(
            connections=dict(input=self.flow_engine_train.io.output),
            renameDict=band_dict, seed=29,
        )

        self.inv_redshift = InvRedshiftIncompleteness.build(
            connections=dict(input=self.lsst_error_model_train.io.output),
            pivot_redshift=1.0,
        )

        self.line_confusion = LineConfusion.build(
            connections=dict(input=self.inv_redshift.io.output),
            true_wavelen=5007., wrong_wavelen=3727., frac_wrong=0.05,
        )	

What this is doing is:

#. Finding the pretrained model `flow_file` to use to generate data.

#. Defining a class ``GoldenspikePipeline`` to encapsulate the pipeline and setting up that pipeline.

#. Set up the rail ``DataStore`` for interactive use, allowing you to overwrite output files, (say if you re-run the pipeline in a notebook cell).

#. Defining some common parameters, e.g., ``bands``, ``bands_dict`` for the pipeline.

#. Defining four stages, and adding them to the pipeline, note that for each stage the syntax is more or less the same.  We have to define,

   * The name of the stage, i.e., ``self.flow_engine_train`` will make a stage called ``flow_engine_train`` through some python cleverness.

   * The class of the stage, which is specified by which type of stage we ask to build, ``FlowEngine.build`` will make a ``FlowEngine`` stage.

   * Any configuration parameters, which are specified as keyword arguments, e.g., ``n_samples=50``.

   * Any input connections from other stages, e.g., ``connections=dict(input=self.flow_engine_train.io.output)``,
     in the ``self.lsst_error_model_train`` block will connect the ``output`` of ``self.flow_engine_train``
     to the ``input`` of ``self.lsst_error_model_train``.  Later in that example we
     can see how to connect multiple inputs, e.g., one named ``input`` and 
     another named ``model``, as required for an estimator stage.


==============================
Making a configurable Pipeline
==============================

Here is an example of a configurable pipeline, were we select which
algorithms to include in the pipeline


.. code-block:: python

    from rail.utils.algo_library import PZ_ALGORITHMS

    eval_shared_stage_opts = dict(
        metrics=['all'],
        exclude_metrics=['rmse', 'ks', 'kld', 'cvm', 'ad', 'rbpe', 'outlier'],
        hdf5_groupname="",
        limits=[0, 3.5],
        truth_point_estimates=['redshift'],
        point_estimates=['zmode'],
    )


    class PzPipeline(RailPipeline):

        default_input_dict={
            'input_train':'dummy.in',
            'input_test':'dummy.in',
        }

        def __init__(self, algorithms: dict|None=None):
            RailPipeline.__init__(self)

            DS = RailStage.data_store
            DS.__class__.allow_overwrite = True

            if algorithms is None:
                algorithms = PZ_ALGORITHMS

            for key, val in algorithms.items():
                inform_class = ceci.PipelineStage.get_stage(val['Inform'], val['Module'])
                the_informer = inform_class.make_and_connect(
                    name=f'inform_{key}',
                    aliases=dict(input='input_train'),
                    hdf5_groupname='',
                )
                self.add_stage(the_informer)

                estimate_class = ceci.PipelineStage.get_stage(val['Estimate'], val['Module'])
                the_estimator = estimate_class.make_and_connect(
                    name=f'estimate_{key}',
                    aliases=dict(input='input_test'),
                    connections=dict(
                        model=the_informer.io.model,
                    ),
                    calculated_point_estimates=['zmode'],
                    hdf5_groupname='',
                )
                self.add_stage(the_estimator)

                the_evaluator = SingleEvaluator.make_and_connect(
                    name=f'evaluate_{key}',
                    aliases=dict(truth='input_test'),
                    connections=dict(
                        input=the_estimator.io.output,
                    ),
                    **eval_shared_stage_opts,
                )
                self.add_stage(the_evaluator)


The main differences with the previous example are that:

* We pass in a dict that gives the names of all the algorithms to
  include, as well as information on how to load the stages in question.

* Instead of using `build` we use `make_and_connect` follwed by
  `add_stage`.  This is because we are making several stages of the
  same type, but with different names, inside a loop, so the cleverness
  behind the `build` mechanism would not work here.
