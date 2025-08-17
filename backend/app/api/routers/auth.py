from fastapi import APIRouter, Depends, HTTPException, status, BackgroundTasks
from sqlalchemy.orm import Session
from ... import schemas, crud
from ...core.security import create_access_token
from ...core.email import send_verification_email
from ...core.exceptions import InvalidTokenError
from ...dependencies.auth import get_db, get_current_user
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/signup", response_model=schemas.UserRead)
def signup(user_in: schemas.UserCreate, bg: BackgroundTasks, db: Session = Depends(get_db)):
    if crud.user.get_user_by_email(db, user_in.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    user = crud.user.create_user(db, user_in)
    token = crud.user.create_email_verification_token(db, user)
    send_verification_email(bg, user.email, token)
    return user

@router.post("/login", response_model=schemas.Token)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.user.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not db_user.is_active:
        raise HTTPException(status_code=401, detail="You must activate your account first")
    access_token = create_access_token({"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/token", response_model=schemas.Token)
def login_oauth(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
    ):
    db_user = crud.user.authenticate_user(db, form_data.username, form_data.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    if not db_user.is_active:
        raise HTTPException(status_code=401, detail="You must activate your account first")
    access_token = create_access_token({"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=schemas.UserRead)
def read_users_me(current_user: schemas.UserRead = Depends(get_current_user)):
    return current_user

@router.get("/verify-email", response_model=schemas.VerifyEmailResponse)
def verify_email(token: str, db: Session = Depends(get_db)):
    try:
        user = crud.user.verify_email_token(db, token)
    except InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")
    return user

@router.post("/resend-verification", status_code=status.HTTP_200_OK)
def resend_verification(form_in: schemas.ResendVerification, bg: BackgroundTasks, db: Session = Depends(get_db)):
    user = crud.user.get_user_by_email(db, form_in.email.lower())
    if user and not user.is_active:
        token = crud.user.create_email_verification_token(db, user, overwrite=True)
        send_verification_email(bg, user.email, token)
    return {"msg": "If that account exists, a verification email has been sent."}

