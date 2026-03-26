from .base import CurrencyCloudProvider
import httpx
from fastapi import HTTPException
from typing import Dict, Optional

class CurrencyCloudAuthorizationManagerProvider(CurrencyCloudProvider):
    """
    This provider will handle all the actions related with the authorization
    Rotating access_tokens etc
    """
    def __init__(self):
        super().__init__()
    
    @staticmethod
    async def login(login_id: str, api_key: str):
        instance = CurrencyCloudAuthorizationManagerProvider()
        """
        This is the login method

        Args:
            login_id (str): This is your email registered on the currency cloud platform
            api_key (str): This is the api key you get after creating account
            
            These arguments must be provided
        """
        response = await instance.initialize("POST","authenticate/api", data={"login_id": login_id, "api_key": api_key})
        
        return response.json()


    @staticmethod
    def extract_auth_token(response: dict) -> str:
        """
        Extracts the auth token from the login response
        and prepares it for use in headers.

        Args:
            response (dict): raw response from login()

        Returns:
            str: auth token string
        """
        if not response or "auth_token" not in response:
            raise ValueError("Auth token not found in response")
        return response["auth_token"]

    @staticmethod
    def prepare_headers(auth_token: str) -> dict:
        """
        Prepares headers for Currency Cloud API calls.

        Args:
            auth_token (str): token extracted from login

        Returns:
            dict: headers including X-Auth-Token
        """
        return {
            "X-Auth-Token": auth_token,
            "Content-Type": "application/json",
        }






class CurrencyCloudClient(CurrencyCloudProvider):
    """
    Helper class to interact with Currency Cloud API.
    Handles login, token management, HTTP requests, and automatic error handling.
    """

    def __init__(self, login_id: str, api_key: str, base_url: str):
        super().__init__()
        self.login_id = login_id
        self.api_key = api_key
        self.base_url = base_url
        self.auth_token: Optional[str] = None

    async def authenticate(self):
        """
        Logs in and stores the auth token internally.
        """
        response = await CurrencyCloudAuthorizationManagerProvider.login(
            login_id=self.login_id,
            api_key=self.api_key
        )
        self.auth_token = CurrencyCloudAuthorizationManagerProvider.extract_auth_token(response)

    def get_headers(self) -> Dict[str, str]:
        """
        Returns headers for requests, including the auth token.
        """
        if not self.auth_token:
            raise HTTPException(status_code=401, detail="Client not authenticated. Call `authenticate()` first.")
        return CurrencyCloudAuthorizationManagerProvider.prepare_headers(self.auth_token)

    async def post(self, path: str, data: dict | None = None, timeout: int = 10) -> dict:
        """
        Makes a POST request with automatic error handling.
        Returns JSON or raises HTTPException on failure.
        """
        url = f"{self.base_url}/{path}"
        async with httpx.AsyncClient(timeout=timeout) as client:
            try:
                response = await client.post(url, json=data, headers=self.get_headers())
                response.raise_for_status()
                
                return response.json()
            except httpx.HTTPStatusError as e:
                try:
                    detail = e.response.json()
                except Exception:
                    detail = e.response.text
                raise HTTPException(status_code=e.response.status_code, detail=detail)
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=f"Currency Cloud request failed: {str(e)}")

    async def get(self, path: str, params: dict | None = None, timeout: int = 10) -> dict:
        """
        Makes a GET request with automatic error handling.
        Returns JSON or raises HTTPException on failure.
        """
        url = f"{self.base_url}/{path}"
        async with httpx.AsyncClient(timeout=timeout) as client:
            try:
                response = await client.get(url, params=params, headers=self.get_headers())
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                try:
                    detail = e.response.json()
                except Exception:
                    detail = e.response.text
                raise HTTPException(status_code=e.response.status_code, detail=detail)
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=f"Currency Cloud request failed: {str(e)}")


