from typing import Optional
from pydantic import BaseModel

class RoleRead(BaseModel):
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class RoleCreate(RoleRead):
    name: str
    description: Optional[str] = None

class RoleUpdate(RoleRead):
    name: Optional[str] = None
    description: Optional[str] = None

class Role(BaseModel):
    name: str