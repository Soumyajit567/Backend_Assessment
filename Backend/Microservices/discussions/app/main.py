from fastapi import FastAPI
from .routers import discussions
from .db import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(discussions.router, prefix="/api/v1/discussions", tags=["discussions"])
