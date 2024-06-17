from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional

def create_comment(db: Session, comment: schemas.CommentCreate, user_id: int, discussion_id: int):
    db_comment = models.Comment(**comment.dict(), owner_id=user_id, discussion_id=discussion_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
    return db_comment

def create_like(db: Session, like: schemas.LikeCreate, user_id: int, comment_id: int):
    db_like = models.Like(owner_id=user_id, comment_id=comment_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

def delete_like(db: Session, like_id: int):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like:
        db.delete(db_like)
        db.commit()
    return db_like