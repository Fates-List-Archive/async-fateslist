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
        headers = {} if not headers else headers
                
        headers["authorization"] = self.api_token
        headers["User-Agent"] = self.user_agent
        headers['FL-API-Version'] = self.ver
        
        async with aiohttp.ClientSession() as sess:
            f = getattr(sess, method.lower())
            async with f(f"{cfg.api}{endpoint}", headers = headers, json = json) as res:
                return APIResponse(res = res, json = json)
     
