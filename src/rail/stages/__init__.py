from ._version import __version__
from rail.core.utilStages import *
from rail.creation.engine import * 
from rail.creation.engines.flowEngine import *

from rail.creation.degrader import *
from rail.creation.degradation.grid_selection import *
from rail.creation.degradation.lsst_error_model import *
from rail.creation.degradation.quantityCut import *
from rail.creation.degradation.spectroscopic_degraders import *
from rail.creation.degradation.spectroscopic_selections import *

from rail.estimation.estimator import *
from rail.estimation.summarizer import *
from rail.estimation.algos.NZDir import *
from rail.estimation.algos.knnpz import *
from rail.estimation.algos.naiveStack import *
from rail.estimation.algos.pointEstimateHist import *
from rail.estimation.algos.pzflow import *
from rail.estimation.algos.randomPZ import *
from rail.estimation.algos.sklearn_nn import *
from rail.estimation.algos.trainZ import *
from rail.estimation.algos.varInference import *

from rail.evaluation.evaluator import Evaluator

try:
    from rail.estimation.algos.delightPZ import *
except ImportError:  # pragma: no cover
    pass
try:
    from rail.estimation.algos.bpz_lite import *
except ImportError:  # pragma: no cover
    pass
try:
    from rail.estimation.algos.flexzboost import *
except ImportError:  # pragma: no cover
    pass
    
from rail.evaluation import *
