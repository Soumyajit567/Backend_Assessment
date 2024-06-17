from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, db

router = APIRouter()

@router.post("/", response_model=schemas.UserFollow)
def follow_user(follower_id: int, followed_id: int, db: Session = Depends(db.get_db)):
    return crud.follow_user(db=db, follower_id=follower_id, followed_id=followed_id)

@router.delete("/", response_model=schemas.UserFollow)
def unfollow_user(follower_id: int, followed_id: int, db: Session = Depends(db.get_db)):
    db_follow = crud.unfollow_user(db=db, follower_id=follower_id, followed_id=followed_id)
    if db_follow is None:
        raise HTTPException(status_code=404, detail="Follow relationship not found")
    return db_follow
