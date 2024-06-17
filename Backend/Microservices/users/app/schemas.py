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

class UserFollowBase(BaseModel):
    follower_id: int
    followed_id: int

class UserFollowCreate(UserFollowBase):
    pass

class UserFollow(UserFollowBase):
    id: int
    class Config:
        orm_mode = True