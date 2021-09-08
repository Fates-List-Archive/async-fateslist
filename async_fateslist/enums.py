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
    fetch_user = ['users/{user_id}', RequestTypes.get]
    set_user_description = ['users/{user_id}/description', RequestTypes.patch]
    regenerate_user_token = ['users/{user_id}/token', RequestTypes.patch]
    set_js_mode = ['users/{user_id}/js_allowed', RequestTypes.patch]
    get_cache_user = ['users/{user_id}/obj', RequestTypes.get]
    add_bot = ['users/{user_id}/bots/{bot_id}', RequestTypes.put]
    delete_bot = ['users/{user_id}/bots/{bot_id}', RequestTypes.delete]
    edit_bot = ['users/{user_id}/bots/{bot_id}', RequestTypes.patch]
    
    #ula
    get_list = ['ula/list/{url}', RequestTypes.get]
    get_all_lists = ['ula/lists', RequestTypes.get]
    new_list = ['ula/{user_id}/lists', RequestTypes.put]
    delete_list = ['ula/{user_id}/list/{url}', RequestTypes.put]
    edit_list = ['ula/{user_id}/list/{url}', RequestTypes.patch]
    new_endpoint = ['ula/{user_id}/list/{url}/endpoints', RequestTypes.put]
    edit_endpoint = ['ula/{user_id}/list/{url}/endpoints', RequestTypes.patch]
    delete_endpoint = ['ula/{user_id}/list/{url}/endpoint/{feature}', RequestTypes.delete]
    post_stats = ['ula/bots/{bot_id}/stats', RequestTypes.post]
    get_bot = ['ula/bots/{bot_id}', RequestTypes.get]
    get_user_voted = ['ula/bots/{bot_id}/votes/check', RequestTypes.post]
    get_feature_by_id = ['ula/feature/{id}/id', RequestTypes.get]
    get_feature_by_internal_name = ['ula/feature/{iname}/iname', RequestTypes.get]
    
    #reviews
    get_bot_reviews = ['bots/{bot_id}/reviews', RequestTypes.get]
    new_review = ['users/{user_id}/bots/{bot_id}/reviews', RequestTypes.post]
    delete_review = ['users/{user_id}/bots/{bot_id}/reviews/{id}', RequestTypes.delete]
    edit_review = ['users/{user_id}/bots/{bot_id}/reviews/{id}', RequestTypes.patch]
    
    #commands
    get_commands = ['bots/{bot_id}/commands', RequestTypes.get]
    add_command = ['bots/{bot_id}/commands', RequestTypes.post]
    delete_command = ['bots/{bot_id}/commands/{id}', RequestTypes.delete]
    
    #bots
    get_votes_per_month = ['bots/{bot_id}/vpm', RequestTypes.get]
