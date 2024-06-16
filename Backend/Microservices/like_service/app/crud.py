from sqlalchemy.orm import Session
from . import models, schemas
import httpx
import logging
from tenacity import retry, stop_after_attempt, wait_fixed

logger = logging.getLogger(__name__)

USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"
DISCUSSION_SERVICE_URL = "http://127.0.0.1:8001/api/v1/discussions/"
COMMENT_SERVICE_URL = "http://127.0.0.1:8002/api/v1/comments/"

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

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def get_comment_from_comment_service(comment_id):
    response = httpx.get(f"{COMMENT_SERVICE_URL}{comment_id}", timeout=10.0)
    response.raise_for_status()
    return response.json()

# def create_like(db: Session, like: schemas.LikeCreate):
#     try:
#         user_data = get_user_from_user_service(like.user_id)
#         db_user = db.query(models.User).filter(models.User.id == like.user_id).first()
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

#         if like.content_type == "discussion":
#             discussion_data = get_discussion_from_discussion_service(like.content_id)
#             db_discussion = db.query(models.Discussion).filter(models.Discussion.id == like.content_id).first()
#             if not db_discussion:
#                 db_discussion = models.Discussion(
#                     id=discussion_data["id"],
#                     title=discussion_data["title"],
#                     content=discussion_data["content"],
#                     user_id=discussion_data["user_id"]
#                 )
#                 db.add(db_discussion)
#                 db.commit()
#                 db.refresh(db_discussion)

#         elif like.content_type == "comment":
#             comment_data = get_comment_from_comment_service(like.content_id)
#             db_comment = db.query(models.Comment).filter(models.Comment.id == like.content_id).first()
#             if not db_comment:
#                 db_comment = models.Comment(
#                     id=comment_data["id"],
#                     content=comment_data["content"],
#                     user_id=comment_data["user_id"],
#                     discussion_id=comment_data["discussion_id"]
#                 )
#                 db.add(db_comment)
#                 db.commit()
#                 db.refresh(db_comment)

#         db_like = models.Like(
#             user_id=like.user_id,
#             content_id=like.content_id,
#             content_type=like.content_type
#         )
#         db.add(db_like)
#         db.commit()
#         db.refresh(db_like)
#         return db_like
#     except Exception as e:
#         logger.error(f"Error creating like: {e}")
#         db.rollback()
#         raise e

def create_like(db: Session, like: schemas.LikeCreate):
    try:
        user_data = get_user_from_user_service(like.user_id)
        db_user = db.query(models.User).filter(models.User.id == like.user_id).first()
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

        if like.content_type == "discussion":
            discussion_data = get_discussion_from_discussion_service(like.content_id)
            db_discussion = db.query(models.Discussion).filter(models.Discussion.id == like.content_id).first()
            if not db_discussion:
                db_discussion = models.Discussion(
                    id=discussion_data["id"],
                    title=discussion_data["title"],
                    content=discussion_data["content"],
                    user_id=discussion_data["user_id"],
                    file_path=discussion_data.get("file_path", None)  # Include file_path
                )
                db.add(db_discussion)
                db.commit()
                db.refresh(db_discussion)

        elif like.content_type == "comment":
            comment_data = get_comment_from_comment_service(like.content_id)
            db_comment = db.query(models.Comment).filter(models.Comment.id == like.content_id).first()
            if not db_comment:
                db_comment = models.Comment(
                    id=comment_data["id"],
                    content=comment_data["content"],
                    user_id=comment_data["user_id"],
                    discussion_id=comment_data["discussion_id"]
                )
                db.add(db_comment)
                db.commit()
                db.refresh(db_comment)

        db_like = models.Like(
            user_id=like.user_id,
            content_id=like.content_id,
            content_type=like.content_type
        )
        db.add(db_like)
        db.commit()
        db.refresh(db_like)
        return db_like
    except Exception as e:
        logger.error(f"Error creating like: {e}")
        db.rollback()
        raise e

def delete_like(db: Session, like_id: int):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like is None:
        return None
    db.delete(db_like)
    db.commit()
    return db_like

def get_likes(db: Session):
    return db.query(models.Like).all()

def get_like_by_id(db: Session, like_id: int):
    return db.query(models.Like).filter(models.Like.id == like_id).first()


