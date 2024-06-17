from sqlalchemy.orm import Session
from . import models, schemas
from typing import Optional

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

