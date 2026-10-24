from idlelib import query
from xml.dom import ValidationErr

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_
from db.models import users
import sqlalchemy as sa
class userOperations:
    def __init__(self, dbsession: AsyncSession) -> None :
        self.dbsession = dbsession

    async def creat(self, username:str, password:str) -> users :
        user= users(username=username, password=password)
        async with self.dbsession as session:
            session.add(user)
        return user
    async def get_user_by_username(self, username:str) -> users :
        query = sa.select([users]).where(users.username == username)
        async with self.dbsession as session:
            user_data= session.scalar(query)
            if user_data is None:
                raise ValidationErr ("USER NOT FOUND")
            return user_data



