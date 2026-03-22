from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from .database import db

async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    async with db.async_session_maker() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()