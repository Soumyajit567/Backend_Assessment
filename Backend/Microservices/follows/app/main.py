from fastapi import FastAPI
from .routers import follows
from .db import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(follows.router, prefix="/api/v1/follows", tags=["follows"])
