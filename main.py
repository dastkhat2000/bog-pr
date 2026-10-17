from fastapi import FastAPI
from routers.users import router as users_router
import uvicorn
app = FastAPI()
app.include_router(users_router , prefix="/users")





if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
