import enum

class ApiVersion(enum.Enum):
    current: int = 2
    default: int = current
    beta: int = 3
    deprecated: int = 1
