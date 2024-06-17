from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas, models, db
from typing import Optional

router = APIRouter()

@router.post("/", response_model=schemas.Discussion)
def create_discussion(discussion: schemas.DiscussionCreate, user_id: int, db: Session = Depends(db.get_db)):
    return crud.create_discussion(db=db, discussion=discussion, user_id=user_id)

@router.get("/", response_model=List[schemas.Discussion])
def read_discussions(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    discussions = db.query(models.Discussion).offset(skip).limit(limit).all()
    return discussions

@router.get("/{discussion_id}", response_model=schemas.Discussion)
def read_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
    db_discussion = db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()
    if db_discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return db_discussion

@router.post("/{discussion_id}/comments/", response_model=schemas.Comment)
def create_comment(comment: schemas.CommentCreate, discussion_id: int, user_id: int, db: Session = Depends(db.get_db)):
    return crud.create_comment(db=db, comment=comment, user_id=user_id, discussion_id=discussion_id)

@router.delete("/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(db.get_db)):
    db_comment = crud.delete_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.post("/{discussion_id}/likes/", response_model=schemas.Like)
def like_discussion(discussion_id: int, user_id: int, db: Session = Depends(db.get_db)):
    return crud.create_like(db=db, like=schemas.LikeCreate(), user_id=user_id, discussion_id=discussion_id)

@router.post("/{discussion_id}/comments/{comment_id}/likes/", response_model=schemas.Like)
def like_comment(discussion_id: int, comment_id: int, user_id: int, db: Session = Depends(db.get_db)):
    return crud.create_like(db=db, like=schemas.LikeCreate(), user_id=user_id, comment_id=comment_id)

@router.delete("/likes/{like_id}", response_model=schemas.Like)
def delete_like(like_id: int, db: Session = Depends(db.get_db)):
    db_like = crud.delete_like(db=db, like_id=like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

