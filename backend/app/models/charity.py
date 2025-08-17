import enum
import uuid
from sqlalchemy import Column, String, Text, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..db import Base, TimestampMixin

class CharityStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"

class Charity(Base, TimestampMixin):
    __tablename__ = "charities"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name           = Column(String(200), nullable=False)
    description    = Column(Text)
    logo_url       = Column(String(300))
    hero_image_url = Column(String(300))
    bank_account   = Column(String(100))
    status         = Column(Enum(CharityStatus, name="charity_status"), default=CharityStatus.pending, nullable=False)

    # Charity can have multiple admins and lotteries
    admins        = relationship("User", back_populates="charity")
