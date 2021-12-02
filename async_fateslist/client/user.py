from __future__ import annotations

from typing import Optional, Union
from .. import *

# For initial resolution
from ..enums import ApiVersion
from ..classes import ToMoveAPI

class UserClient:
    '''
    Current API: v2 beta 3
        Default API: v2
        API Docs: https://apidocs.fateslist.xyz
        Enum Reference: https://apidocs.fateslist.xyz/structures/enums.autogen
    '''
    __slots__ = ['token', 'api_ver', 'beta', 'retry', "formattedtoken"]
    
    def __init__(self, token: str, api_ver: Optional[Union[ApiVersion, int]] = ApiVersion.current.value, beta: Optional[bool] = False, retry: Optional[bool] = False):
        if api_ver not in [2,3]:
            raise WrongApiVersionError
        self.token = token
        self.api_ver = api_ver
        self.api_ver = self.api_ver if isinstance(self.api_ver, int) else self.api_ver.value
        self.beta = beta
        self.retry = retry
        self.formattedtoken = f'User {self.token}'
    
    def __str__(self):
        return f'<Fates User-Client Connection | API Version: {self.api_ver} | Beta: {self.beta} | Retry: {self.retry}>'

    async def get_vanity(self, vanity: str) -> ToMoveAPI:
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
        return ToMoveAPI(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.vanity.value[-1], 
                endpoint=Routes.vanity.value[0].formet(vanity=vanity),
                retry=retry
            )
        )
    
    async def get_index(self, cert: bool = True, type_enum:int  = 0) -> ToMoveAPI:
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
        return ToMoveAPI(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.index.value[-1], 
                endpoint=Routes.index.value[0],
                retry=retry,
                json={'cert': cert, 'type_enum': type_enum}
            )
        )
    
    async def search_list(self, query:str, target_type:str = "bots" or "profile") -> ToMoveAPI:
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
        return ToMoveAPI(
            await BaseHTTP(
                api_token=self.formattedtoken, 
                api_ver=self.api_ver
            ).request(
                method=Routes.search_list.value[-1], 
                endpoint=Routes.search_list.value[0],
                retry=retry,
                json={'q': query, 'target_type': target_type}
            )
        )
