from fastapi import HTTPException
from sqlalchemy import select, delete, update
from sqlalchemy.ext.asyncio import AsyncSession

from db.models import users
from exeptions import NotFoundException
from utils.secrets import password_manager


class userOperations:
    def __init__(self, dbsession: AsyncSession) -> None:
        self.dbsession = dbsession

    async def create(self, username: str, password: str):
        hashed_password = password_manager.hash(password)
        user = users(username=username, password=hashed_password)
        async with self.dbsession as session:
            session.add(user)
            await session.commit()
            await session.refresh(user)
        return user

    async def get_user_by_username(self, username: str):
        query = select(users).where(users.username == username)
        async with self.dbsession as session:
            result = await session.execute(query)
            user_data = result.scalar_one_or_none()
            if user_data is None:
                raise NotFoundException
            return user_data

    async def update_username(self, old_username: str, new_username: str):
        select_query = select(users).where(users.username == old_username)
        update_query = (
            update(users)
            .where(users.username == old_username)
            .values(username=new_username)
        )
        async with self.dbsession as session:
            result = await session.execute(select_query)
            user_data = result.scalar_one_or_none()
            if user_data is None:
                raise NotFoundException
            await session.execute(update_query)
            await session.commit()
            user_data.username = new_username
            return user_data

    async def login(self, username: str, password: str):
        async with self.dbsession as session:
            result = await session.execute(select(users).where(users.username == username))
            user_data = result.scalar_one_or_none()
            if user_data is None:
                raise NotFoundException
            if not password_manager.verify(password, user_data.password):
                raise HTTPException(status_code=401, detail="Invalid password")
            return user_data

    async def user_delete_account(self, username: str, password: str):
        async with self.dbsession as session:
            user_data = await session.execute(
                select(users).where(users.username == username)
            )
            user_data = user_data.scalar_one_or_none()
            if user_data is None:
                raise NotFoundException
            if not password_manager.verify(password, user_data.password):
                raise HTTPException(status_code=401, detail="Invalid password")

            delete_query = delete(users).where(users.username == username)
            await session.execute(delete_query)
            await session.commit()
            return user_data


