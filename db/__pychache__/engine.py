from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


SQLALCHEMY_DATABASE_URL = "sqlite+aiosqlite:///./blog.db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

sessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass


# Base = DeclarativeBase()   # این خط کلاس Base بالا را خراب می‌کند، پس کامنت شد


async def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        await db.close()