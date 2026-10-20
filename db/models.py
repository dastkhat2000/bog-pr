
from sqlalchemy.orm import Mapped, MappedColumn
from db.engine import Base
class users(Base):
    __tablename__ = "users"
    id : Mapped[int]= MappedColumn(primary_key=True)
    password: Mapped[str] = MappedColumn()
    username: Mapped[str] = MappedColumn(unique=True, default=None, nullable=False)
    email: Mapped[str] = MappedColumn()
