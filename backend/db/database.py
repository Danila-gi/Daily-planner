from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from settings.config import settings


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True


class Database:
    def __init__(self):
        self.engine = None
        self.async_session_maker = None

    async def init(self):
        DATABASE_URL = settings.get_db_url()
        self.engine = create_async_engine(
            url=DATABASE_URL,
            echo=True
        )
        self.async_session_maker = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            class_=AsyncSession
        )

    async def close(self):
        if self.engine:
            await self.engine.dispose()


db = Database()