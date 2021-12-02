from __future__ import annotations
from pydantic import BaseModel

class WidgetOptions(BaseModel):
    format: str = "png"
    bgcolor: str = "black"
    textcolor: str = "white"
    no_cache: bool = False
    cd: str = ""
    full_desc: bool = False
        
class Widgets:
    '''This class is made for you when you setup async-fateslist'''
    def __init__(self, id: int, target_type: int):
        self.id = id
        self.target_type = target_type
    
    def widget_url(opts: WidgetOptions):
        return
    
    def get_widget(self, format: str = "png", cd: str = "", full_desc: bool = False, no_cache: bool = True):
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
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method="GET", 
                endpoint=self.widget_url(format, cd, full_desc, no_cache),
                retry=self.retry
            )
        )
