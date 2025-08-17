from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status
from ..schemas import RoleCreate

def get_role_by_name(db: Session, name:str):
    return db.query(models.Role).filter(models.Role.name == name).first()

def create_role(db: Session, role_in: schemas.role.RoleCreate):

    # noinspection PyArgumentList
    role = models.Role(
        name=role_in.name,
        description=role_in.description
    )
    db.add(role)
    db.commit()
    db.refresh(role)

    return role

def update_role(db: Session,
                role_id: int,
                role_in: schemas.role.RoleUpdate):

    role = db.query(models.Role).filter(models.Role.id == role_id).first()

    if not role:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Role not found")

    update_data = role_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(role, field, value)

    db.add(role)
    db.commit()
    db.refresh(role)
    return role
