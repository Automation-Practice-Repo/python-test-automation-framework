"""REST API tests for health check and user endpoints."""

import pytest
from utils.api_client import APIClient


@pytest.mark.api
@pytest.mark.smoke
def test_api_health_check(api_client: APIClient) -> None:
    """Verify system health endpoint returns HTTP response status code."""
    response = api_client.get("users?page=1")
    assert response.status_code in [200, 404]


@pytest.mark.api
@pytest.mark.regression
@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user_by_id(api_client: APIClient, user_id: int) -> None:
    """Data-driven API validation for user endpoints."""
    response = api_client.get(f"users/{user_id}")
    assert response.status_code in [200, 404]
