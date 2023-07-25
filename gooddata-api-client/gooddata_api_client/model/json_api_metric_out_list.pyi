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


class JsonApiMetricOutList(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A JSON:API document with a list of resources
    """


    class MetaOapg:
        required = {
            "data",
        }
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JsonApiMetricOutWithLinks']:
                        return JsonApiMetricOutWithLinks
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['JsonApiMetricOutWithLinks'], typing.List['JsonApiMetricOutWithLinks']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JsonApiMetricOutWithLinks':
                    return super().__getitem__(i)
            
            
            class included(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['JsonApiMetricOutIncludes']:
                        return JsonApiMetricOutIncludes
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['JsonApiMetricOutIncludes'], typing.List['JsonApiMetricOutIncludes']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'included':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'JsonApiMetricOutIncludes':
                    return super().__getitem__(i)
        
            @staticmethod
            def links() -> typing.Type['ListLinks']:
                return ListLinks
            __annotations__ = {
                "data": data,
                "included": included,
                "links": links,
            }
    
    data: MetaOapg.properties.data
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["included"]) -> MetaOapg.properties.included: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["links"]) -> 'ListLinks': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", "included", "links", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["included"]) -> typing.Union[MetaOapg.properties.included, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["links"]) -> typing.Union['ListLinks', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", "included", "links", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, ],
        included: typing.Union[MetaOapg.properties.included, list, tuple, schemas.Unset] = schemas.unset,
        links: typing.Union['ListLinks', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonApiMetricOutList':
        return super().__new__(
            cls,
            *_args,
            data=data,
            included=included,
            links=links,
            _configuration=_configuration,
            **kwargs,
        )

from gooddata_api_client.model.json_api_metric_out_includes import JsonApiMetricOutIncludes
from gooddata_api_client.model.json_api_metric_out_with_links import JsonApiMetricOutWithLinks
from gooddata_api_client.model.list_links import ListLinks
