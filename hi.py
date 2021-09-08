import enum

@enum.unique
class RequestTypes(enum.Enum):
    delete = 0
    get = 1
    head = 2
    patch = 3
    put = 4

print(RequestTypes.delete, RequestTypes.delete.value)
print(type(RequestTypes.delete))