"""API client for REST API testing."""
import requests
from typing import Dict, Optional, Any
import logging

logger = logging.getLogger(__name__)


class APIClient:
    """HTTP API client with session management."""

    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

    def set_auth_token(self, token: str) -> None:
        """Set authorization token."""
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def clear_auth(self) -> None:
        """Clear authorization headers."""
        if "Authorization" in self.session.headers:
            del self.session.headers["Authorization"]

    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send GET request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        response = self.session.get(url, params=params, timeout=self.timeout, **kwargs)
        logger.info(f"Status: {response.status_code}")
        return response

    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send POST request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        response = self.session.post(url, data=data, json=json, timeout=self.timeout, **kwargs)
        logger.info(f"Status: {response.status_code}")
        return response

    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send PUT request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PUT {url}")
        response = self.session.put(url, data=data, json=json, timeout=self.timeout, **kwargs)
        logger.info(f"Status: {response.status_code}")
        return response

    def patch(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """Send PATCH request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"PATCH {url}")
        response = self.session.patch(url, data=data, json=json, timeout=self.timeout, **kwargs)
        logger.info(f"Status: {response.status_code}")
        return response

    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """Send DELETE request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"DELETE {url}")
        response = self.session.delete(url, timeout=self.timeout, **kwargs)
        logger.info(f"Status: {response.status_code}")
        return response

    def close(self) -> None:
        """Close the session."""
        self.session.close()
