from fastapi import APIRouter
from fastapi.params import Body

from schemas._Input import register_user

router = APIRouter()
@router.post("/register")
async def register(data: register_user = Body):
    return  data

@router.post("/login")
async def login():
    ...
@router.get("/")
async def get_user_profile():
    ...
@router.put("/")
async def user_update_profile():
    ...
