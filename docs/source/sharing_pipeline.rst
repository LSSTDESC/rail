***********************
Sharing a Rail Pipeline
***********************

Here is an example of the first part of the ``goldenspike`` pipeline definition.



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

   * We use the ``namer`` class and enumerations to ensure that the data end up following our location conventions.

