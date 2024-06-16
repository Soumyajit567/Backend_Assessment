# from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint
# from .db import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     mobile_no = Column(String, unique=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)

# class Follow(Base):
#     __tablename__ = "follows"

#     id = Column(Integer, primary_key=True, index=True)
#     follower_id = Column(Integer, ForeignKey("users.id"))
#     followee_id = Column(Integer, ForeignKey("users.id"))
#     UniqueConstraint('follower_id', 'followee_id', name='unique_follow')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mobile_no = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey("users.id"))
    followee_id = Column(Integer, ForeignKey("users.id"))
    
    follower = relationship("User", foreign_keys=[follower_id])
    followee = relationship("User", foreign_keys=[followee_id])

