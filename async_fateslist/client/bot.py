from __future__ import annotations

from typing import Optional, Union
from ..errors import WrongApiVersionError

from ..enums import ApiVersion, ReviewType, Routes
from ..classes import GeneralJsonOnlyClass, Promotion, GeneralClass
from ..widgets import Widgets
from ..http_client import BaseHTTP, Error, Success

class BotClient:
    '''
    Current API: v2 beta 3
        Default API: v2
        API Docs: https://apidocs.fateslist.xyz
        Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen/
    '''
    __slots__ = ['token', 'bot_id','api_ver', 'beta', 'retry', "formattedtoken", 'widgets']
    
    def __init__(self, bot_id: int, token: Optional[str] = "", api_ver: Optional[Union[ApiVersion, int]] = ApiVersion.current.value, beta: Optional[bool] = False, retry: Optional[bool] = False):
        if api_ver not in [2,3]:
            raise WrongApiVersionError
        self.bot_id = bot_id
        self.token = token
        self.api_ver = api_ver
        self.api_ver = self.api_ver if isinstance(self.api_ver, int) else self.api_ver.value
        self.beta = beta
        self.retry = retry
        self.formattedtoken = f'Bot {self.token}'
        self.widgets = Widgets(id=bot_id, api_ver=self.api_ver, target_type=ReviewType.bot)
    
    def __str__(self):
        return f'<Fates Bot-Client Connection| Bot ID: {self.bot_id} | API Version: {self.api_ver} | Beta: {self.beta} | Retry: {self.retry}>'
    
    async def get_vanity(self, vanity: str) -> GeneralJsonOnlyClass:
        '''
        Get Vanity
        
        PATH PARAMETERS
            vanity [required] : string (Vanity)
        
        Responses
            200 Successful Response
                RESPONSE SCHEMA: application/json
                    type [required] : string (Type)
                    redirect [required] : string (Redirect)
            422 Validation Error
                RESPONSE SCHEMA: application/json
                    detail : Array of objects (Detail)
        '''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.vanity.value[-1], 
                endpoint=Routes.vanity.value[0].formet(vanity=vanity),
                retry=self.retry
            )
        )
    
    async def get_index(self, cert: bool = True, type_enum:int  = 0) -> GeneralJsonOnlyClass:
        '''
        Get Index
        For any potential Android/iOS app, crawlers etc.

        QUERY PARAMETERS
        t [int (T)] | Default: 0 (0/1)
        cert [boolean (Cert)] | Default: true
        
        Responses
            200 Successful Response
                RESPONSE SCHEMA: application/json
                    tags_fixed [required] : Array of objects (FLTags)
                    top_voted [required] : Array of objects (BotPartialList)
                    certified_bots [required] : Array of objects (BotPartialList)
                    new_bots [required] : Array of objects (BotPartialList)
                    roll_api [required] : string (Roll Api)
            422 Validation Error
                RESPONSE SCHEMA: application/json
                    detail : Array of objects (Detail)
        '''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.index.value[-1], 
                endpoint=Routes.index.value[0],
                retry=self.retry,
                json={'cert': cert, 'type_enum': type_enum}
            )
        )
    
    async def search_list(self, query:str, target_type:str = "bots" or "profile") -> GeneralJsonOnlyClass:
        '''
        Search List
        For any potential Android/iOS app, crawlers etc. Q is the query to search for. T is either bots or profiles

        QUERY PARAMETERS
        q [required] : string (Q)
        t [string (T)] | Default: "bots"
        
        Responses
            200 Successful Response
                RESPONSE SCHEMA: application/json
                    tags_fixed [required] : Array of objects (FLTags)
                    query [required] : string (Query)
                    search_res [required] : Array of any (Search Res)
                    profile_search [required] : boolean (Profile Search)
            422 Validation Error
                RESPONSE SCHEMA: application/json
                    detail : Array of objects (Detail)
        '''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.search_list.value[-1], 
                endpoint=Routes.search_list.value[0],
                retry=self.retry,
                json={'q': query, 'target_type': target_type}
            )
        )
    
    @classmethod
    async def get_promotion(self) -> Promotion:
        '''
        Returns all the promotions for a bot on Fates List

        PATH PARAMETERS
            bot_id [required] : integer (Bot Id)
        Responses
            200 Successful Response
                RESPONSE SCHEMA: application/json
                    promotions [required] : Array of objects (BotPromotionList)

            422 Validation Error
                RESPONSE SCHEMA: application/json
                    detail : Array of objects (Detail)
        '''
        data = await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.get_promotions.value[-1], 
                endpoint=Routes.get_promotions.value[0].format(bot_id=self.bot_id),
                retry=self.retry,
            )
        for i in data:
            yield Promotion(json=i).dict_to_object()
    
    async def new_promotion(self, promotion: Promotion) -> Union[Success, Error]:
        '''
        Creates a promotion for a bot. Type can be 1 for announcement, 2 for promotion or 3 for generic

        AUTHORIZATIONS:
            Bot
        PATH PARAMETERS
            bot_id [required] : integer (Bot Id)
        REQUEST BODY SCHEMA: application/json
            title [required] : string (Title)
            info [required] : string (Info)
            css	: string (Css)
            type [required] : integer (PromotionType) (Enum: 0 1 2) An enumeration.

        Responses
            200 Successful Response
                RESPONSE SCHEMA: application/json
                    done [required] : boolean (Done)
                    reason	: string (Reason)
            422 Validation Error
                RESPONSE SCHEMA: application/json
                    detail : Array of objects (Detail)
        '''
        return await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.add_promotion.value[-1], 
                endpoint=Routes.add_promotion.value[0].format(bot_id=self.bot_id),
                retry=self.retry,
                json=promotion.to_dict()
            )
    
    async def privacy_policy(self) -> GeneralJsonOnlyClass:
        '''Returns the privacy policy for fates list as a JSON'''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.privacy_policy.value[-1], 
                endpoint=Routes.privacy_policy.value[0],
                retry=self.retry,
            )
        )
    
    async def rules(self) -> GeneralJsonOnlyClass:
        '''Returns the rules for fates list as a JSON'''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.rules.value[-1], 
                endpoint=Routes.rules.value[0],
                retry=self.retry,
            )
        )
    
    async def all_policies(self) -> GeneralJsonOnlyClass:
        '''Returns the all policies for fates list as a JSON'''
        return GeneralJsonOnlyClass(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.all_policies.value[-1], 
                endpoint=Routes.all_policies.value[0],
                retry=self.retry,
            )
        )
