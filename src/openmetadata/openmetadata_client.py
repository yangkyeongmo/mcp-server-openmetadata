"""Centralized OpenMetadata REST API client configuration.

This module provides the core OpenMetadata client with authentication handling,
HTTP session management, and base methods for CRUD operations on metadata entities.
"""

from typing import Any, Dict, Optional
from urllib.parse import urljoin

import httpx

# Global client instance
_client: Optional["OpenMetadataClient"] = None


class OpenMetadataError(Exception):
    """Base exception for OpenMetadata client errors."""

    pass


def get_client() -> "OpenMetadataClient":
    """Get the global OpenMetadata client instance.

    Returns:
        The initialized OpenMetadata client

    Raises:
        RuntimeError: If client has not been initialized
    """
    if _client is None:
        raise RuntimeError("OpenMetadata client not initialized. Call initialize_client() first.")
    return _client


def initialize_client(
    host: str, api_token: Optional[str] = None, username: Optional[str] = None, password: Optional[str] = None
) -> None:
    """Initialize the global OpenMetadata client.

    Args:
        host: OpenMetadata host URL
        api_token: JWT token for API authentication
        username: Username for basic authentication
        password: Password for basic authentication

    Raises:
        OpenMetadataError: If neither API token nor username/password is provided
    """
    global _client
    _client = OpenMetadataClient(host, api_token, username, password)


class OpenMetadataClient:
    """Client for interacting with OpenMetadata API.

    Provides centralized authentication handling, HTTP session management,
    and error handling for all OpenMetadata API operations.
    """

    def __init__(
        self, host: str, api_token: Optional[str] = None, username: Optional[str] = None, password: Optional[str] = None
    ):
        """Initialize OpenMetadata client.

        Args:
            host: OpenMetadata host URL
            api_token: JWT token for API authentication
            username: Username for basic authentication
            password: Password for basic authentication

        Raises:
            OpenMetadataError: If neither API token nor username/password is provided
        """
        self.host = host.rstrip("/")
        self.base_url = urljoin(self.host, "/api/v1/")
        self.session = httpx.Client()

        # Set up authentication
        if api_token:
            self.session.headers["Authorization"] = f"Bearer {api_token}"
        elif username and password:
            # Basic auth implementation would go here if needed
            # For now, OpenMetadata primarily uses JWT tokens
            pass
        else:
            raise OpenMetadataError("Either API token or username/password must be provided")

    def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make HTTP request to OpenMetadata API.

        Args:
            method: HTTP method (GET, POST, PUT, DELETE)
            endpoint: API endpoint path
            params: Query parameters
            json_data: JSON payload for POST/PUT requests

        Returns:
            API response as dictionary

        Raises:
            OpenMetadataError: If the API request fails
        """
        url = urljoin(self.base_url, endpoint)

        try:
            response = self.session.request(method=method, url=url, params=params, json=json_data)
            response.raise_for_status()
            return response.json() if response.content else {}
        except httpx.HTTPStatusError as e:
            raise OpenMetadataError(f"HTTP {e.response.status_code}: {e.response.text}") from e
        except httpx.RequestError as e:
            raise OpenMetadataError(f"Request failed: {str(e)}") from e

    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Make GET request to OpenMetadata API."""
        return self._make_request("GET", endpoint, params=params)

    def post(self, endpoint: str, json_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make POST request to OpenMetadata API."""
        return self._make_request("POST", endpoint, json_data=json_data)

    def put(self, endpoint: str, json_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make PUT request to OpenMetadata API."""
        return self._make_request("PUT", endpoint, json_data=json_data)

    def patch(self, endpoint: str, json_data: Dict[str, Any]) -> Dict[str, Any]:
        """Make PATCH request to OpenMetadata API."""
        return self._make_request("PATCH", endpoint, json_data=json_data)

    def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> None:
        """Make DELETE request to OpenMetadata API."""
        self._make_request("DELETE", endpoint, params=params)

    def close(self) -> None:
        """Close the HTTP session."""
        self.session.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
