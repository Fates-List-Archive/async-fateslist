from __future__ import annotations

import aiohttp
from typing import Optional, Union, Awaitable, Coroutine
from . import __version__
from .enums import ApiVersion, RequestTypes, Routes


import platform
if int(platform.python_version().split('.')[1]) <= 8:
    from typing import Dict

class BaseHTTP:    
    __slots__ = ['ver', "api_token", "user_agent"]
    
    def __init__(self, api_token, api_ver: Optional[Union[ApiVersion, int]]):
        self.api_token = api_token
        self.ver = api_ver or ApiVersion.current.value
        self.user_agent = f"async_fateslist/{__version__}"       
    
    async def request(
        self, 
        method: RequestTypes, 
        endpoint: Routes,
        api_ver: Optional[Union[ApiVersion, int]],
        json: Optional[dict], 
        headers: Optional[dict], 
        retry: bool = False
    ) -> Union[Awaitable, Coroutine]:
        """Makes a API request"""
        headers = {} if not headers else headers
                
        headers["Authorization"] = self.api_token
        headers["User-Agent"] = self.user_agent
        headers['FL-API-Version'] = api_ver or self.ver
        
        async with aiohttp.ClientSession() as session, sess.request(str(method.name).upper(), f'https://fateslist.xyz/api/{str(endpoint)}',headers=headers,json=json) as response:
            return await response
     
