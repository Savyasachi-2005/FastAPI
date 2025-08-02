from fastapi_mail import MessageSchema
from fastapi import BackgroundTasks
from core.client import fm

async def send_reset_email(email_to:str,reset_link:str):
    msg=MessageSchema(
        subject="Password Reset Request",
        recipients=[email_to],
        body=f"""
        Hi there,

        You requested a password reset. Please click the link below to reset your password:
        {reset_link}

        If you did not request this, please ignore this email.

        Best regards,
        Your Team
        """,
        subtype="html"
    )
    await fm.send_message(msg)