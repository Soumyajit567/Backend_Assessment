from pydantic import BaseModel, EmailStr

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
