from sqlalchemy.ext.asyncio import AsyncSession
from db.models import user
class userOperations:
    def __init__(self, dbsession: AsyncSession) -> None
        self.dbsession = dbsession

    def creat(self, username:str,password:str) -> user
        user= user(username=username, password=password)


