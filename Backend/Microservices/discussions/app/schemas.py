from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

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

