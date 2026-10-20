from pydantic import BaseModel

class register_user(BaseModel):
    username: str
    password: int

