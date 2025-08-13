***********
Citing RAIL
***********

RAIL is open source and may be used according to the terms of its 
`LICENSE <https://github.com/LSSTDESC/RAIL/blob/main/LICENSE>`_ 
(`BSD 3-Clause <https://opensource.org/licenses/BSD-3-Clause>`_).

If you used RAIL in your study, please cite 
`this repository <https://github.com/LSSTDESC/RAIL>`_ and 
`RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_:

.. code-block:: bibtex

    @ARTICLE{2025arXiv250502928T,
           author = {{The RAIL Team} and {van den Busch}, Jan Luca and {Charles}, Eric and {Cohen-Tanugi}, Johann and {Crafford}, Alice and {Crenshaw}, John Franklin and {Dagoret}, Sylvie and {De-Santiago}, Josue and {De Vicente}, Juan and {Hang}, Qianjun and {Joachimi}, Benjamin and {Joudaki}, Shahab and {Bryce Kalmbach}, J. and {Kannawadi}, Arun and {Liang}, Shuang and {Lynn}, Olivia and {Malz}, Alex I. and {Mandelbaum}, Rachel and {Merz}, Grant and {Moskowitz}, Irene and {Oldag}, Drew and {Ruiz-Zapatero}, Jaime and {Rahman}, Mubdi and {Rau}, Markus M. and {Schmidt}, Samuel J. and {Scora}, Jennifer and {Shirley}, Raphael and {St{\"o}lzner}, Benjamin and {Toribio San Cipriano}, Laura and {Tortorelli}, Luca and {Yan}, Ziang and {Zhang}, Tianqing and {the Dark Energy Science Collaboration}},
            title = "{Redshift Assessment Infrastructure Layers (RAIL): Rubin-era photometric redshift stress-testing and at-scale production}",
          journal = {arXiv e-prints},
         keywords = {Instrumentation and Methods for Astrophysics, Cosmology and Nongalactic Astrophysics, Astrophysics of Galaxies},
             year = 2025,
            month = may,
              eid = {arXiv:2505.02928},
            pages = {arXiv:2505.02928},
              doi = {10.48550/arXiv.2505.02928},
    archivePrefix = {arXiv},
           eprint = {2505.02928},
     primaryClass = {astro-ph.IM},
           adsurl = {https://ui.adsabs.harvard.edu/abs/2025arXiv250502928T},
          adsnote = {Provided by the SAO/NASA Astrophysics Data System}
    }


Please consider also inviting the developers as co-authors on publications resulting from your use of RAIL by [making an issue](https://github.com/LSSTDESC/rail/issues/new/choose).

The following list provides the necessary references for external codes accessible through the RAIL ecosystem, which must be cited as follows if those methods are used in a publication:

Creators and degraders:

- **LSSTErrorModel** (Noisifier, rail-astro-tools):  
  Cite: `Ivezić et al. (2019) <https://ui.adsabs.harvard.edu/abs/2019ApJ...873..111I>`_,  
  `Crenshaw et al. (2024) <https://ui.adsabs.harvard.edu/abs/2024AJ....168...80C>`_

- **ObservingConditionDegrader** (Noisifier, rail-astro-tools):  
  Cite: `Hang et al. (2024) <https://arxiv.org/abs/2409.02501>`_

- **SpectroscopicDegraders** (Noisifier, rail-astro-tools):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **QuantityCut** (Selector, rail-base):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **SpectroscopicSelectors** (Selector, rail-astro-tools):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **SOMSpecSelector** (Selector, rail-som):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **UnrecBlModel** (Degrader, rail-astro-tools):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

Photo-z estimators:

- **BPZ** (CatInformer, CatEstimator, `rail-bpz <https://github.com/LSSTDESC/rail_bpz>`_):  
  Cite: `Benítez (2000) <https://ui.adsabs.harvard.edu/abs/2000ApJ...536..571B>`_

- **CMNN** (CatInformer, CatEstimator, `rail-cmnn <https://github.com/LSSTDESC/rail_cmnn>`_):  
  Cite: `Graham et al. (2018) <https://ui.adsabs.harvard.edu/abs/2018AJ....155....1G>`_

