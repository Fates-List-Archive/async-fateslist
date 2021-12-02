from __future__ import annotations

import aiohttp
from typing import Optional, Union, Awaitable, Coroutine
from . import __version__
from .enums import ApiVersion, RequestTypes, Routes

class Success:
    __slots__=['http_status','json',"done","reason"]
    def __init__(self, done: Optional[str], reason: Optional[str], json: Optional[dict]):
        self.done = done
        self.reason = reason
        self.http_status = 200
        self.json = json
    
    @classmethod
    def dict_to_object(self):
        if self.json:
            self.done = self.json.get('done')
            self.reason = self.json.get('reason')
            return self
        raise LookupError('No json data was gicen')
    
    @classmethod
    def to_dict(self):
        """Converts this embed object into a dict."""
        result = {
            key[1:]: getattr(self, key)
            for key in self.__slots__
            if key[0] == '_' and hasattr(self, key)
        }
        try:
            colour = result.pop('json')
        except KeyError:
            pass
        return result 


class Error:
    pass


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
        
        async with aiohttp.ClientSession() as session:
            with session.request(str(method.name).upper(), f'https://fateslist.xyz/api/{str(endpoint)}',headers=headers,json=json) as response:
                return await response
     
