from contextlib import asynccontextmanager
from fastapi import FastAPI
from db.__pychache__.engine import Base, engine
from routers.users import router as users_router
import uvicorn
app = FastAPI()
app.include_router(users_router , prefix="/users")

#@app.on_event("startup")
#async def init_tables():
#    async with engine.begin() as conn:
 #       await conn.run_sync(Base.metadata.create_all)

@asynccontextmanager
async def lifespan(app: FastAPI):
     async with engine.begin() as conn:
         await conn.run_sync(Base.metadata.create_all)



if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
