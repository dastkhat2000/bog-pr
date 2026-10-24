from uuid import UUID, uuid4

from sqlalchemy.orm import Mapped, MappedColumn
from db.engine import Base
class users(Base):
    __tablename__ = "users"
    password: Mapped[str] = MappedColumn()
    id : Mapped[UUID]= MappedColumn(primary_key=True, default_factory=uuid4)
    username: Mapped[str] = MappedColumn(unique=True)
    email: Mapped[str] = MappedColumn()
