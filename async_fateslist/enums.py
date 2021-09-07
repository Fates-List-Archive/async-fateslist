import enum


@enum.unique
class ApiVersion(enum.IntEnum):
    current = 2
    default = current
    beta = 3
    deprecated = 1


@enum.unique
class RequestTypes(enum.IntEnum):
    delete = 0
    get = 1
    head = 2
    patch = 3
    put = 4


@enum.unique
class Routes(enum.Enum):
    vote = 'bots/{bot_id}/reviews/{rid}/votes'
    vanity = 'code/{vanity}'
    index = 'index'
    search_list = 'search'
    
    #promotions
    promotions = 'bots/{bot_id}/promotions'
    add_promotion = 'bots/{bot_id}/promotions'
