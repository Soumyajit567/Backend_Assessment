from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas, models, db

router = APIRouter()

@router.post("/", response_model=schemas.Like)
def create_like(like: schemas.LikeCreate, user_id: int, discussion_id: Optional[int] = None, comment_id: Optional[int] = None, db: Session = Depends(db.get_db)):
    return crud.create_like(db=db, like=like, user_id=user_id, discussion_id=discussion_id, comment_id=comment_id)

@router.get("/", response_model=List[schemas.Like])
def read_likes(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    likes = db.query(models.Like).offset(skip).limit(limit).all()
    return likes

@router.get("/{like_id}", response_model=schemas.Like)
def read_like(like_id: int, db: Session = Depends(db.get_db)):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

@router.delete("/{like_id}", response_model=schemas.Like)
def delete_like(like_id: int, db: Session = Depends(db.get_db)):
    db_like = crud.delete_like(db=db, like_id=like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like
