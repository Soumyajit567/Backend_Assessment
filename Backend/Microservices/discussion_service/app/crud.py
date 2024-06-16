# import httpx
# from sqlalchemy.orm import Session
# from . import models, schemas
# import logging
# from tenacity import retry, stop_after_attempt, wait_fixed

# logger = logging.getLogger(__name__)

# USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"  # User service URL

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def get_user_from_user_service(user_id):
#     response = httpx.get(f"{USER_SERVICE_URL}{user_id}", timeout=10.0)
#     response.raise_for_status()  # Raise an error if the request failed
#     return response.json()

# def create_discussion(db: Session, discussion: schemas.DiscussionCreate):
#     try:
#         logger.info(f"Checking if user with id {discussion.user_id} exists.")
        
#         # Verify if user exists in the user_service database
#         user_data = get_user_from_user_service(discussion.user_id)
#         logger.info(f"User service response content: {user_data}")
        
#         # Check if the user already exists in the discussion_service database
#         db_user = db.query(models.User).filter(models.User.id == discussion.user_id).first()
#         if not db_user:
#             logger.info(f"Inserting user data into discussion_service database: {user_data}")
#             db_user = models.User(
#                 id=user_data["id"],
#                 name=user_data["name"],
#                 mobile_no=user_data["mobile_no"],
#                 email=user_data["email"],
#                 hashed_password="hashed_password_placeholder"  # Placeholder for demonstration
#             )
#             db.add(db_user)
#             db.commit()
#             db.refresh(db_user)
        
#         db_discussion = models.Discussion(
#             title=discussion.title,
#             content=discussion.content,
#             user_id=discussion.user_id
#         )
#         db.add(db_discussion)
#         db.commit()
#         db.refresh(db_discussion)
#         return db_discussion
#     except Exception as e:
#         logger.error(f"Error creating discussion: {e}")
#         db.rollback()
#         raise e



# def get_discussion(db: Session, discussion_id: int):
#     return db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()

# def update_discussion(db: Session, discussion_id: int, discussion: schemas.DiscussionCreate):
#     db_discussion = get_discussion(db, discussion_id)
#     if db_discussion is None:
#         return None
#     db_discussion.title = discussion.title
#     db_discussion.content = discussion.content
#     db.commit()
#     db.refresh(db_discussion)
#     return db_discussion

# def delete_discussion(db: Session, discussion_id: int):
#     db_discussion = get_discussion(db, discussion_id)
#     if db_discussion is None:
#         return None
#     db.delete(db_discussion)
#     db.commit()
#     return db_discussion


# import httpx
# from sqlalchemy.orm import Session
# from . import models, schemas
# import logging
# from tenacity import retry, stop_after_attempt, wait_fixed
# from fastapi import UploadFile
# import os

# logger = logging.getLogger(__name__)

# USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"  

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def get_user_from_user_service(user_id):
#     response = httpx.get(f"{USER_SERVICE_URL}{user_id}", timeout=10.0)
#     response.raise_for_status()
#     return response.json()

# def save_file(file: UploadFile, upload_dir: str):
#     os.makedirs(upload_dir, exist_ok=True)
#     file_path = os.path.join(upload_dir, file.filename)
#     with open(file_path, "wb") as f:
#         f.write(file.file.read())
#     return file_path

# def create_discussion(db: Session, discussion: schemas.DiscussionCreate, file: UploadFile = None):
#     try:
#         logger.info(f"Checking if user with id {discussion.user_id} exists.")
        
#         user_data = get_user_from_user_service(discussion.user_id)
#         logger.info(f"User service response content: {user_data}")
        
#         db_user = db.query(models.User).filter(models.User.id == discussion.user_id).first()
#         if not db_user:
#             logger.info(f"Inserting user data into discussion_service database: {user_data}")
#             db_user = models.User(
#                 id=user_data["id"],
#                 name=user_data["name"],
#                 mobile_no=user_data["mobile_no"],
#                 email=user_data["email"],
#                 hashed_password="hashed_password_placeholder"
#             )
#             db.add(db_user)
#             db.commit()
#             db.refresh(db_user)
        
#         file_path = None
#         if file:
#             file_path = save_file(file, "uploads")
        
#         db_discussion = models.Discussion(
#             title=discussion.title,
#             content=discussion.content,
#             user_id=discussion.user_id,
#             file_path=file_path  
#         )
#         db.add(db_discussion)
#         db.commit()
#         db.refresh(db_discussion)
#         return db_discussion
#     except Exception as e:
#         logger.error(f"Error creating discussion: {e}")
#         db.rollback()
#         raise e



# def get_discussion(db: Session, discussion_id: int):
#     return db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()

# def update_discussion(db: Session, discussion_id: int, discussion: schemas.DiscussionCreate):
#     db_discussion = get_discussion(db, discussion_id)
#     if db_discussion is None:
#         return None
#     db_discussion.title = discussion.title
#     db_discussion.content = discussion.content
#     db.commit()
#     db.refresh(db_discussion)
#     return db_discussion

# def delete_discussion(db: Session, discussion_id: int):
#     db_discussion = get_discussion(db, discussion_id)
#     if db_discussion is None:
#         return None
#     db.delete(db_discussion)
#     db.commit()
#     return db_discussion

import httpx
from sqlalchemy.orm import Session
from . import models, schemas
import logging
from tenacity import retry, stop_after_attempt, wait_fixed
from fastapi import UploadFile
import os

logger = logging.getLogger(__name__)

USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_user_from_user_service(user_id):
    response = httpx.get(f"{USER_SERVICE_URL}{user_id}", timeout=10.0)
    response.raise_for_status()
    return response.json()

def save_file(file: UploadFile, upload_dir: str):
    os.makedirs(upload_dir, exist_ok=True)
    file_path = os.path.join(upload_dir, file.filename)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    return file_path

def create_discussion(db: Session, discussion: schemas.DiscussionCreate, file: UploadFile = None):
    try:
        logger.info(f"Checking if user with id {discussion.user_id} exists.")
        
        user_data = get_user_from_user_service(discussion.user_id)
        logger.info(f"User service response content: {user_data}")
        
        db_user = db.query(models.User).filter(models.User.id == discussion.user_id).first()
        if not db_user:
            logger.info(f"Inserting user data into discussion_service database: {user_data}")
            db_user = models.User(
                id=user_data["id"],
                name=user_data["name"],
                mobile_no=user_data["mobile_no"],
                email=user_data["email"],
                hashed_password="hashed_password_placeholder"
            )
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
        
        file_path = None
        if file:
            file_path = save_file(file, "uploads")
        
        db_discussion = models.Discussion(
            title=discussion.title,
            content=discussion.content,
            user_id=discussion.user_id,
            file_path=file_path
        )
        db.add(db_discussion)
        db.commit()
        db.refresh(db_discussion)
        return db_discussion
    except Exception as e:
        logger.error(f"Error creating discussion: {e}")
        db.rollback()
        raise e

def get_discussion(db: Session, discussion_id: int):
    return db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()

def update_discussion(db: Session, discussion_id: int, discussion: schemas.DiscussionCreate):
    db_discussion = get_discussion(db, discussion_id)
    if db_discussion is None:
        return None
    db_discussion.title = discussion.title
    db_discussion.content = discussion.content
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

def delete_discussion(db: Session, discussion_id: int):
    db_discussion = get_discussion(db, discussion_id)
    if db_discussion is None:
        return None
    db.delete(db_discussion)
    db.commit()
    return db_discussion
