from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from .. import models, schemas, db

router = APIRouter()

@router.post("/sync_user/", response_model=schemas.User)
def sync_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = db.query(models.User).filter(models.User.id == user.id).first()
    if db_user:
        db_user.name = user.name
        db_user.mobile_no = user.mobile_no
        db_user.email = user.email
        db_user.hashed_password = user.hashed_password
    else:
        db_user = models.User(
            id=user.id,
            name=user.name,
            mobile_no=user.mobile_no,
            email=user.email,
            hashed_password=user.hashed_password
        )
        db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
