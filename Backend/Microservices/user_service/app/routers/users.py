# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List
# from app import crud, schemas, models, db

# router = APIRouter()

# @router.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)

# @router.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
#     users = db.query(models.User).offset(skip).limit(limit).all()
#     return users

# @router.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(db.get_db)):
#     db_user = db.query(models.User).filter(models.User.id == user_id).first()
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @router.put("/users/{user_id}", response_model=schemas.User)
# def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(db.get_db)):
#     db_user = crud.update_user(db=db, user_id=user_id, user=user)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

# @router.delete("/users/{user_id}", response_model=schemas.User)
# def delete_user(user_id: int, db: Session = Depends(db.get_db)):
#     db_user = crud.delete_user(db=db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, schemas, models, db
import httpx

router = APIRouter()

DISCUSSION_SERVICE_URL = "http://127.0.0.1:8001/sync_user/"

def sync_user_with_discussion_service(user: schemas.User):
    try:
        response = httpx.post(DISCUSSION_SERVICE_URL, json=user.dict())
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=500, detail=f"Failed to sync user with discussion service: {e}")

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    created_user = crud.create_user(db=db, user=user)
    
    # Sync with discussion service
    sync_user_with_discussion_service(schemas.User.from_orm(created_user))
    
    return created_user

@router.put("/users/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = crud.update_user(db=db, user_id=user_id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Sync with discussion service
    sync_user_with_discussion_service(schemas.User.from_orm(db_user))
    
    return db_user


@router.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(db.get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(db.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# @router.put("/users/{user_id}", response_model=schemas.User)
# def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(db.get_db)):
#     db_user = crud.update_user(db=db, user_id=user_id, user=user)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
    
#     # Sync with discussion service
#     sync_user_with_discussion_service(user)
    
#     return db_user

@router.delete("/users/{user_id}", response_model=schemas.User)
def delete_user(user_id: int, db: Session = Depends(db.get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
