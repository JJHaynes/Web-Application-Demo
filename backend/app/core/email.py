from fastapi import BackgroundTasks
from ..config.settings import settings

def send_verification_email(bg: BackgroundTasks, to_email: str, token: str):
    verify_url = f"{settings.APP_URL}/auth/verify-email?token={token}"
    subject = "Activate your account"
    body = (
        f"Welcome! Please click the link to verify your email:\n\n"
        f"{verify_url}\n\n"
        f"This link expires in {settings.VERIFICATION_TOKEN_TTL_HOURS} hours."
    )
    bg.add_task(_placeholder, to_email, subject, body)

def _placeholder(to, subject, body):
    # Swap this out for real email code (SMTP, SES, SendGrid, etc.)
    print(f"[EMAIL to={to}]\nSubject: {subject}\n\n{body}")
