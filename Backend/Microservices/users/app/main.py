from fastapi import FastAPI
from .db import engine, Base
from .routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Discussions API"}


