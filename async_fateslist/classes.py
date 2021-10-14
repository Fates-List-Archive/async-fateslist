from __future__ import annotations

from typing import Awaitable, Coroutine, Optional, Union

class ToMoveAPIResponse:
    '''
    This creates a class with attributes as stated in the json for the ToMove response.
    '''
    
    async def __init__(self, request_return: Union[Awaitable, Coroutine]):
        json = await request_return.json()
        async for i in json:
            setattr(self, i, json[i])