- **Delight** (CatInformer, CatEstimator, `rail-delight <https://github.com/LSSTDESC/rail_delight>`_):  
  Cite: `Leistedt et al. (2017) <https://ui.adsabs.harvard.edu/abs/2017ApJ...838....5L>`_

- **DNF** (CatInformer, CatEstimator, `rail-dnf <https://github.com/LSSTDESC/rail_dnf>`_):  
  Cite: `De Vicente et al. (2016) <https://ui.adsabs.harvard.edu/abs/2016MNRAS.459.3078D>`_

- **FlexZBoost** (CatInformer, CatEstimator, `rail-flexzboost <https://github.com/LSSTDESC/rail_flexzboost>`_):  
  Cite: `Izbicki et al. (2017) <https://doi.org/10.1214/17-EJS1302>`_

- **GPz** (CatInformer, CatEstimator, `rail-gpz-v1 <https://github.com/LSSTDESC/rail_gpz_v1>`_):  
  Cite: `Almosallam et al. (2016) <https://ui.adsabs.harvard.edu/abs/2016MNRAS.462..726A>`_

- **k-nearest neighbors** (CatInformer, CatEstimator, `rail-sklearn <https://github.com/LSSTDESC/rail_sklearn>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **LePHARE** (CatInformer, CatEstimator, `rail-lephare <https://github.com/LSSTDESC/rail_lephare>`_):  
  Cite: `Arnouts et al. (1999) <https://ui.adsabs.harvard.edu/abs/1999MNRAS.310..540A>`_

- **Neural network** (CatInformer, CatEstimator, `rail-sklearn <https://github.com/LSSTDESC/rail_sklearn>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **pzflow** (CatInformer, CatEstimator, `rail-pzflow <https://github.com/LSSTDESC/rail_pzflow>`_):  
  Cite: `Crenshaw et al. (2024) <https://ui.adsabs.harvard.edu/abs/2024AJ....168...80C>`_

- **Random Gaussian** (CatInformer, CatEstimator, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **TPZ** (CatInformer, CatEstimator, `rail-tpz <https://github.com/LSSTDESC/rail_tpz>`_):  
  Cite: `Carrasco Kind & Brunner (2013) <https://ui.adsabs.harvard.edu/abs/2013MNRAS.432.1483C>`_

- **trainZ** (CatInformer, CatEstimator, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `Schmidt et al. (2020) <https://academic.oup.com/mnras/article/499/2/1587/5905416>`_

- **Uniform binning** (PZClassifier, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **Equal count binning** (PZClassifier, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **Random forest** (CatInformer, CatClassifier, `rail-sklearn <https://github.com/LSSTDESC/rail_sklearn>`_):  
  Cite: `Breiman (2001) <https://ui.adsabs.harvard.edu/abs/2001MachL..45....5B>`_

- **Variational inference stacking** (PzInformer, PZSummarizer, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `Rau et al. (2022) <https://ui.adsabs.harvard.edu/abs/2022MNRAS.509.4886R>`_

- **minisom** (CatInformer, PZSummarizer, `rail-som <https://github.com/LSSTDESC/rail_som>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **Naive stacking** (PzInformer, PZSummarizer, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `Myles et al. (2020) <https://ui.adsabs.harvard.edu/abs/2020arXiv200712178M>`_

- **somoclu** (CatInformer, PZSummarizer, `rail-som <https://github.com/LSSTDESC/rail_som>`_):  
  Cite: `Wittek et al. (2017) <https://www.jstatsoft.org/index.php/jss/article/view/v078i09>`_

- **NZDIR** (CatInformer, CatSummarizer, `rail-sklearn <https://github.com/LSSTDESC/rail_sklearn>`_):  
  Cite: `Lima et al. (2008) <https://ui.adsabs.harvard.edu/abs/2008MNRAS.390..118L>`_

- **Point estimate histogram** (PzInformer, PZSummarizer, `rail-base <https://github.com/LSSTDESC/rail_base>`_):  
  Cite: `RAIL Team et al. (2025) <https://arxiv.org/abs/2505.02928>`_

- **yet_another_wizz** (YawSummarize, final stage, `rail-yaw <https://github.com/LSSTDESC/rail_yaw>`_):  
  Cite: `van den Busch et al. (2020) <https://ui.adsabs.harvard.edu/abs/2020A&A...642A.200V>`_
