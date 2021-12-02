from __future__ import annotations

from typing import Optional, Union
from .. import *

# For initial resolution
from ..enums import ApiVersion
from ..classes import ToMoveAPI

class ServerClient:
    '''
    Current API: v2 beta 3
        Default API: v2
        API Docs: https://apidocs.fateslist.xyz
        Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen/
    '''
    __slots__ = ['token', 'server_id','api_ver', 'beta', 'retry', "formattedtoken"]
    
    def __init__(self, server_id: int,token: str, api_ver: Optional[Union[ApiVersion, int]] = ApiVersion.current.value, beta: Optional[bool] = False, retry: Optional[bool] = False):
        if api_ver not in [2,3]:
            raise WrongApiVersionError
        self.server_id = server_id
        self.token = token
        self.api_ver = self.api_ver if isinstance(self.api_ver, int) else self.api_ver.value
        self.beta = beta
        self.retry = retry
        self.formattedtoken = f'Server {self.token}'
    
    def __str__(self):
        return f'<Fates Server-Client Connection| Server ID: {self.server_id} | API Version: {self.api_ver} | Beta: {self.beta} | Retry: {self.retry}>'
    
    @property
    def server_widget(self):
        raise NotImplementedError
