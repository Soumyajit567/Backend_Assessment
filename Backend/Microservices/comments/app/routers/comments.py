from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models, db

router = APIRouter()

@router.post("/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, user_id: int, discussion_id: int, db: Session = Depends(db.get_db)):
    return crud.create_comment(db=db, comment=comment, user_id=user_id, discussion_id=discussion_id)

@router.get("/", response_model=List[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    comments = db.query(models.Comment).offset(skip).limit(limit).all()
    return comments

@router.get("/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(db.get_db)):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.delete("/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(db.get_db)):
    db_comment = crud.delete_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.post("/{comment_id}/likes/", response_model=schemas.Like)
def like_comment(comment_id: int, user_id: int, db: Session = Depends(db.get_db)):
    return crud.create_like(db=db, like=schemas.LikeCreate(), user_id=user_id, comment_id=comment_id)

@router.delete("/likes/{like_id}", response_model=schemas.Like)
def delete_like(like_id: int, db: Session = Depends(db.get_db)):
    db_like = crud.delete_like(db=db, like_id=like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like
