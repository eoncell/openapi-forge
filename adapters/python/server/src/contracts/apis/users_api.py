# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from contracts.apis.users_api_base import BaseUsersApi
import contracts.impl

from fastapi import (  # noqa: F401
    APIRouter,
    Body,
    Cookie,
    Depends,
    Form,
    Header,
    HTTPException,
    Path,
    Query,
    Response,
    Security,
    status,
)

from contracts.models.extra_models import TokenModel  # noqa: F401
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

router = APIRouter()

ns_pkg = contracts.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/v1/users",
    responses={
        201: {"model": User, "description": "User successfully created. A new user is returned."},
        400: {"model": Error, "description": "Invalid request."},
        401: {"model": Error, "description": "Unauthorized."},
        409: {"model": Error, "description": "User already exists."},
    },
    tags=["Users"],
    summary="Create user",
    response_model_by_alias=True,
)
async def create_user(
    user_create_request: UserCreateRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> User:
    """Create a new user (admin only)"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().create_user(user_create_request)


@router.delete(
    "/v1/users/{userId}",
    responses={
        200: {"model": LogoutUser200Response, "description": "User deleted successfully"},
        400: {"model": Error, "description": "Invalid request."},
        401: {"model": Error, "description": "Unauthorized."},
        404: {"model": Error, "description": "User not found."},
    },
    tags=["Users"],
    summary="Delete user",
    response_model_by_alias=True,
)
async def delete_user_by_id(
    userId: Annotated[StrictStr, Field(description="User unique identifier")] = Path(..., description="User unique identifier"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> LogoutUser200Response:
    """Delete a specific user"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().delete_user_by_id(userId)


@router.get(
    "/v1/users/{userId}",
    responses={
        200: {"model": User, "description": "User retrieved successfully"},
        400: {"model": Error, "description": "Invalid request."},
        401: {"model": Error, "description": "Unauthorized."},
        404: {"model": Error, "description": "User not found."},
    },
    tags=["Users"],
    summary="Get user by ID",
    response_model_by_alias=True,
)
async def get_user_by_id(
    userId: Annotated[StrictStr, Field(description="User unique identifier")] = Path(..., description="User unique identifier"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> User:
    """Retrieve a specific user by their ID"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().get_user_by_id(userId)


@router.get(
    "/v1/users",
    responses={
        200: {"model": GetUserList200Response, "description": "Successful retrieval of users."},
        400: {"model": Error, "description": "Invalid request."},
        401: {"model": Error, "description": "Unauthorized."},
    },
    tags=["Users"],
    summary="List users",
    response_model_by_alias=True,
)
async def get_user_list(
    users_request_payload: Annotated[object, Field(description="Filter, sort and pagination query to fetch records.")] = Query(None, description="Filter, sort and pagination query to fetch records.", alias="UsersRequestPayload"),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> GetUserList200Response:
    """Get users based on provided filters, sorting and pagination parameters."""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().get_user_list(users_request_payload)


@router.put(
    "/v1/users/{userId}",
    responses={
        200: {"model": User, "description": "User updated successfully"},
        400: {"model": Error, "description": "Invalid request."},
        401: {"model": Error, "description": "Unauthorized."},
        404: {"model": Error, "description": "User not found."},
    },
    tags=["Users"],
    summary="Update user",
    response_model_by_alias=True,
)
async def update_user_by_id(
    userId: Annotated[StrictStr, Field(description="User unique identifier")] = Path(..., description="User unique identifier"),
    user_update_request: UserUpdateRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> User:
    """Update a specific user&#39;s information"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().update_user_by_id(userId, user_update_request)


@router.put(
    "/v1/users/{userId}/email",
    responses={
        200: {"model": User, "description": "User email updated successfully"},
        400: {"model": Error, "description": "Invalid request"},
        401: {"model": Error, "description": "Unauthorized"},
        403: {"model": Error, "description": "Access denied"},
        404: {"model": Error, "description": "User not found"},
    },
    tags=["Users"],
    summary="Update user email",
    response_model_by_alias=True,
)
async def update_user_email(
    userId: Annotated[StrictStr, Field(description="User unique identifier")] = Path(..., description="User unique identifier"),
    user_update_email_request: UserUpdateEmailRequest = Body(None, description=""),
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> User:
    """Update user email address (requires password confirmation)"""
    if not BaseUsersApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseUsersApi.subclasses[0]().update_user_email(userId, user_update_email_request)
