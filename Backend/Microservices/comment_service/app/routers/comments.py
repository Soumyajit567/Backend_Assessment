from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models, db
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/comments/", response_model=schemas.Comment)
async def create_comment(comment: schemas.CommentCreate, db: Session = Depends(db.get_db)):
    logger.info(f"Received comment data: {comment}")
    try:
        return crud.create_comment(db=db, comment=comment)
    except HTTPException as e:
        logger.error(f"Error creating comment: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/comments/", response_model=List[schemas.Comment])
def read_comments(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    comments = db.query(models.Comment).offset(skip).limit(limit).all()
    return comments

@router.get("/comments/{comment_id}", response_model=schemas.Comment)
def read_comment(comment_id: int, db: Session = Depends(db.get_db)):
    comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.put("/comments/{comment_id}", response_model=schemas.Comment)
def update_comment(comment_id: int, comment: schemas.CommentCreate, db: Session = Depends(db.get_db)):
    db_comment = crud.update_comment(db=db, comment_id=comment_id, comment=comment)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

@router.delete("/comments/{comment_id}", response_model=schemas.Comment)
def delete_comment(comment_id: int, db: Session = Depends(db.get_db)):
    db_comment = crud.delete_comment(db=db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment

