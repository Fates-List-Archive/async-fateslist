from __future__ import annotations
from pydantic import BaseModel
from urllib.parse import urlencode
import aiohttp

class WidgetOptions(BaseModel):
    format: str = "png"
    bgcolor: str = "black"
    textcolor: str = "white"
    no_cache: bool = False
    cd: str = ""
    full_desc: bool = False
        
class Widgets:
    '''This class is made for you when you setup async-fateslist'''
    def __init__(self, id: int, target_type: int, api_version: int):
        self.id = id
        self.target_type = target_type
        self.api_version = api_version
        self.retry = True
    
    def url(self, opts: WidgetOptions):
        '''Returns the widget URL for this bot/server'''
        return f"https://fateslist.xyz/{self.api_version}/widgets/{self.id}?{urlencode(opts.dict())}&target_type={self.target_type}"
    
    def download(self, opts: WidgetOptions) -> aiohttp.ClientResponse:
        '''
        Downloads a widget
        '''
        return await BaseHTTP(
            api_token="", 
            api_ver=self.api_ver
        ).request(
            method="GET", 
            endpoint=self.url(opts),
            retry=self.retry
        )
