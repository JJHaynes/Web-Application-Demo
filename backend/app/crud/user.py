from uuid import UUID
import uuid
from sqlalchemy.orm import Session
from .. import models, schemas
from ..core.security import hash_password, verify_password
from ..core.exceptions import InvalidTokenError
from fastapi import HTTPException, status
from datetime import datetime, timedelta
from ..config.settings import settings

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user_by_id(db: Session, user_id: UUID):
    return db.query(models.User).get(user_id)

def list_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def activate_user(db: Session, user_id: UUID) -> models.User:
    activation_in = schemas.user.UserUpdate(is_active=True)
    return update_user(db, user_id, activation_in)

def create_user(db: Session, user_in: schemas.user.UserCreate):

    try:
        # Setting a Default Role
        participant = db.query(models.Role).filter(models.Role.name == "participant").first()
        if not participant:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Default role ‘participant’ not found. Seed your roles table."
            )

        # noinspection PyArgumentList
        db_user = models.User(
            email=user_in.email.lower(),
            password_hash=hash_password(user_in.password),
            is_active = False
        )

        # Adding default role to the user
        db_user.roles.append(participant)

        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    except Exception as e:
        db.rollback()
        raise e

def update_user(db: Session,
                user_id: UUID,
                user_in: schemas.user.UserUpdate):
    try:
        user = get_user_by_id(db, user_id)
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

        update_data = user_in.model_dump(exclude_unset=True)

        if "password" in update_data:
            user.password_hash = hash_password(update_data.pop("password"))

        if "role_ids" in update_data:
            roles = db.query(models.Role).filter(models.Role.id.in_(update_data["role_ids"])).all()
            user.roles = roles
            update_data.pop("role_ids")

        for field, value in update_data.items():
            setattr(user, field, value)

        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    except Exception as e:
        db.rollback()
        raise e

def authenticate_user(db: Session, email: str, password: str):
    user = get_user_by_email(db, email.lower())
    if not user or not verify_password(password, user.password_hash):
        return None
    return user

def create_email_verification_token(db: Session, user: models.User, overwrite: bool = False) -> str:
    # Optionally invalidate old tokens
    if overwrite:
        db.query(models.EmailVerificationToken) \
          .filter_by(user_id=user.id, is_used=False) \
          .update({"is_used": True})

    token = uuid.uuid4().hex
    expires = datetime.utcnow() + timedelta(hours=settings.VERIFICATION_TOKEN_TTL_HOURS)

    db_token = models.EmailVerificationToken(
        user_id=user.id,
        token=token,
        expires_at=expires
    )
    db.add(db_token)
    db.commit()
    return token

def verify_email_token(db: Session, token: str):
    now = datetime.utcnow()
    db_token = (
        db.query(models.EmailVerificationToken)
          .filter_by(token=token, is_used=False)
          .filter(models.EmailVerificationToken.expires_at >= now)
          .first()
    )
    if not db_token:
        raise InvalidTokenError(token)

    # Mark token used & activate user
    db_token.is_used = True
    user = db_token.user
    user.is_active = True
    db.add_all((db_token, user))
    db.commit()
    return user