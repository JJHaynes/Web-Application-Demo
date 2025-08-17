from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ... import schemas
from ...crud.roles import create_role as crud_create_role
from ...crud.roles import update_role as crud_update_role
from ...dependencies.auth import get_db
from ...dependencies.roles import require_roles

router = APIRouter(prefix="/role", tags=["roles"])

@router.post("/add", response_model=schemas.RoleRead)
def create_role(role_in: schemas.RoleCreate,
                db: Session = Depends(get_db),
                _current_user=Depends(require_roles("super_admin"))):
    return crud_create_role(db, role_in)

@router.patch("/update", response_model=schemas.RoleRead)
def update_role(role_id: int,
                role_in: schemas.RoleUpdate,
                db: Session = Depends(get_db),
                _current_user = Depends(require_roles("super_admin"))):
    return crud_update_role(db, role_id, role_in)


