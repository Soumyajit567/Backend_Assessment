from fastapi import FastAPI
from .routers import likes
from .db import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(likes.router, prefix="/api/v1/likes", tags=["likes"])
