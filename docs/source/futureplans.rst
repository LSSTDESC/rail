************
Future plans
************

RAIL's design aims to break up the PZ WG's pipeline responsibilities into smaller milestones that can be accomplished by individuals or small groups on short timescales, i.e. under a year.
The next stages of RAIL development (tentative project codenames subject to change) are intended to be paper-able projects, each of which addresses one or more SRM deliverables by incrementally 
advancing the code along the way to project completion. They are scoped such that any can be executed in any order or even simultaneously.

* *RAILyard*: Assess the performance of template-fitting codes by extending the creation subpackage to forward model templates.

* *RAIL network*: Assess the performance of clustering-redshift methods by extending the creation subpackage to forward model positions.

* *Off the RAILs*: Investigate the effects of erroneous spectroscopic redshifts (or uncertain narrow-band photo-zs) in a training set by extending the creation subpackage's imperfect prior model.

* *Third RAIL*: Investigate the effects of imperfect deblending on estimated photo-z posteriors by extending the creation subpackage to forward model the effect of imperfect deblending.

* *RAIL gauge*: Investigate the impact of measurement errors (PSF, aperture photometry, flux calibration, etc.) on estimated photo-z posteriors by including their effects in the the forward model of the creation subpackage.

* *DERAIL*: Investigate the impact of imperfect photo-z posterior estimation on a probe-specific (e.g. :math:`3\times2{\rm pt}`) cosmological parameter constraint by connecting the estimation subpackage to other DESC pipelines.

* *RAIL line*: Assess the sensitivity of estimated photo-z posteriors to photometry impacted by emission lines by extending the creation subpackage's forward model.

Informal library of fun train-themed names for future projects/pipelines built with RAIL include: 
`monoRAIL`, `tRAILblazer`, `tRAILmix`, `tRAILer`.
