from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from .db import Base
import datetime

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

    owner = relationship("User", back_populates="comments")
    discussion = relationship("Discussion", back_populates="comments")
    likes = relationship("Like", back_populates="comment")

class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
    discussion_id = Column(Integer, ForeignKey("discussions.id"), nullable=True)
    comment_id = Column(Integer, ForeignKey("comments.id"), nullable=True)

    owner = relationship("User", back_populates="likes")
    discussion = relationship("Discussion", back_populates="likes")
    comment = relationship("Comment", back_populates="likes")
