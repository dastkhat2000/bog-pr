from typing import Annotated

from fastapi import APIRouter, Body, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from db.engine import get_db
from operations.users import userOperations
from schemas._Input import DeleteUserAccountInput, RegisterInput, UpdateUserProfileInput

router = APIRouter()


@router.post("/register")
async def register(
    db_Session: Annotated[AsyncSession, Depends(get_db)],
    data: RegisterInput = Body(),
):
    user = await userOperations(db_Session).create(
        username=data.username,
        password=data.password,
    )
    return user


@router.post("/login")
async def login(
    db_Session: Annotated[AsyncSession, Depends(get_db)],
    data: RegisterInput = Body(),
):
    user = await userOperations(db_Session).login(
        username=data.username,
        password=data.password,
    )
    return {"username": user.username, "message": "login ok"}


@router.get("/{username}/")
async def get_user_profile(
    username: str,
    db_Session: Annotated[AsyncSession, Depends(get_db)],
):
    user_profile = await userOperations(db_Session).get_user_by_username(username)
    return user_profile


@router.put("/")
async def update_user_profile(
    db_Session: Annotated[AsyncSession, Depends(get_db)],
    data: UpdateUserProfileInput = Body(),
):
    user = await userOperations(db_Session).update_username(
        data.old_username,
        data.new_username,
    )
    return user


@router.delete("/")
async def delete_user_account(
    db_Session: Annotated[AsyncSession, Depends(get_db)],
    data: DeleteUserAccountInput = Body(),
):
    user_profile = await userOperations(db_Session).user_delete_account(
        data.username,
        data.password,
    )
    return user_profile
