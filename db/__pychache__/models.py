from sqlalchemy.orm import Mapped, MappedColumn
from .engine import Base

class users(Base):
    __tablename__ = 'users'
    username: Mapped[str] = MappedColumn(unique=True, default=None)
    password: Mapped[str] = MappedColumn(default=None)
