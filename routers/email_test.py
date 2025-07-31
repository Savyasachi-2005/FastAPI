from fastapi import APIRouter
from core.email_config import send_email
from pydantic import EmailStr

apirouter = APIRouter(
    prefix="/email",
    tags=["Email"]
)

@apirouter.post("/")
async def send_email_endpoint(email: EmailStr):
    await send_email(email_to=email)
    return f"Email sent to {email} successfully."

