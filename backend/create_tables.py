import asyncio
from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import create_async_engine
from db.database import Base, db
from models.task import Task

async def init_tables(engine):

    async with engine.begin() as conn:
        def sync_inspect(connection):
            inspector = inspect(connection)
            return inspector.get_table_names()

        existing_tables = await conn.run_sync(sync_inspect)

        if not existing_tables:
            await conn.run_sync(Base.metadata.create_all)
            print("Таблицы созданы")
        else:
            print(f"Таблицы уже существуют: {existing_tables}")

    await engine.dispose()


async def run_init():
    try:
        await db.init()
        await init_tables(db.engine)
    except Exception as e:
        raise
    finally:
        await db.close()

if __name__ == "__main__":
    asyncio.run(run_init())