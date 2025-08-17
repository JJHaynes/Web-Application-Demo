import uuid
from sqlalchemy import Column, ForeignKey, String, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from ..db import Base, TimestampMixin

class AuditLog(Base, TimestampMixin):
    __tablename__ = "audit_logs"

    id          = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    actor_id    = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"))
    action      = Column(String(50), nullable=False)
    entity_type = Column(String(50), nullable=False)
    entity_id   = Column(UUID(as_uuid=True), nullable=False)
    details     = Column(JSON)

    actor = relationship("User", back_populates="audit_logs")