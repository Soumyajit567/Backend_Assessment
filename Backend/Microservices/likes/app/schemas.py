from pydantic import BaseModel
from typing import Optional

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
