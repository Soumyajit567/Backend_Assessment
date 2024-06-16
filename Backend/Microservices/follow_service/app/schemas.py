# from pydantic import BaseModel
# from typing import Optional

# class UserBase(BaseModel):
#     name: str
#     mobile_no: str
#     email: str

# class UserCreate(UserBase):
#     hashed_password: str

# class User(UserBase):
#     id: int

#     class Config:
#         from_attributes = True

# class FollowBase(BaseModel):
#     follower_id: int
#     followee_id: int

# class FollowCreate(FollowBase):
#     pass

# class Follow(FollowBase):
#     id: int

#     class Config:
#         from_attributes = True

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

class FollowBase(BaseModel):
    follower_id: int
    followee_id: int

class FollowCreate(FollowBase):
    pass

class Follow(FollowBase):
    id: int

    class Config:
        orm_mode = True
