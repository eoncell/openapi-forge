# coding: utf-8

from typing import Dict, List  # noqa: F401
import importlib
import pkgutil

from contracts.apis.authentication_api_base import BaseAuthenticationApi
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
from contracts.models.auth_request_payload import AuthRequestPayload
from contracts.models.auth_token_refresh_request_payload import AuthTokenRefreshRequestPayload
from contracts.models.authenticate_user200_response import AuthenticateUser200Response
from contracts.models.error import Error
from contracts.models.logout_user200_response import LogoutUser200Response
from contracts.models.register_request_payload import RegisterRequestPayload
from contracts.models.token_response import TokenResponse
from contracts.security_api import get_token_bearerAuth

router = APIRouter()

ns_pkg = contracts.impl
for _, name, _ in pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + "."):
    importlib.import_module(name)


@router.post(
    "/v1/auth/login",
    responses={
        200: {"model": AuthenticateUser200Response, "description": "Login successful"},
        400: {"model": Error, "description": "Invalid request"},
        401: {"model": Error, "description": "Invalid credentials"},
    },
    tags=["Authentication"],
    summary="User login",
    response_model_by_alias=True,
)
async def authenticate_user(
    auth_request_payload: AuthRequestPayload = Body(None, description=""),
) -> AuthenticateUser200Response:
    """Authenticate a user with email/username and password. Returns JWT tokens for subsequent API calls. """
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().authenticate_user(auth_request_payload)


@router.post(
    "/v1/auth/logout",
    responses={
        200: {"model": LogoutUser200Response, "description": "Logout successful"},
        401: {"model": Error, "description": "Unauthorized"},
    },
    tags=["Authentication"],
    summary="User logout",
    response_model_by_alias=True,
)
async def logout_user(
    token_bearerAuth: TokenModel = Security(
        get_token_bearerAuth
    ),
) -> LogoutUser200Response:
    """Logout user and invalidate tokens"""
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().logout_user()


@router.post(
    "/v1/auth/refresh",
    responses={
        200: {"model": TokenResponse, "description": "Token refreshed successfully"},
        400: {"model": Error, "description": "Invalid request"},
        401: {"model": Error, "description": "Invalid refresh token"},
    },
    tags=["Authentication"],
    summary="Refresh tokens",
    response_model_by_alias=True,
)
async def refresh_tokens(
    auth_token_refresh_request_payload: AuthTokenRefreshRequestPayload = Body(None, description=""),
) -> TokenResponse:
    """Refresh access token using refresh token. Returns new JWT tokens. """
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().refresh_tokens(auth_token_refresh_request_payload)


@router.post(
    "/v1/auth/register",
    responses={
        201: {"model": AuthenticateUser200Response, "description": "User registered successfully"},
        400: {"model": Error, "description": "Invalid request"},
        409: {"model": Error, "description": "User already exists"},
    },
    tags=["Authentication"],
    summary="Register new user",
    response_model_by_alias=True,
)
async def register_user(
    register_request_payload: RegisterRequestPayload = Body(None, description=""),
) -> AuthenticateUser200Response:
    """Create a new user account"""
    if not BaseAuthenticationApi.subclasses:
        raise HTTPException(status_code=500, detail="Not implemented")
    return await BaseAuthenticationApi.subclasses[0]().register_user(register_request_payload)
