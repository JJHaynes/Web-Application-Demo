from sqlalchemy.orm import Session
from uuid import UUID
from .. import schemas, models
from fastapi import HTTPException, status

def create_charity(
        db: Session,
        owner_id: UUID,
        charity_in:schemas.charity.CharityCreate)->models.Charity:

    # noinspection PyArgumentList
    charity = models.Charity(
        name=charity_in.name,
        description=charity_in.description,
        logo_url=charity_in.logo_url,
        bank_account=charity_in.bank_account,
    )
    db.add(charity)
    db.commit()
    db.refresh(charity)
    return charity

def update_charity_by_id(
        db: Session,
        charity_id: UUID,
        updated_by_id: UUID,
        charity_in:schemas.charity.CharityUpdate
):
    charity = db.query(models.Charity).filter(models.Charity.id == charity_id).first()

    if not charity:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Charity not found")

    update_data = charity_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(charity, field, value)

    db.add(charity)
    db.commit()
    db.refresh(charity)
    return charity

def list_charities(db:Session, skip: int = 0, limit: int = 100):
    return db.query(models.Charity).offset(skip).limit(limit).all()

