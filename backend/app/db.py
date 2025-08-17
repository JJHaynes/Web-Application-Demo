import os
from sqlalchemy import create_engine, Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Get your database URL from an environment variable (fallback to a default)
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://postgres:password@localhost:5432/charity-lottery-dev"
)

# Create the engine
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,
)

# Create a configured "Session" class
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

# Base class for all models to inherit
Base = declarative_base()

class TimestampMixin:

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

def get_db():
    """
    FastAPI dependency that yields a SQLAlchemy Session,
    then closes it when the request is done.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()