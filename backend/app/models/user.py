import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..db import Base, TimestampMixin
from .user_roles import user_roles

class User(Base, TimestampMixin):
    __tablename__ = "users"

    id             = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email          = Column(String(200), unique=True, nullable=False)
    password_hash  = Column(String(128), nullable=False)
    is_active      = Column(Boolean, default=False, nullable=False)

    # Many-to-many → roles
    roles          = relationship("Role", secondary=user_roles, back_populates="users")

    # One-to-many → if a charity-admin, which charity they belong to
    # Not sure about this - feels strange.
    charity_id     = Column(
                        UUID(as_uuid=True),
                        ForeignKey("charities.id", ondelete="SET NULL"),
                        nullable=True
                     )
    charity        = relationship("Charity", back_populates="admins")

    # Purchases, notifications & audit logs
    audit_logs              = relationship("AuditLog", back_populates="actor")
    email_tokens = relationship("EmailVerificationToken", back_populates="user", cascade="all, delete-orphan")

