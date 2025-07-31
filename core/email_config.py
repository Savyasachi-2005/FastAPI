from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import EmailStr
from core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_FROM_NAME=settings.MAIL_FROM_NAME,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,

    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)
fm=FastMail(conf)

async def send_email(email_to: EmailStr,verification_link: str):
    body = f"""
    Welcome to Sparsha! 🐾
    
    Please click the link below to verify your email:
    {verification_link}
    
    Thanks for joining our community ❤️
    """
    msg=MessageSchema(
        subject="Hello from team Sparsha",
        recipients=[email_to],
        body=body,
        subtype="plain"
    )
    await fm.send_message(msg)