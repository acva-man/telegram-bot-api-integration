from abc import ABC, abstractmethod
from typing import List, Dict, Any

class BaseRepository(ABC):
    @abstractmethod
    async def save_users(self, users: List[Dict[str, Any]]):
        pass
