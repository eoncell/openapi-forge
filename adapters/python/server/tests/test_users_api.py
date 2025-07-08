# coding: utf-8

from fastapi.testclient import TestClient


from pydantic import Field, StrictStr  # noqa: F401
from typing_extensions import Annotated  # noqa: F401
from contracts.models.error import Error  # noqa: F401
from contracts.models.get_user_list200_response import GetUserList200Response  # noqa: F401
from contracts.models.logout_user200_response import LogoutUser200Response  # noqa: F401
from contracts.models.user import User  # noqa: F401
from contracts.models.user_create_request import UserCreateRequest  # noqa: F401
from contracts.models.user_update_email_request import UserUpdateEmailRequest  # noqa: F401
from contracts.models.user_update_request import UserUpdateRequest  # noqa: F401
from contracts.models.object import object  # noqa: F401


def test_create_user(client: TestClient):
    """Test case for create_user

    Create user
    """
    user_create_request = {"first_name":"John","last_name":"John","password":"SecurePassword123!","role":"BUYER","email":"user@example.com","status":"ACTIVE"}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "POST",
    #    "/v1/users",
    #    headers=headers,
    #    json=user_create_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_delete_user_by_id(client: TestClient):
    """Test case for delete_user_by_id

    Delete user
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "DELETE",
    #    "/v1/users/{userId}".format(userId='user_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_by_id(client: TestClient):
    """Test case for get_user_by_id

    Get user by ID
    """

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/users/{userId}".format(userId='user_id_example'),
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_get_user_list(client: TestClient):
    """Test case for get_user_list

    List users
    """
    params = [("users_request_payload", None)]
    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/users",
    #    headers=headers,
    #    params=params,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_user_by_id(client: TestClient):
    """Test case for update_user_by_id

    Update user
    """
    user_update_request = {"first_name":"John","last_name":"John","role":"BUYER","avatar_url":"https://example.com/avatars/user.jpg","status":"ACTIVE"}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/users/{userId}".format(userId='user_id_example'),
    #    headers=headers,
    #    json=user_update_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200


def test_update_user_email(client: TestClient):
    """Test case for update_user_email

    Update user email
    """
    user_update_email_request = {"password":"SecurePassword123!","new_email":"user@example.com"}

    headers = {
        "Authorization": "Bearer special-key",
    }
    # uncomment below to make a request
    #response = client.request(
    #    "PUT",
    #    "/v1/users/{userId}/email".format(userId='user_id_example'),
    #    headers=headers,
    #    json=user_update_email_request,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

