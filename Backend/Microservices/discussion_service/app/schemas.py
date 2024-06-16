# from pydantic import BaseModel, EmailStr
# from typing import List

# class DiscussionBase(BaseModel):
#     title: str
#     content: str

# class DiscussionCreate(DiscussionBase):
#     pass

# class Discussion(DiscussionBase):
#     id: int
#     user_id: int

#     class Config:
#         orm_mode = True

# class UserBase(BaseModel):
#     name: str
#     mobile_no: str
#     email: EmailStr

# class UserCreate(UserBase):
#     password: str

# class User(UserBase):
#     id: int
#     discussions: List[Discussion] = []

#     class Config:
#         orm_mode = True

# from pydantic import BaseModel

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

# from pydantic import BaseModel

# class UserBase(BaseModel):
#     name: str
#     mobile_no: str
#     email: str

# class UserCreate(UserBase):
#     hashed_password: str

# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode = True

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

# from pydantic import BaseModel

# class UserBase(BaseModel):
#     name: str
#     mobile_no: str
#     email: str

# class UserCreate(UserBase):
#     hashed_password: str

# class User(UserBase):
#     id: int

#     class Config:
#         orm_mode = True

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
#         orm_mode = True

# class DiscussionBase(BaseModel):
#     title: str
#     content: str

# class DiscussionCreate(DiscussionBase):
#     user_id: int

# class Discussion(DiscussionBase):
#     id: int
#     user_id: int
#     file_path: Optional[str] = None  

#     class Config:
#         orm_mode = True

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
