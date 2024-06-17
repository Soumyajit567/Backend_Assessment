from pydantic import BaseModel

class UserFollowBase(BaseModel):
    follower_id: int
    followed_id: int

class UserFollowCreate(UserFollowBase):
    pass

class UserFollow(UserFollowBase):
    id: int
    class Config:
        orm_mode = True
