from __future__ import annotations

from typing import Optional, Union
from .. import *

# For initial resolution
from ..enums import ApiVersion, ReviewType
from ..classes import GeneralJsonOnlyClass
from ..widgets import Widgets
from ..errors import WrongApiVersionError

class ServerClient:
    '''
    Current API: v2 beta 3
        Default API: v2
        API Docs: https://apidocs.fateslist.xyz
        Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen/
    '''
    __slots__ = ['token', 'server_id','api_ver', 'beta', 'retry', "formattedtoken", 'widgets']
    
    def __init__(self, server_id: int,token: str, api_ver: Optional[Union[ApiVersion, int]] = ApiVersion.current.value, beta: Optional[bool] = False, retry: Optional[bool] = False):
        if api_ver not in [2,3]:
            raise WrongApiVersionError
        self.server_id = server_id
        self.token = token
        self.api_ver = api_ver
        self.api_ver = self.api_ver if isinstance(self.api_ver, int) else self.api_ver.value
        self.beta = beta
        self.retry = retry
        self.formattedtoken = f'Server {self.token}'
        self.widgets = Widgets(id=server_id, api_ver=self.api_ver, target_type=ReviewType.server)
    
    def __str__(self):
        return f'<Fates Server-Client Connection| Server ID: {self.server_id} | API Version: {self.api_ver} | Beta: {self.beta} | Retry: {self.retry}>'
    
    async def privacy_policy(self) -> GeneralJsonOnlyClass:
        '''Returns the privacy policy for fates list as a JSON'''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.privacy_policy.value[-1], 
                endpoint=Routes.privacy_policy.value[0],
                retry=self.retry,
            )
        )
    
    async def rules(self) -> GeneralJsonOnlyClass:
        '''Returns the rules for fates list as a JSON'''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.rules.value[-1], 
                endpoint=Routes.rules.value[0],
                retry=self.retry,
            )
        )
    
    async def all_policies(self) -> GeneralJsonOnlyClass:
        '''Returns the all policies for fates list as a JSON'''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.all_policies.value[-1], 
                endpoint=Routes.all_policies.value[0],
                retry=self.retry,
            )
        )
