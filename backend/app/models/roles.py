from sqlalchemy import Column, String, Text, Integer
from sqlalchemy.orm import relationship
from ..db import Base, TimestampMixin
from .user_roles import user_roles

class Role(Base, TimestampMixin):
    __tablename__ = "roles"

    id          = Column(Integer, primary_key=True, autoincrement=True)
    name        = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    users = relationship( "User", secondary=user_roles, back_populates="roles")