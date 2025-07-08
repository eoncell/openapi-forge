# coding: utf-8

from fastapi.testclient import TestClient


from contracts.models.error import Error  # noqa: F401
from contracts.models.get_health_status200_response import GetHealthStatus200Response  # noqa: F401


def test_get_health_status(client: TestClient):
    """Test case for get_health_status

    Health check
    """

    headers = {
    }
    # uncomment below to make a request
    #response = client.request(
    #    "GET",
    #    "/v1/health",
    #    headers=headers,
    #)

    # uncomment below to assert the status code of the HTTP response
    #assert response.status_code == 200

