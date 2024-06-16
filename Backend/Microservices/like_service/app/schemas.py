from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    name: str
    mobile_no: str
    email: str

class UserCreate(UserBase):
    hashed_password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# class DiscussionBase(BaseModel):
#     title: str
#     content: str

# class DiscussionCreate(DiscussionBase):
#     user_id: int

# class Discussion(DiscussionBase):
#     id: int
#     user_id: int

#     class Config:
#         orm_mode = True

class DiscussionBase(BaseModel):
    title: str
    content: str

class DiscussionCreate(DiscussionBase):
    user_id: int

class Discussion(DiscussionBase):
    id: int
    user_id: int
    file_path: Optional[str] = None

    class Config:
        orm_mode = True

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    user_id: int
    discussion_id: int

class Comment(CommentBase):
    id: int
    user_id: int
    discussion_id: int

    class Config:
        orm_mode = True

# class LikeBase(BaseModel):
#     user_id: int
#     discussion_id: Optional[int] = None
#     comment_id: Optional[int] = None

# class LikeCreate(LikeBase):
#     pass

# class Like(LikeBase):
#     id: int

#     class Config:
#         orm_mode = True

class LikeBase(BaseModel):
    user_id: int
    content_id: int
    content_type: str  # "discussion" or "comment"

class LikeCreate(LikeBase):
    pass

class Like(LikeBase):
    id: int

    class Config:
        orm_mode = True
