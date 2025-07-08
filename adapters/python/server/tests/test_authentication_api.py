# coding: utf-8

from fastapi.testclient import TestClient


from contracts.models.auth_request_payload import AuthRequestPayload  # noqa: F401
from contracts.models.auth_token_refresh_request_payload import AuthTokenRefreshRequestPayload  # noqa: F401
from contracts.models.authenticate_user200_response import AuthenticateUser200Response  # noqa: F401
from contracts.models.error import Error  # noqa: F401
from contracts.models.logout_user200_response import LogoutUser200Response  # noqa: F401
from contracts.models.register_request_payload import RegisterRequestPayload  # noqa: F401
from contracts.models.token_response import TokenResponse  # noqa: F401


def test_authenticate_user(client: TestClient):
    """Test case for authenticate_user

    User login
    """
    auth_request_payload = {"password":"SecurePassword123!","is_remember_me":0,"email":"user@example.com"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/auth/login",
    #    headers=headers,
    #    json=auth_request_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_logout_user(client: TestClient):
    """Test case for logout_user

    User logout
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/auth/logout",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_refresh_tokens(client: TestClient):
    """Test case for refresh_tokens

    Refresh tokens
    """
    auth_token_refresh_request_payload = {"refresh_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/auth/refresh",
    #    headers=headers,
    #    json=auth_token_refresh_request_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_register_user(client: TestClient):
    """Test case for register_user

    Register new user
    """
    register_request_payload = {"first_name":"John","last_name":"John","password":"SecurePassword123!","email":"user@example.com"}

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/auth/register",
    #    headers=headers,
    #    json=register_request_payload,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

