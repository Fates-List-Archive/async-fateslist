from __future__ import annotations

import aiohttp
from typing import Optional
from ..errors import *

class UserClient:
    '''
    Current API: v2 beta 3
        Default API: v2
        API Docs: https://apidocs.fateslist.xyz
        Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen
    '''
    
    def __init__(self, token: str, api_ver: Optional[int] = 2, beta: Optional[bool] = False, retry: Optional[bool] = False):
        if api_ver not in [2,3]:
            raise WrongApiVersionError
        self.token = token
        self.api_ver = api_ver
        self.beta = beta
        self.retry = retry
    
    def __str__(self):
        return '<Fates User-Client Connection>'