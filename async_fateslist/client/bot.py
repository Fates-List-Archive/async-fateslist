from __future__ import annotations

from typing import Optional, Union
from .. import *


class BotClient:
    '''
    Current API: v2 beta 3
        Default API: v2
        API Docs: https://apidocs.fateslist.xyz
        Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen
    '''
    __slots__ = ['token', 'api_ver', 'beta', 'retry']
    
    def __init__(self, token: str, api_ver: Optional[Union[ApiVersion, int]] = ApiVersion.current.value, beta: Optional[bool] = False, retry: Optional[bool] = False):
        if api_ver not in [2,3]:
            raise WrongApiVersionError
        self.token = token
        self.api_ver = self.api_ver if isinstance(self.api_ver, int) else self.api_ver.value
        self.beta = beta
        self.retry = retry
        self.formattedtoken = f'Bot {self.token}'
    
    def __str__(self):
        return f'<Fates Bot-Client Connection | API Version: {self.api_ver} | Beta: {self.beta} | Retry: {self.retry}>'
    
    async def get_vanity(self, vanity: str) -> ToMoveAPIResponse:
        return ToMoveAPIResponse(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.vanity.value[-1], 
                endpoint=Routes.vanity.value[0]
            )
        )