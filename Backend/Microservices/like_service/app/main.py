import logging
import sys
import os
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

# Add the project root directory to the PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

# Print PYTHONPATH
print("PYTHONPATH:", sys.path)

# Print current working directory
print("Current Working Directory:", os.getcwd())

# Load environment variables
if os.getenv("DOCKER_ENV") == "docker":
    load_dotenv(".env")
else:
    load_dotenv(".env.local")

DATABASE_URL = os.getenv("DATABASE_URL")
print("DATABASE_URL:", DATABASE_URL)  # For debugging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Use absolute import
from app.router import likes

app = FastAPI()

app.include_router(likes.router, prefix="/api/v1", tags=["likes"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the Like Service API"}
