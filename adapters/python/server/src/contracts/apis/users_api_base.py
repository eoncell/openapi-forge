# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from contracts.models.error import Error
from contracts.models.get_user_list200_response import GetUserList200Response
from contracts.models.logout_user200_response import LogoutUser200Response
from contracts.models.user import User
from contracts.models.user_create_request import UserCreateRequest
from contracts.models.user_update_email_request import UserUpdateEmailRequest
from contracts.models.user_update_request import UserUpdateRequest
from contracts.models.object import object
from contracts.security_api import get_token_bearerAuth

class BaseUsersApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseUsersApi.subclasses = BaseUsersApi.subclasses + (cls,)
    async def create_user(
        self,
        user_create_request: UserCreateRequest,
    ) -> User:
        """Create a new user (admin only)"""
        ...


    async def delete_user_by_id(
        self,
        userId: Annotated[StrictStr, Field(description="User unique identifier")],
    ) -> LogoutUser200Response:
        """Delete a specific user"""
        ...


    async def get_user_by_id(
        self,
        userId: Annotated[StrictStr, Field(description="User unique identifier")],
    ) -> User:
        """Retrieve a specific user by their ID"""
        ...


    async def get_user_list(
        self,
        users_request_payload: Annotated[object, Field(description="Filter, sort and pagination query to fetch records.")],
    ) -> GetUserList200Response:
        """Get users based on provided filters, sorting and pagination parameters."""
        ...


    async def update_user_by_id(
        self,
        userId: Annotated[StrictStr, Field(description="User unique identifier")],
        user_update_request: UserUpdateRequest,
    ) -> User:
        """Update a specific user&#39;s information"""
        ...


    async def update_user_email(
        self,
        userId: Annotated[StrictStr, Field(description="User unique identifier")],
        user_update_email_request: UserUpdateEmailRequest,
    ) -> User:
        """Update user email address (requires password confirmation)"""
        ...
