# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, db, models
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/users/", response_model=schemas.User)
# async def create_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received user data: {user}")
#     try:
#         return crud.create_user(db=db, user=user)
#     except HTTPException as e:
#         logger.error(f"Error creating user: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.get("/users/{user_id}", response_model=schemas.User)
# async def read_user(user_id: int, db: Session = Depends(db.get_db)):
#     db_user = crud.get_user(db=db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @router.post("/follows/", response_model=schemas.Follow)
# async def create_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received follow data: {follow}")
#     try:
#         return crud.create_follow(db=db, follow=follow)
#     except HTTPException as e:
#         logger.error(f"Error creating follow: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/follows/", response_model=schemas.Follow)
# async def delete_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
#     db_follow = crud.delete_follow(db=db, follow=follow)
#     if db_follow is None:
#         raise HTTPException(status_code=404, detail="Follow relationship not found")
#     return db_follow

# @router.get("/followers/{user_id}", response_model=List[schemas.Follow])
# async def read_followers(user_id: int, db: Session = Depends(db.get_db)):
#     return crud.get_followers(db=db, user_id=user_id)

# @router.get("/followings/{user_id}", response_model=List[schemas.Follow])
# async def read_followings(user_id: int, db: Session = Depends(db.get_db)):
#     return crud.get_followings(db=db, user_id=user_id)


# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, db, models
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/follows/", response_model=schemas.Follow)
# async def create_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received follow data: {follow}")
#     try:
#         return crud.create_follow(db=db, follow=follow)
#     except HTTPException as e:
#         logger.error(f"Error creating follow: {e.detail}")
#         raise e
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/follows/{follow_id}", response_model=schemas.Follow)
# async def delete_follow(follow_id: int, db: Session = Depends(db.get_db)):
#     db_follow = crud.delete_follow(db=db, follow_id=follow_id)
#     if db_follow is None:
#         raise HTTPException(status_code=404, detail="Follow not found")
#     return db_follow

# @router.get("/followers/{user_id}", response_model=List[schemas.Follow])
# async def get_followers(user_id: int, db: Session = Depends(db.get_db)):
#     followers = crud.get_followers(db=db, user_id=user_id)
#     return followers

# @router.get("/followings/{user_id}", response_model=List[schemas.Follow])
# async def get_followings(user_id: int, db: Session = Depends(db.get_db)):
#     followings = crud.get_followings(db=db, user_id=user_id)
#     return followings
# @router.get("/followers/{user_id}", response_model=List[schemas.Follow])
# async def read_followers(user_id: int, db: Session = Depends(db.get_db)):
#     return crud.get_followers(db=db, user_id=user_id)

# @router.get("/followings/{user_id}", response_model=List[schemas.Follow])
# async def read_followings(user_id: int, db: Session = Depends(db.get_db)):
#     return crud.get_followings(db=db, user_id=user_id)

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from .. import crud, schemas, db
# import logging

# router = APIRouter()
# logger = logging.getLogger(__name__)

# @router.post("/follows/", response_model=schemas.Follow)
# async def create_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
#     logger.info(f"Received follow data: {follow}")
#     try:
#         return crud.create_follow(db=db, follow=follow)
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.delete("/follows/", response_model=schemas.Follow)
# async def delete_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
#     try:
#         db_follow = crud.delete_follow(db=db, follow=follow)
#         if db_follow is None:
#             raise HTTPException(status_code=404, detail="Follow not found")
#         return db_follow
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.get("/followers/{user_id}", response_model=List[schemas.User])
# async def get_followers(user_id: int, db: Session = Depends(db.get_db)):
#     try:
#         followers = crud.get_followers(db=db, user_id=user_id)
#         return followers
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# @router.get("/followings/{user_id}", response_model=List[schemas.User])
# async def get_followings(user_id: int, db: Session = Depends(db.get_db)):
#     try:
#         followings = crud.get_followings(db=db, user_id=user_id)
#         return followings
#     except Exception as e:
#         logger.error(f"Unexpected error: {str(e)}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas, db
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

@router.post("/follows/", response_model=schemas.Follow)
async def create_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
    logger.info(f"Received follow data: {follow}")
    try:
        return crud.create_follow(db=db, follow=follow)
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/follows/", response_model=schemas.Follow)
async def delete_follow(follow: schemas.FollowCreate, db: Session = Depends(db.get_db)):
    try:
        db_follow = crud.delete_follow(db=db, follow=follow)
        if db_follow is None:
            raise HTTPException(status_code=404, detail="Follow not found")
        return db_follow
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/followers/{user_id}", response_model=List[schemas.User])
async def get_followers(user_id: int, db: Session = Depends(db.get_db)):
    try:
        followers = crud.get_followers(db=db, user_id=user_id)
        return followers
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/followings/{user_id}", response_model=List[schemas.User])
async def get_followings(user_id: int, db: Session = Depends(db.get_db)):
    try:
        followings = crud.get_followings(db=db, user_id=user_id)
        return followings
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
