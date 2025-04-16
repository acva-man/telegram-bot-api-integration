from injectable import injectable, Autowired, autowired
from sqlalchemy.ext.asyncio import AsyncSession
from aiohttp import ClientSession
from .repositories.postgres import PostgresRepository
from .repositories.google_sheets import GoogleSheetsRepository
from .services.api_service import APIService
from .services.data_service import DataService

@injectable
class DIContainer:
    @autowired
    def __init__(
        self,
        db_session: Autowired(AsyncSession),
        http_client: Autowired(ClientSession),
        postgres_repo: Autowired(PostgresRepository),
        google_sheets_repo: Autowired(GoogleSheetsRepository),
        api_service: Autowired(APIService),
        data_service: Autowired(DataService),
    ):
        self.db_session = db_session
        self.http_client = http_client
        self.postgres_repo = postgres_repo
        self.google_sheets_repo = google_sheets_repo
        self.api_service = api_service
        self.data_service = data_service
