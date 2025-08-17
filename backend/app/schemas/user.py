from typing import Optional, List
from pydantic import BaseModel, EmailStr
from uuid import UUID
from .role import Role

class UserLogin(BaseModel):
    email: str
    password: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class ActivateUser(BaseModel):
    id: UUID
    is_active: bool

class ResendVerification(BaseModel):
    email: EmailStr

class VerifyEmailResponse(BaseModel):
    id: UUID
    email: EmailStr
    is_active: bool

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    is_active: Optional[bool] = None
    role_ids: Optional[List[int]] = None

class UserRead(BaseModel):
    id: UUID
    email: EmailStr
    roles: List[Role]
    is_active: bool

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
