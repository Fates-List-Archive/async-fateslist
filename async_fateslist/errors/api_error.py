from __future__ import annotations

class WrongApiVersionError:
    def __str__(self):
        return f'<{self.__name__} The API version must either 2 or 3>'