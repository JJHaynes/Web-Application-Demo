from fastapi import APIRouter, Depends, HTTPException
from uuid import UUID
from sqlalchemy.orm import Session
from ... import schemas, crud
from ...dependencies.auth import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.patch("/{user_id}", response_model=schemas.user.UserRead)
def update_user(user_id: UUID, user_in: schemas.user.UserUpdate, db: Session = Depends(get_db)):
    if crud.user.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.user.update_user(db, user_id, user_in)

@router.get("/", response_model=list[schemas.user.UserRead])
def list_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.user.list_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=schemas.user.UserRead)
def read_user(user_id: UUID, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(404, "User not found")
    return user
