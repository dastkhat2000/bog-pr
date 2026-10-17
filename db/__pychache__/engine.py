from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass


SQLALCHAMY_DATABASE_URI = "sqlite+aiosqlite:///:blog.db:"

engine = create_async_engine(SQLALCHAMY_DATABASE_URL)

sessionLocal = async_sessionmaker (
    bind = engine,
    autocommit = False,
    autoflush = False,
)
class Base(DeclarativeBase, MappedAsDataclass):
    pass

Base = declarative_base()
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
