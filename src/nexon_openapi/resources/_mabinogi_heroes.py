from __future__ import annotations

from typing import TYPE_CHECKING, Optional, Union
from typing_extensions import Required, TypedDict


import httpx

from ._types import Ocid
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._models import BaseModel
from ..utils import maybe_transform
from .._resource import SyncAPIResource
from .._base_client import make_request_options

if TYPE_CHECKING:
    from .._client import NexonOpenAPI

__all__ = ["MabinogiHeroes", "MabinogiHeroesCharacterBasic"]


class MabinogiHeroes(SyncAPIResource):
    def __init__(self, client: NexonOpenAPI) -> None:
        super().__init__(client)

    def get_ocid(
        self,
        *,
        character_name: str,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> Ocid:
        return self._get(
            "heroes/v1/id",
            options=make_request_options(
                query=maybe_transform(
                    {"character_name": character_name},
                    GetOcidRequestParam,
                ),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=Ocid,
        )

    def get_character_basic(
        self,
        *,
        ocid: Ocid,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[float, httpx.Timeout, None, NotGiven] = NOT_GIVEN,
    ) -> MabinogiHeroesCharacterBasic:
        return self._get(
            path="heroes/v1/character/basic",
            options=make_request_options(
                query=maybe_transform({"ocid": ocid.ocid}, GetCharacterBasicRequestParam),
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
            ),
            cast_to=MabinogiHeroesCharacterBasic,
        )


class GetOcidRequestParam(TypedDict, total=True):
    character_name: Required[str]


class GetCharacterBasicRequestParam(TypedDict, total=False):
    ocid: Required[Ocid]


class MabinogiHeroesCharacterBasic(BaseModel):
    realm_name: str
    character_name: str
    """ 영웅(캐릭터) 명 """

    character_date_create: str
    """ 영웅(캐릭터) 생성 일(시) (UTC0) """

    character_last_login: str
    """ 영웅(캐릭터) 마지막 로그인 일(시) (UTC0) """

    character_last_logout: str
    """ 영웅(캐릭터) 마지막 로그아웃 일(시) (UTC0) """

    character_class_name: str
    """영웅(캐릭터) 직업 명"""

    character_gender: str
    """ 영웅(캐릭터) 성별 """

    character_level: int
    """ 영웅(캐릭터) 레벨 """

    character_exp: int
    """ 영웅(캐릭터) 경험치 """
