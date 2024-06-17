from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str
    mobile_no: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    created_on: datetime
    owner_id: int
    discussion_id: int
    class Config:
        orm_mode = True

class LikeBase(BaseModel):
    pass

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    id: int
    owner_id: int
    discussion_id: Optional[int] = None
    comment_id: Optional[int] = None
    class Config:
        orm_mode = True

class DiscussionBase(BaseModel):
    text: str
    image: Optional[str] = None
    hashtags: List[str]

class DiscussionCreate(DiscussionBase):
    pass

class Discussion(DiscussionBase):
    id: int
    created_on: datetime
    owner_id: int
    comments: List[Comment] = []
    likes: List[Like] = []
    class Config:
        orm_mode = True

class UserFollowBase(BaseModel):
    follower_id: int
    followed_id: int

class UserFollowCreate(UserFollowBase):
    pass

class UserFollow(UserFollowBase):
    id: int
    class Config:
        orm_mode = True

