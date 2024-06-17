from fastapi import FastAPI
from .routers import comments
from .db import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(comments.router, prefix="/api/v1/comments", tags=["comments"])
