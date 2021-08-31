import aiohttp
from typing import Optional
from . import __version__
from .enums import ApiVersion

class BaseHTTP:    
    __slots__ = ['id', 'ver']
    
    def __init__(self, id, api_ver: Optional[int]):
        self.id = id
        self.ver = api_ver or ApiVersion.current
        self.user_agent = f"async_fateslist/{__version__}"       
    
    async def request(
        self, 
        method: str, 
        endpoint: str,
        api_ver: int,
        json: Optional[dict] = None, 
        headers: Optional[dict] = None, 
        retry: bool = False
    ):
        """Makes a API request"""
        if method.lower in ['post', 'get', 'patch', 'delete', 'put', 'head']:
            raise Exception #This will be custom exception
        headers = {} if not headers else headers
                
        headers["authorization"] = self.api_token
        headers["User-Agent"] = self.user_agent
        headers['FL-API-Version'] = self.ver
        
        async with aiohttp.ClientSession() as sess:
            async with sess.request() as res:
                return APIResponse(res = res, json = json)
     
