from idlelib import query
from xml.dom import ValidationErr

from pydantic_core.core_schema import none_schema
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import await_
from db.models import users
import sqlalchemy as sa
class userOperations:
    def __init__(self, dbsession: AsyncSession) -> None :
        self.dbsession = dbsession


    async def create(self, username:str, password:str) -> users :
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

    async def update_username(self, old_username:str, new_username: str ) -> users :
        query = sa.select([users]).where(users.username == old_username)
        update_query = sa.update(users).where(users.username == old_username).values(username=new_username)
        async with self.dbsession as session:
            user_data=await session.scalar(query)

            if user_data is None:
                raise ValidationErr("USER NOT FOUND")
            await session.execute(update_query)
            user_data.username=new_username
            return user_data

    async def user_delete_account(self, username:str, password: str ) -> users :
        delete_query = sa.select([users]).where(users.username == username, password==password)
        async with self.dbsession as session:
         delete_query = sa.delete(users).where(users.username == username)
        async with self.dbsession as session:
            user_data= await session.execute(query)
            await session.execute(delete_query)
            await session.commit()






