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
    
    def widget_url(self, opts: WidgetOptions):
        '''Returns the widget URL for this bot/server'''
        return f"https://fateslist.xyz/{self.api_version}?{urlencode(opts.dict()}"
    
    def get_widget(self, opts: WidgetOptions) -> aiohttp.ClientResponse:
        '''
        Get Widget

        Returns a widget
        
        format - What format widget to return

        cd - A custom description you wish to set for the widget

        full_desc - If this is set to true, the full description will be used, otherwise, only the first 25 characters will be used

        no_cache - If this is set to true, cache will not be used but will still be updated. 
        If using cd, set this option to true and cache the image yourself.
        Note that no_cache is slow and may lead to ratelimits and/or your got being banned if used excessively
        '''
        return await BaseHTTP(
                api_token="", 
                api_ver=self.api_ver
            ).request(
                method="GET", 
                endpoint=self.widget_url(opts),
                retry=self.retry
            )
        )
