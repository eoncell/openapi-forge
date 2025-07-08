# coding: utf-8

from typing import ClassVar, Dict, List, Tuple  # noqa: F401

from contracts.models.auth_request_payload import AuthRequestPayload
from contracts.models.auth_token_refresh_request_payload import AuthTokenRefreshRequestPayload
from contracts.models.authenticate_user200_response import AuthenticateUser200Response
from contracts.models.error import Error
from contracts.models.logout_user200_response import LogoutUser200Response
from contracts.models.register_request_payload import RegisterRequestPayload
from contracts.models.token_response import TokenResponse
from contracts.security_api import get_token_bearerAuth

class BaseAuthenticationApi:
    subclasses: ClassVar[Tuple] = ()

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        BaseAuthenticationApi.subclasses = BaseAuthenticationApi.subclasses + (cls,)
    async def authenticate_user(
        self,
        auth_request_payload: AuthRequestPayload,
    ) -> AuthenticateUser200Response:
        """Authenticate a user with email/username and password. Returns JWT tokens for subsequent API calls. """
        ...


    async def logout_user(
        self,
    ) -> LogoutUser200Response:
        """Logout user and invalidate tokens"""
        ...


    async def refresh_tokens(
        self,
        auth_token_refresh_request_payload: AuthTokenRefreshRequestPayload,
    ) -> TokenResponse:
        """Refresh access token using refresh token. Returns new JWT tokens. """
        ...


    async def register_user(
        self,
        register_request_payload: RegisterRequestPayload,
    ) -> AuthenticateUser200Response:
        """Create a new user account"""
        ...
