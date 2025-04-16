from aiohttp import ClientSession
from typing import List
from ..schemas.api_schemas import UserSchema

class APIService:
    """Service for interacting with JSON Placeholder API"""
    
    def __init__(self, http_client: ClientSession):
        self.http_client = http_client
        self.base_url = "https://jsonplaceholder.typicode.com"
    
    async def get_users(self) -> List[UserSchema]:
        """
        Fetch users from API and validate response
        
        Returns:
            List of validated user data in snake_case format
            
        Raises:
            ValueError: If API request fails or data is invalid
        """
        async with self.http_client.get(f"{self.base_url}/users") as response:
            if response.status != 200:
                raise ValueError("Failed to fetch users from API")
            
            data = await response.json()
            return [UserSchema(**user) for user in data]
