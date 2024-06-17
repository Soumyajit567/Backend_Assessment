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



