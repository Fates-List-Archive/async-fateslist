from __future__ import annotations

try:
    import PIL
except ImportError:
    raise RuntimeError('You need to install pillow in order to use the Widgets class!')

class Widgets:
    '''It gives you widgets'''
    
    def __init__(self, id: int):
        self.id = id
    
    