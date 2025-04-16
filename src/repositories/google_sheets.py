import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any
from .base import BaseRepository

class GoogleSheetsRepository(BaseRepository):
    def __init__(self, credentials_path: str, sheet_id: str):
        scope = ['https://www.googleapis.com/auth/spreadsheets']
        creds = Credentials.from_service_account_file(credentials_path, scopes=scope)
        self.client = gspread.authorize(creds)
        self.sheet = self.client.open_by_key(sheet_id).sheet1

    async def save_users(self, users: List[Dict[str, Any]]):
        """Сохраняет пользователей в Google Sheets"""
        if not users:
            return
            
        headers = list(users[0].keys())
        values = [list(user.values()) for user in users]
        
        self.sheet.clear()
        self.sheet.append_row(headers)
        self.sheet.append_rows(values)
