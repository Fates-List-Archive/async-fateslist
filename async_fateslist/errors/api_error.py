from __future__ import annotations
from typing import Awaitable, Coroutine, Optional, Union, Callable

class WrongApiVersionError(RuntimeError):
    def __str__(self):
        return f'<{self.__name__} The API version must either 2 or 3>'
    
    
class RateLimited(Exception):
    __slots__ = ['status', 'retry_after', 'error', "request_obj", "retry"]
    
    def __init__(self, request_obj: Optional[Union[Awaitable, Coroutine, Callable]], retry: bool = False):
        self.request_obj = request_obj
        self.status: int = 429
        self.retry_after: int = None
        self.error: str = None
        self.retry = retry
    
    def __str__(self):
        return f'<RateLimited 429 ,timeout={self.retry_after}, error={self.error}>'