from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
    comment_id: Optional[int] = None

    class Config:
        orm_mode = True
