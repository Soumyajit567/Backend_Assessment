from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from .db import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    mobile_no = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    
    followers = relationship("UserFollow", back_populates="follower", foreign_keys="[UserFollow.follower_id]")
    following = relationship("UserFollow", back_populates="followed", foreign_keys="[UserFollow.followed_id]")

