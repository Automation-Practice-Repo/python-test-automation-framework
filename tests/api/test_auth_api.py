"""Sample API test demonstrating REST API testing."""
import pytest
import requests


@pytest.mark.api
@pytest.mark.smoke
class TestAuthAPI:
    """Authentication API tests."""

    def test_login_success(self, api_client):
        """Test successful authentication."""
        response = api_client.post("/auth/login", json={
            "username": "admin@test.com",
            "password": "Test@123"
        })
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert "user_id" in data

    def test_login_invalid_credentials(self, api_client):
        """Test login with invalid credentials."""
        response = api_client.post("/auth/login", json={
            "username": "admin@test.com",
            "password": "wrongpassword"
        })
        assert response.status_code == 401
        data = response.json()
        assert "error" in data

    def test_get_user_profile(self, api_client):
        """Test getting user profile with auth token."""
        login_response = api_client.post("/auth/login", json={
            "username": "admin@test.com",
            "password": "Test@123"
        })
        token = login_response.json()["token"]
        api_client.set_auth_token(token)

        response = api_client.get("/users/profile")
        assert response.status_code == 200
        data = response.json()
        assert data["username"] == "admin@test.com"
        assert "email" in data


@pytest.mark.api
class TestUsersAPI:
    """Users API tests."""

    def test_list_users(self, api_client):
        """Test listing users."""
        response = api_client.get("/users", params={"page": 1, "limit": 10})
        assert response.status_code == 200
        data = response.json()
        assert "users" in data
        assert "total" in data

    def test_create_user(self, api_client):
        """Test creating a new user."""
        user_data = {
            "username": f"testuser_{pytest.timestamp}",
            "email": f"test_{pytest.timestamp}@test.com",
            "password": "Test@123"
        }
        response = api_client.post("/users", json=user_data)
        assert response.status_code == 201
        data = response.json()
        assert data["username"] == user_data["username"]

    def test_get_user_not_found(self, api_client):
        """Test getting non-existent user."""
        response = api_client.get("/users/999999")
        assert response.status_code == 404
