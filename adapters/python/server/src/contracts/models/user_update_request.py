# coding: utf-8

"""
    Contracts Blueprint API

    # Contracts Blueprint API  A simple API blueprint demonstrating enterprise-grade OpenAPI specifications with multi-language code generation support for Go, Python, and TypeScript.  This API provides basic authentication and user management functionality.  ## Features - JWT-based authentication - User CRUD operations - Multi-language SDK generation - Comprehensive error handling  ## Error Codes - `ERR_INTERNAL`: Internal server error - `ERR_INVALID_ARG`: Invalid argument(s) provided - `ERR_NOT_FOUND`: Resource not found - `ERR_ALREADY_EXISTS`: Resource already exists - `ERR_ACCESS_DENIED`: Access denied - `ERR_INVALID_CREDENTIALS`: Invalid authentication credentials - `ERR_VALIDATION_FAILED`: Request validation failed 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json




from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from contracts.models.user_role import UserRole
from contracts.models.user_status import UserStatus
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UserUpdateRequest(BaseModel):
    """
    Request payload for updating user information
    """ # noqa: E501
    first_name: Optional[Annotated[str, Field(strict=True)]] = Field(default='', description="Name (either first name or last name) of the user.", alias="firstName")
    last_name: Optional[Annotated[str, Field(strict=True)]] = Field(default='', description="Name (either first name or last name) of the user.", alias="lastName")
    role: Optional[UserRole] = None
    status: Optional[UserStatus] = None
    avatar_url: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, description="User avatar URL", alias="avatarUrl")
    __properties: ClassVar[List[str]] = ["firstName", "lastName", "role", "status", "avatarUrl"]

    @field_validator('first_name')
    def first_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    @field_validator('last_name')
    def last_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^.{0,50}$", value):
            raise ValueError(r"must validate the regular expression /^.{0,50}$/")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UserUpdateRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # set to None if avatar_url (nullable) is None
        # and model_fields_set contains the field
        if self.avatar_url is None and "avatar_url" in self.model_fields_set:
            _dict['avatarUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UserUpdateRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firstName": obj.get("firstName") if obj.get("firstName") is not None else '',
            "lastName": obj.get("lastName") if obj.get("lastName") is not None else '',
            "role": obj.get("role"),
            "status": obj.get("status"),
            "avatarUrl": obj.get("avatarUrl")
        })
        return _obj


