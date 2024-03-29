import enum
from typing import List, Tuple


#ApiVersion Enums
class ApiVersion(enum.IntEnum):
    current = 2
    default = current
    beta = 3
    deprecated = 1


#Request Types
@enum.unique
class RequestTypes(enum.IntEnum):
    delete = 0
    get = 1
    head = 2
    patch = 3
    put = 4
    post = 5
    
#Routes
@enum.unique
class Routes(Tuple[str, RequestTypes],enum.Enum):
    vanity = ['code/{vanity}', RequestTypes.get]
    index = ['index', RequestTypes.get]
    search_list = ['search', RequestTypes.get]
    
    #promotions
    get_promotions = ['bots/{bot_id}/promotions', RequestTypes.get]
    add_promotion = ['bots/{bot_id}/promotions', RequestTypes.post]
    delete_promotion = ['bots/{bot_id}/promotions/{id}', RequestTypes.delete]
    edit_promotion = ['bots/{bot_id}/promotions/{id}', RequestTypes.patch]
    
    #Policies
    privacy_policy = ['policies/privacy', RequestTypes.get]
    rules = ['policies/rules', RequestTypes.get]
    all_policies = ['policies/all', RequestTypes.get]
    
    #Votes
    user_votes = ['users/{user_id}/bots/{bot_id}/votes', RequestTypes.get]
    create_vote = ['users/{user_id}/bots/{bot_id}/votes', RequestTypes.patch]
    send_test_webhook = ['bots/{bot_id}/testhook', RequestTypes.post]
    vote_review = ['bots/{bot_id}/reviews/{rid}/votes', RequestTypes.patch]
    
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
    get_total_votes = ['bots/{bot_id}/tv', RequestTypes.get]
    regenerate_bot_token = ['bots/{bot_id}/token', RequestTypes.patch]
    fetch_random_bot = ['bots/{bot_id}/random', RequestTypes.get]
    bot_exists = ['bots/{bot_id}', RequestTypes.head]
    bot_widget = ['bots/{bot_id}/widget', RequestTypes.get]
    get_bot_events = ['bots/{bot_id}/events', RequestTypes.get]
    get_bot_ws_events = ['bots/{bot_id}/ws_events', RequestTypes.get]
    set_bot_stats = ['bots/{bot_id}/stats', RequestTypes.post]
    appeal_bot = ['bots/{bot_id}/appeal', RequestTypes.post]


#Promotions
@enum.unique
class PromotionType(enum.IntEnum):
    announcement = 0
    promotion = 1
    generic = 2

# Internal review type enum
@enum.unique
class ReviewType(enum.IntEnum):
    bot = 0
    server = 1
