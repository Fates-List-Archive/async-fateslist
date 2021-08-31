__title__ = 'async_fateslist'
__author__ = 'Dhruva Shaw'
__license__ = 'GNU GENERAL PUBLIC LICENSE'
__copyright__ = 'Copyright 2021-present FatesList'
__version__ = '1.0.0'
__path__ = __import__('pkgutil').extend_path(__path__, __name__)

import logging
from typing import NamedTuple, Literal

from .client import *
from .errors import *
from .widgets import *

