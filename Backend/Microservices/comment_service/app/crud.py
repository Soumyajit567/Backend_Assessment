# from sqlalchemy.orm import Session
# from . import models, schemas
# import httpx
# import logging
# from tenacity import retry, stop_after_attempt, wait_fixed

# logger = logging.getLogger(__name__)

# USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"
# DISCUSSION_SERVICE_URL = "http://127.0.0.1:8001/api/v1/discussions/"

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def get_user_from_user_service(user_id):
#     response = httpx.get(f"{USER_SERVICE_URL}{user_id}", timeout=10.0)
#     response.raise_for_status()
#     return response.json()

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def get_discussion_from_discussion_service(discussion_id):
#     response = httpx.get(f"{DISCUSSION_SERVICE_URL}{discussion_id}", timeout=10.0)
#     response.raise_for_status()
#     return response.json()

# def create_comment(db: Session, comment: schemas.CommentCreate):
#     try:
#         user_data = get_user_from_user_service(comment.user_id)
#         discussion_data = get_discussion_from_discussion_service(comment.discussion_id)
#         db_user = db.query(models.User).filter(models.User.id == comment.user_id).first()
#         if not db_user:
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

#         # Insert discussion data if not already present
#         db_discussion = db.query(models.Discussion).filter(models.Discussion.id == comment.discussion_id).first()
#         if not db_discussion:
#             db_discussion = models.Discussion(
#                 id=discussion_data["id"],
#                 title=discussion_data["title"],
#                 content=discussion_data["content"],
#                 user_id=discussion_data["user_id"]
#             )
#             db.add(db_discussion)
#             db.commit()
#             db.refresh(db_discussion)

#         # Insert comment
#         db_comment = models.Comment(
#             content=comment.content,
#             user_id=comment.user_id,
#             discussion_id=comment.discussion_id
#         )
#         db.add(db_comment)
#         db.commit()
#         db.refresh(db_comment)
#         return db_comment
#     except Exception as e:
#         logger.error(f"Error creating comment: {e}")
#         db.rollback()
#         raise e

# def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate):
#     db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
#     if db_comment is None:
#         return None
#     db_comment.content = comment.content
#     db_comment.user_id = comment.user_id
#     db_comment.discussion_id = comment.discussion_id
#     db.commit()
#     db.refresh(db_comment)
#     return db_comment

# def delete_comment(db: Session, comment_id: int):
#     db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
#     if db_comment is None:
#         return None
#     db.delete(db_comment)
#     db.commit()
#     return db_comment

from sqlalchemy.orm import Session
from . import models, schemas
import httpx
import logging
from tenacity import retry, stop_after_attempt, wait_fixed

logger = logging.getLogger(__name__)

USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"
DISCUSSION_SERVICE_URL = "http://127.0.0.1:8001/api/v1/discussions/"

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_user_from_user_service(user_id):
    response = httpx.get(f"{USER_SERVICE_URL}{user_id}", timeout=10.0)
    response.raise_for_status()
    return response.json()

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_discussion_from_discussion_service(discussion_id):
    response = httpx.get(f"{DISCUSSION_SERVICE_URL}{discussion_id}", timeout=10.0)
    response.raise_for_status()
    return response.json()

def create_comment(db: Session, comment: schemas.CommentCreate):
    try:
        user_data = get_user_from_user_service(comment.user_id)
        discussion_data = get_discussion_from_discussion_service(comment.discussion_id)
        
        db_user = db.query(models.User).filter(models.User.id == comment.user_id).first()
        if not db_user:
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

        db_discussion = db.query(models.Discussion).filter(models.Discussion.id == comment.discussion_id).first()
        if not db_discussion:
            db_discussion = models.Discussion(
                id=discussion_data["id"],
                title=discussion_data["title"],
                content=discussion_data["content"],
                user_id=discussion_data["user_id"],
                file_path=discussion_data.get("file_path")  
            )
            db.add(db_discussion)
            db.commit()
            db.refresh(db_discussion)

        db_comment = models.Comment(
            content=comment.content,
            user_id=comment.user_id,
            discussion_id=comment.discussion_id
        )
        db.add(db_comment)
        db.commit()
        db.refresh(db_comment)
        return db_comment
    except Exception as e:
        logger.error(f"Error creating comment: {e}")
        db.rollback()
        raise e

def update_comment(db: Session, comment_id: int, comment: schemas.CommentCreate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment is None:
        return None
    db_comment.content = comment.content
    db_comment.user_id = comment.user_id
    db_comment.discussion_id = comment.discussion_id
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment is None:
        return None
    db.delete(db_comment)
    db.commit()
    return db_comment
