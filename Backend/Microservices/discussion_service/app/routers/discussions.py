# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, models, db
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/discussions/", response_model=schemas.Discussion)
# async def create_discussion(discussion: schemas.DiscussionCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received discussion data: {discussion}")
#     try:
#         return crud.create_discussion(db=db, discussion=discussion)
#     except HTTPException as e:
#         logger.error(f"Error creating discussion: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")


# @router.get("/discussions/", response_model=List[schemas.Discussion])
# def read_discussions(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
#     discussions = db.query(models.Discussion).offset(skip).limit(limit).all()
#     return discussions

# @router.get("/discussions/{discussion_id}", response_model=schemas.Discussion)
# def read_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
#     discussion = db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()
#     if discussion is None:
#         raise HTTPException(status_code=404, detail="Discussion not found")
#     return discussion

# @router.put("/discussions/{discussion_id}", response_model=schemas.Discussion)
# def update_discussion(discussion_id: int, discussion: schemas.DiscussionCreate, db: Session = Depends(db.get_db)):
#     db_discussion = crud.update_discussion(db=db, discussion_id=discussion_id, discussion=discussion)
#     if db_discussion is None:
#         raise HTTPException(status_code=404, detail="Discussion not found")
#     return db_discussion

# @router.delete("/discussions/{discussion_id}", response_model=schemas.Discussion)
# def delete_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
#     db_discussion = crud.delete_discussion(db=db, discussion_id=discussion_id)
#     if db_discussion is None:
#         raise HTTPException(status_code=404, detail="Discussion not found")
#     return db_discussion

# from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, models, db
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/discussions/", response_model=schemas.Discussion)
# async def create_discussion(
#     title: str,
#     content: str,
#     user_id: int,
#     file: UploadFile = File(None),
#     db: Session = Depends(db.get_db)
# ):
#     logger.info(f"Received discussion data: title={title}, content={content}, user_id={user_id}")
#     discussion_create = schemas.DiscussionCreate(title=title, content=content, user_id=user_id)
#     try:
#         return crud.create_discussion(db=db, discussion=discussion_create, file=file)
#     except HTTPException as e:
#         logger.error(f"Error creating discussion: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.get("/discussions/", response_model=List[schemas.Discussion])
# def read_discussions(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
#     discussions = db.query(models.Discussion).offset(skip).limit(limit).all()
#     return discussions

# @router.get("/discussions/{discussion_id}", response_model=schemas.Discussion)
# def read_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
#     discussion = db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()
#     if discussion is None:
#         raise HTTPException(status_code=404, detail="Discussion not found")
#     return discussion

# @router.put("/discussions/{discussion_id}", response_model=schemas.Discussion)
# def update_discussion(discussion_id: int, discussion: schemas.DiscussionCreate, db: Session = Depends(db.get_db)):
#     db_discussion = crud.update_discussion(db=db, discussion_id=discussion_id, discussion=discussion)
#     if db_discussion is None:
#         raise HTTPException(status_code=404, detail="Discussion not found")
#     return db_discussion

# @router.delete("/discussions/{discussion_id}", response_model=schemas.Discussion)
# def delete_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
#     db_discussion = crud.delete_discussion(db=db, discussion_id=discussion_id)
#     if db_discussion is None:
#         raise HTTPException(status_code=404, detail="Discussion not found")
#     return db_discussion

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, models, db
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/discussions/", response_model=schemas.Discussion)
async def create_discussion(
    title: str = Form(...),
    content: str = Form(...),
    user_id: int = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(db.get_db)
):
    logger.info(f"Received discussion data: title={title}, content={content}, user_id={user_id}")
    discussion_create = schemas.DiscussionCreate(title=title, content=content, user_id=user_id)
    try:
        return crud.create_discussion(db=db, discussion=discussion_create, file=file)
    except HTTPException as e:
        logger.error(f"Error creating discussion: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/discussions/", response_model=List[schemas.Discussion])
def read_discussions(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    discussions = db.query(models.Discussion).offset(skip).limit(limit).all()
    return discussions

@router.get("/discussions/{discussion_id}", response_model=schemas.Discussion)
def read_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
    discussion = db.query(models.Discussion).filter(models.Discussion.id == discussion_id).first()
    if discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return discussion

@router.put("/discussions/{discussion_id}", response_model=schemas.Discussion)
def update_discussion(discussion_id: int, discussion: schemas.DiscussionCreate, db: Session = Depends(db.get_db)):
    db_discussion = crud.update_discussion(db=db, discussion_id=discussion_id, discussion=discussion)
    if db_discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return db_discussion

@router.delete("/discussions/{discussion_id}", response_model=schemas.Discussion)
def delete_discussion(discussion_id: int, db: Session = Depends(db.get_db)):
    db_discussion = crud.delete_discussion(db=db, discussion_id=discussion_id)
    if db_discussion is None:
        raise HTTPException(status_code=404, detail="Discussion not found")
    return db_discussion
