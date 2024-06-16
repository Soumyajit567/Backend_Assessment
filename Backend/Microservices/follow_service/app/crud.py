# from sqlalchemy.orm import Session
# from . import models, schemas

# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(
#         name=user.name,
#         mobile_no=user.mobile_no,
#         email=user.email,
#         hashed_password=user.hashed_password
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()

# def create_follow(db: Session, follow: schemas.FollowCreate):
#     db_follow = models.Follow(follower_id=follow.follower_id, followee_id=follow.followee_id)
#     db.add(db_follow)
#     db.commit()
#     db.refresh(db_follow)
#     return db_follow

# def delete_follow(db: Session, follow: schemas.FollowCreate):
#     db_follow = db.query(models.Follow).filter_by(follower_id=follow.follower_id, followee_id=follow.followee_id).first()
#     if db_follow:
#         db.delete(db_follow)
#         db.commit()
#     return db_follow

# def get_followers(db: Session, user_id: int):
#     return db.query(models.Follow).filter_by(followee_id=user_id).all()

# def get_followings(db: Session, user_id: int):
#     return db.query(models.Follow).filter_by(follower_id=user_id).all()

# from sqlalchemy.orm import Session
# from . import models, schemas
# import httpx
# import logging
# from tenacity import retry, stop_after_attempt, wait_fixed

# logger = logging.getLogger(__name__)

# USER_SERVICE_URL = "http://127.0.0.1:8000/api/v1/users/"

# @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
# def get_user_from_user_service(user_id):
#     response = httpx.get(f"{USER_SERVICE_URL}{user_id}", timeout=10.0)
#     response.raise_for_status()
#     return response.json()

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()

# def create_follow(db: Session, follow: schemas.FollowCreate):
#     try:
#         follower_data = get_user_from_user_service(follow.follower_id)
#         followee_data = get_user_from_user_service(follow.followee_id)
        
#         db_follower = db.query(models.User).filter(models.User.id == follow.follower_id).first()
#         if not db_follower:
#             db_follower = models.User(
#                 id=follower_data["id"],
#                 name=follower_data["name"],
#                 mobile_no=follower_data["mobile_no"],
#                 email=follower_data["email"],
#                 hashed_password="hashed_password_placeholder"
#             )
#             db.add(db_follower)
#             db.commit()
#             db.refresh(db_follower)
        
#         db_followee = db.query(models.User).filter(models.User.id == follow.followee_id).first()
#         if not db_followee:
#             db_followee = models.User(
#                 id=followee_data["id"],
#                 name=followee_data["name"],
#                 mobile_no=followee_data["mobile_no"],
#                 email=followee_data["email"],
#                 hashed_password="hashed_password_placeholder"
#             )
#             db.add(db_followee)
#             db.commit()
#             db.refresh(db_followee)

#         db_follow = models.Follow(follower_id=follow.follower_id, followee_id=follow.followee_id)
#         db.add(db_follow)
#         db.commit()
#         db.refresh(db_follow)
#         return db_follow
#     except Exception as e:
#         logger.error(f"Error creating follow: {e}")
#         db.rollback()
#         raise e

# def delete_follow(db: Session, follow_id: int):
#     db_follow = db.query(models.Follow).filter(models.Follow.id == follow_id).first()
#     if db_follow:
#         db.delete(db_follow)
#         db.commit()
#     return db_follow

# def get_followers(db: Session, user_id: int):
#     return db.query(models.Follow).filter_by(followee_id=user_id).all()

# def get_followings(db: Session, user_id: int):
#     return db.query(models.Follow).filter_by(follower_id=user_id).all()

# from sqlalchemy.orm import Session
# from . import models, schemas

# def create_user(db: Session, user: schemas.UserCreate):
#     db_user = models.User(
#         name=user.name,
#         mobile_no=user.mobile_no,
#         email=user.email,
#         hashed_password=user.hashed_password
#     )
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()

# def create_follow(db: Session, follow: schemas.FollowCreate):
#     db_follow = models.Follow(follower_id=follow.follower_id, followee_id=follow.followee_id)
#     db.add(db_follow)
#     db.commit()
#     db.refresh(db_follow)
#     return db_follow

# def delete_follow(db: Session, follow: schemas.FollowCreate):
#     db_follow = db.query(models.Follow).filter_by(follower_id=follow.follower_id, followee_id=follow.followee_id).first()
#     if db_follow:
#         db.delete(db_follow)
#         db.commit()
#     return db_follow

# def get_followers(db: Session, user_id: int):
#     followers = db.query(models.Follow).filter_by(followee_id=user_id).all()
#     return [get_user(db, follow.follower_id) for follow in followers]

# def get_followings(db: Session, user_id: int):
#     followings = db.query(models.Follow).filter_by(follower_id=user_id).all()
#     return [get_user(db, follow.followee_id) for follow in followings]


from sqlalchemy.orm import Session
from . import models, schemas

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        mobile_no=user.mobile_no,
        email=user.email,
        hashed_password=user.hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_follow(db: Session, follow: schemas.FollowCreate):
    db_follow = models.Follow(follower_id=follow.follower_id, followee_id=follow.followee_id)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow

def delete_follow(db: Session, follow: schemas.FollowCreate):
    db_follow = db.query(models.Follow).filter_by(follower_id=follow.follower_id, followee_id=follow.followee_id).first()
    if db_follow:
        db.delete(db_follow)
        db.commit()
    return db_follow

def get_followers(db: Session, user_id: int):
    followers = db.query(models.Follow).filter_by(followee_id=user_id).all()
    return [get_user(db, follow.follower_id) for follow in followers]

def get_followings(db: Session, user_id: int):
    followings = db.query(models.Follow).filter_by(follower_id=user_id).all()
    return [get_user(db, follow.followee_id) for follow in followings]
