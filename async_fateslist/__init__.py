__title__ = 'async_fateslist'
__author__ = 'Dhruvacube'
__license__ = 'GNU GENERAL PUBLIC LICENSE'
__copyright__ = 'Copyright 2021-present FatesList'
__version__ = '1.0.0candidate'
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

# import logging
from typing import NamedTuple, Literal

from .client import *
from .errors import *
from .widgets import *
from .http_client import *
from .classes import *
from .enums import *

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int


version_info: VersionInfo = VersionInfo(major=1, minor=0, micro=0, releaselevel='beta', serial=0)

# logging.getLogger(__name__).addHandler(logging.NullHandler())

