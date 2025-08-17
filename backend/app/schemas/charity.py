from xmlrpc.client import DateTime

from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from ..models.charity import Charity, CharityStatus

class CharityCreate(BaseModel):
    name: str
    description: Optional[str] = None
    logo_url: Optional[str] = None
    bank_account: Optional[str] = None

class CharityUpdate(BaseModel):
    description: Optional[str] = None
    logo_url: Optional[str] = None
    hero_image_url: Optional[str] = None
    bank_account: Optional[str] = None
    status: Optional[CharityStatus] = None

class CharityRead(BaseModel):
    id: UUID
    name: str
    status: CharityStatus
    description: Optional[str] 
    hero_image_url: Optional[str]