import enum
from typing import List


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
    post = 5




@enum.unique
class Routes(List[str, RequestTypes],enum.Enum):
    #To Move
    vote_review = ['bots/{bot_id}/reviews/{rid}/votes', RequestTypes.patch]
    vanity = ['code/{vanity}', RequestTypes.get]
    index = ['index', RequestTypes.get]
    search_list = ['search', RequestTypes.get]
    
    #promotions
    promotions = ['bots/{bot_id}/promotions', RequestTypes.get]
    add_promotion = ['bots/{bot_id}/promotions', RequestTypes.post]
    delete_promotion = ['bots/{bot_id}/promotions/{id}', RequestTypes.delete]
    edit_promotion = ['bots/{bot_id}/promotions/{id}', RequestTypes.patch]
    
    #Policies
    privacy_policy = ['policies/privacy', RequestTypes.get]
    rules = ['policies/rules', RequestTypes.get]
    
    #Votes
    user_votes = ['users/{user_id}/bots/{bot_id}/votes', RequestTypes.get]
    create_vote = ['users/{user_id}/bots/{bot_id}/votes', RequestTypes.patch]
    send_test_webhook = ['bots/{bot_id}/testhook', RequestTypes.post]
    
    #System
    get_botlist_stats = ['blstats', RequestTypes.get]
    get_features = ['features', RequestTypes.get]
    get_tags = ['tags', RequestTypes.get]
    check_staff_member = ['is_staff', RequestTypes.get]
    
    #users

    
