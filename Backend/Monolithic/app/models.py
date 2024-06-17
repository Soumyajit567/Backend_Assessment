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

    discussions = relationship("Discussion", back_populates="owner")
    followers = relationship("UserFollow", back_populates="follower", foreign_keys="[UserFollow.follower_id]")
    following = relationship("UserFollow", back_populates="followed", foreign_keys="[UserFollow.followed_id]")

class Discussion(Base):
    __tablename__ = "discussions"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    image = Column(String, nullable=True)
    hashtags = Column(ARRAY(String), index=True)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="discussions")
    comments = relationship("Comment", back_populates="discussion")
    likes = relationship("Like", back_populates="discussion")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    created_on = Column(DateTime, default=datetime.datetime.utcnow)
    owner_id = Column(Integer, ForeignKey("users.id"))
    discussion_id = Column(Integer, ForeignKey("discussions.id"))

    owner = relationship("User")
    discussion = relationship("Discussion", back_populates="comments")
    likes = relationship("Like", back_populates="comment")

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    discussion_id = Column(Integer, ForeignKey("discussions.id"), nullable=True)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    owner = relationship("User")
    discussion = relationship("Discussion", back_populates="likes")
    comment = relationship("Comment", back_populates="likes")

class UserFollow(Base):
    __tablename__ = "user_follows"

    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey("users.id"))
    followed_id = Column(Integer, ForeignKey("users.id"))

    follower = relationship("User", foreign_keys=[follower_id], back_populates="followers")
    followed = relationship("User", foreign_keys=[followed_id], back_populates="following")


