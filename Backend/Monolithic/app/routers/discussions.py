from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form, Query
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models, db

router = APIRouter()

@router.post("/discussions/", response_model=schemas.Discussion)
async def create_discussion(
    text: str = Form(...),
    hashtags: str = Form(...),
    user_id: int = Form(...),
    image: UploadFile = File(None),
    db: Session = Depends(db.get_db)
):
    image_url = None
    if image:
        image_url = f"http://example.com/{image.filename}"
    discussion_data = schemas.DiscussionCreate(
        text=text,
        image=image_url,
        hashtags=hashtags.split(",")
    )
    return crud.create_discussion(db=db, discussion=discussion_data, user_id=user_id)

@router.get("/discussions/", response_model=List[schemas.Discussion])
def read_discussions(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    discussions = db.query(models.Discussion).offset(skip).limit(limit).all()
    return discussions

@router.get("/discussions/{discussion_id}", response_model=schemas.Discussion)
def read_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
    db_discussion = db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()
    if db_discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return db_discussion

@router.post("/discussions/{discussion_id}/comments/", response_model=schemas.Comment)
def create_comment(
    discussion_id: int,
    comment: schemas.CommentCreate,
    user_id: int = Query(...),
    db: Session = Depends(db.get_db)
):
    return crud.create_comment(db=db, comment=comment, user_id=user_id, discussion_id=discussion_id)

@router.post("/discussions/{discussion_id}/likes/", response_model=schemas.Like)
def create_discussion_like(discussion_id: int, user_id: int = Query(...), db: Session = Depends(db.get_db)):
    return crud.create_like(db=db, like=schemas.LikeCreate(), user_id=user_id, discussion_id=discussion_id)

@router.post("/comments/{comment_id}/likes/", response_model=schemas.Like)
def create_comment_like(comment_id: int, user_id: int = Query(...), db: Session = Depends(db.get_db)):
    return crud.create_like(db=db, like=schemas.LikeCreate(), user_id=user_id, comment_id=comment_id)





