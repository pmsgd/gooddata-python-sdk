# coding: utf-8

"""
    OpenAPI definition

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0
    Contact: support@gooddata.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from gooddata_api_client import schemas  # noqa: F401


class JsonApiUserDataFilterOutDocument(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "data",
        }
        
        class properties:
        
            @staticmethod
            def data() -> typing.Type['JsonApiUserDataFilterOut']:
                return JsonApiUserDataFilterOut
            
            
            class included(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JsonApiUserDataFilterOutIncludes']:
                        return JsonApiUserDataFilterOutIncludes
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['JsonApiUserDataFilterOutIncludes'], typing.List['JsonApiUserDataFilterOutIncludes']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'included':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JsonApiUserDataFilterOutIncludes':
                    return super().__getitem__(i)
        
            @staticmethod
            def links() -> typing.Type['ObjectLinks']:
                return ObjectLinks
            __annotations__ = {
                "data": data,
                "included": included,
                "links": links,
            }
    
    data: 'JsonApiUserDataFilterOut'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> 'JsonApiUserDataFilterOut': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["included"]) -> MetaOapg.properties.included: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'ObjectLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "included", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> 'JsonApiUserDataFilterOut': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["included"]) -> typing.Union[MetaOapg.properties.included, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['ObjectLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "included", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        data: 'JsonApiUserDataFilterOut',
        included: typing.Union[MetaOapg.properties.included, list, tuple, schemas.Unset] = schemas.unset,
        links: typing.Union['ObjectLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonApiUserDataFilterOutDocument':
        return super().__new__(
            cls,
            *_args,
            data=data,
            included=included,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.json_api_user_data_filter_out import JsonApiUserDataFilterOut
from gooddata_api_client.model.json_api_user_data_filter_out_includes import JsonApiUserDataFilterOutIncludes
from gooddata_api_client.model.object_links import ObjectLinks
