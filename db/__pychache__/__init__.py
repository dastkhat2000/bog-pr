from .engine import Base
from .models import users
__all__ = [
    "Base",
    "users"
           ]
Base.metadata.create_all(bind=engine)
