from __future__ import annotations

from typing import Awaitable, Coroutine, Optional, Union, Callable
from .enums import *

class ToMoveAPI:
    '''
    This creates a class with attributes as stated in the json for the ToMove response.
    '''
    
    def __init__(self, request_return: Union[Awaitable, Coroutine, Callable]):
        json = request_return.json()
        async for i in json:
            setattr(self, i, json[i])


class Promotion:
    '''
    The promotion object for https://fateslist.xyz/api/docs/redoc#tag/API-v2-Promotions
    '''
    __slots__=['json']
    
    def __init__(self, title:Optional[str], info: Optional[str], css:Optional[str], type_enum:Optional[PromotionType], json: Optional[dict]) -> None:
        self.title = title
        self.info = info
        self.css = css
        self.type = type_enum.value if type_enum else PromotionType.announcement.value
        self.json = json
        
    @classmethod
    def dict_to_object(self):
        if self.json:
            self.title = self.json.get('title')
            self.info = self.json.get('info')
            self.css = self.json.get('css')
            self.type = self.json.get('type')
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
        
