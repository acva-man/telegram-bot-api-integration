from typing import List
from ..schemas.api_schemas import UserSchema
from ..repositories.postgres import PostgresRepository
from ..repositories.google_sheets import GoogleSheetsRepository

class DataService:
    """Service for processing and saving data"""
    
    def __init__(self, postgres_repo: PostgresRepository, google_sheets_repo: GoogleSheetsRepository):
        self.postgres_repo = postgres_repo
        self.google_sheets_repo = google_sheets_repo
    
    async def save_users(self, users: List[UserSchema]):
        """Save users to both PostgreSQL and Google Sheets"""
        users_dicts = [user.dict() for user in users]
        
        await self.postgres_repo.save_users(users_dicts)
        await self.google_sheets_repo.save_users(users_dicts)
