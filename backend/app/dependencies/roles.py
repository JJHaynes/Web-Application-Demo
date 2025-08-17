from .. import schemas
from ..api.routers.auth import get_current_user
from fastapi import Depends, HTTPException, status

def require_roles(*allowed_roles: str):
    def role_checker(current_user: schemas.user = Depends(get_current_user)):
        user_roles = {r.name for r in current_user.roles}
        if not (user_roles & set(allowed_roles)):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return current_user
    return role_checker

