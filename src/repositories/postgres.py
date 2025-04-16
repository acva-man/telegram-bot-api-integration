from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from typing import List, Dict, Any
from ..models.db_models import User
from .base import BaseRepository

class PostgresRepository(BaseRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save_users(self, users: List[Dict[str, Any]]):
        """Сохраняет пользователей в PostgreSQL"""
        if not users:
            return
            
        stmt = insert(User).values(users)
        await self.session.execute(stmt)
        await self.session.commit()
