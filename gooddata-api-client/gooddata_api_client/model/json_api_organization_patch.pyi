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


class JsonApiOrganizationPatch(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    JSON:API representation of patching organization entity.
    """


    class MetaOapg:
        required = {
            "id",
            "type",
        }
        
        class properties:
            
            
            class id(
                schemas.StrSchema
            ):
                pass
            
            
            class type(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def ORGANIZATION(cls):
                    return cls("organization")
            
            
            class attributes(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        
                        
                        class allowedOrigins(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'allowedOrigins':
                                return super().__new__(
                                    cls,
                                    _arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        
                        
                        class earlyAccess(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class hostname(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class name(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class oauthClientId(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class oauthClientSecret(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class oauthIssuerId(
                            schemas.StrSchema
                        ):
                            pass
                        
                        
                        class oauthIssuerLocation(
                            schemas.StrSchema
                        ):
                            pass
                        __annotations__ = {
                            "allowedOrigins": allowedOrigins,
                            "earlyAccess": earlyAccess,
                            "hostname": hostname,
                            "name": name,
                            "oauthClientId": oauthClientId,
                            "oauthClientSecret": oauthClientSecret,
                            "oauthIssuerId": oauthIssuerId,
                            "oauthIssuerLocation": oauthIssuerLocation,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["allowedOrigins"]) -> MetaOapg.properties.allowedOrigins: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["earlyAccess"]) -> MetaOapg.properties.earlyAccess: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["hostname"]) -> MetaOapg.properties.hostname: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["oauthClientId"]) -> MetaOapg.properties.oauthClientId: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["oauthClientSecret"]) -> MetaOapg.properties.oauthClientSecret: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["oauthIssuerId"]) -> MetaOapg.properties.oauthIssuerId: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["oauthIssuerLocation"]) -> MetaOapg.properties.oauthIssuerLocation: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["allowedOrigins", "earlyAccess", "hostname", "name", "oauthClientId", "oauthClientSecret", "oauthIssuerId", "oauthIssuerLocation", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["allowedOrigins"]) -> typing.Union[MetaOapg.properties.allowedOrigins, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["earlyAccess"]) -> typing.Union[MetaOapg.properties.earlyAccess, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["hostname"]) -> typing.Union[MetaOapg.properties.hostname, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["oauthClientId"]) -> typing.Union[MetaOapg.properties.oauthClientId, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["oauthClientSecret"]) -> typing.Union[MetaOapg.properties.oauthClientSecret, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["oauthIssuerId"]) -> typing.Union[MetaOapg.properties.oauthIssuerId, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["oauthIssuerLocation"]) -> typing.Union[MetaOapg.properties.oauthIssuerLocation, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["allowedOrigins", "earlyAccess", "hostname", "name", "oauthClientId", "oauthClientSecret", "oauthIssuerId", "oauthIssuerLocation", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, ],
                    allowedOrigins: typing.Union[MetaOapg.properties.allowedOrigins, list, tuple, schemas.Unset] = schemas.unset,
                    earlyAccess: typing.Union[MetaOapg.properties.earlyAccess, str, schemas.Unset] = schemas.unset,
                    hostname: typing.Union[MetaOapg.properties.hostname, str, schemas.Unset] = schemas.unset,
                    name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
                    oauthClientId: typing.Union[MetaOapg.properties.oauthClientId, str, schemas.Unset] = schemas.unset,
                    oauthClientSecret: typing.Union[MetaOapg.properties.oauthClientSecret, str, schemas.Unset] = schemas.unset,
                    oauthIssuerId: typing.Union[MetaOapg.properties.oauthIssuerId, str, schemas.Unset] = schemas.unset,
                    oauthIssuerLocation: typing.Union[MetaOapg.properties.oauthIssuerLocation, str, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        *_args,
                        allowedOrigins=allowedOrigins,
                        earlyAccess=earlyAccess,
                        hostname=hostname,
                        name=name,
                        oauthClientId=oauthClientId,
                        oauthClientSecret=oauthClientSecret,
                        oauthIssuerId=oauthIssuerId,
                        oauthIssuerLocation=oauthIssuerLocation,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "id": id,
                "type": type,
                "attributes": attributes,
            }
    
    id: MetaOapg.properties.id
    type: MetaOapg.properties.type
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "type", "attributes", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> MetaOapg.properties.type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> typing.Union[MetaOapg.properties.attributes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "type", "attributes", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, ],
        type: typing.Union[MetaOapg.properties.type, str, ],
        attributes: typing.Union[MetaOapg.properties.attributes, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'JsonApiOrganizationPatch':
        return super().__new__(
            cls,
            *_args,
            id=id,
            type=type,
            attributes=attributes,
            _configuration=_configuration,
            **kwargs,
        )
