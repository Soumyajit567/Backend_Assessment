from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_mobile(db: Session, mobile_no: str):
    return db.query(models.User).filter(models.User.mobile_no == mobile_no).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = models.User(name=user.name, mobile_no=user.mobile_no, email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_discussion(db: Session, discussion: schemas.DiscussionCreate, user_id: int):
    db_discussion = models.Discussion(**discussion.dict(), owner_id=user_id)
    db.add(db_discussion)
    db.commit()
    db.refresh(db_discussion)
    return db_discussion

def create_comment(db: Session, comment: schemas.CommentCreate, user_id: int, discussion_id: int):
    db_comment = models.Comment(**comment.dict(), owner_id=user_id, discussion_id=discussion_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def create_like(db: Session, like: schemas.LikeCreate, user_id: int, discussion_id: Optional[int] = None, comment_id: Optional[int] = None):
    if comment_id:
        comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
        if comment:
            discussion_id = comment.discussion_id
    db_like = models.Like(owner_id=user_id, discussion_id=discussion_id, comment_id=comment_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def follow_user(db: Session, follower_id: int, followed_id: int):
    db_follow = models.UserFollow(follower_id=follower_id, followed_id=followed_id)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow

def unfollow_user(db: Session, follower_id: int, followed_id: int):
    db_follow = db.query(models.UserFollow).filter(
        models.UserFollow.follower_id == follower_id,
        models.UserFollow.followed_id == followed_id
    ).first()
    if db_follow:
        db.delete(db_follow)
        db.commit()
    return db_follow

def update_user(db: Session, user_id: int, user: schemas.UserCreate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db_user.name = user.name
        db_user.mobile_no = user.mobile_no
        db_user.email = user.email
        db_user.hashed_password = pwd_context.hash(user.password)
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user











