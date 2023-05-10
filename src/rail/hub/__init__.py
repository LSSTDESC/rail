from ._version import __version__

import rail.stages
rail.stages.import_and_attach_all()
from rail.stages import *
