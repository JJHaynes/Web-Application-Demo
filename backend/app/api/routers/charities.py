from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from uuid import UUID
from ...crud.charity import create_charity as crud_create_charity
from ...crud.charity import update_charity_by_id as crud_update_charity_by_id
from ...crud.charity import list_charities as crud_list_charities

from ...dependencies.auth import get_current_user
from ... import schemas, models
from ...db import get_db

router = APIRouter(prefix="/charities", tags=["charities"])

@router.post("/", response_model=schemas.charity.CharityRead, status_code=status.HTTP_201_CREATED,)
def create_charity(
        charity_in: schemas.charity.CharityCreate,
        db: Session = Depends(get_db),
        current_user: models.User = Depends(get_current_user)
):
    return crud_create_charity(db, current_user.id, charity_in)

@router.patch("/{charity_id}", response_model=schemas.charity.CharityRead, status_code=status.HTTP_200_OK)
def update_charity(
        charity_id: UUID,
        charity_in: schemas.charity.CharityUpdate,
        db: Session = Depends(get_db),
        current_user:  models.User = Depends(get_current_user)
):
    return crud_update_charity_by_id(db, charity_id, current_user.id, charity_in)

@router.get("/all", response_model=list[schemas.charity.CharityRead])
def list_charities(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    return crud_list_charities(db, skip, limit)

