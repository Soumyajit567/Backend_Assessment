# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, models, db
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/likes/", response_model=schemas.Like)
# async def create_like(like: schemas.LikeCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received like data: {like}")
#     try:
#         return crud.create_like(db=db, like=like)
#     except HTTPException as e:
#         logger.error(f"Error creating like: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/likes/{like_id}", response_model=schemas.Like)
# async def delete_like(like_id: int, db: Session = Depends(db.get_db)):
#     db_like = crud.delete_like(db=db, like_id=like_id)
#     if db_like is None:
#         raise HTTPException(status_code=404, detail="Like not found")
#     return db_like

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, models, db
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/likes/", response_model=schemas.Like)
# async def create_like(like: schemas.LikeCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received like data: {like}")
#     try:
#         return crud.create_like(db=db, like=like)
#     except HTTPException as e:
#         logger.error(f"Error creating like: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/likes/{like_id}", response_model=schemas.Like)
# async def delete_like(like_id: int, db: Session = Depends(db.get_db)):
#     db_like = crud.delete_like(db=db, like_id=like_id)
#     if db_like is None:
#         raise HTTPException(status_code=404, detail="Like not found")
#     return db_like

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, db
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/likes/", response_model=schemas.Like)
# async def create_like(like: schemas.LikeCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received like data: {like}")
#     try:
#         return crud.create_like(db=db, like=like)
#     except HTTPException as e:
#         logger.error(f"Error creating like: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/likes/{like_id}", response_model=schemas.Like)
# async def delete_like(like_id: int, db: Session = Depends(db.get_db)):
#     db_like = crud.delete_like(db=db, like_id=like_id)
#     if db_like is None:
#         raise HTTPException(status_code=404, detail="Like not found")
#     return db_like

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, db, models
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/likes/", response_model=schemas.Like)
async def create_like(like: schemas.LikeCreate, db: Session = Depends(db.get_db)):
    logger.info(f"Received like data: {like}")
    try:
        return crud.create_like(db=db, like=like)
    except HTTPException as e:
        logger.error(f"Error creating like: {e.detail}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/likes/{like_id}", response_model=schemas.Like)
async def delete_like(like_id: int, db: Session = Depends(db.get_db)):
    db_like = crud.delete_like(db=db, like_id=like_id)
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like

@router.get("/likes/", response_model=List[schemas.Like])
async def read_likes(db: Session = Depends(db.get_db)):
    likes = db.query(models.Like).all()
    return likes

@router.get("/likes/{like_id}", response_model=schemas.Like)
async def read_like(like_id: int, db: Session = Depends(db.get_db)):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return db_like