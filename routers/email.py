# from fastapi import APIRouter
# from celery_worker import send_welcome_email
# router=APIRouter(
#     prefix="/email",
#     tags=["email"]
# )

# @router.post("/")
# async def send_email(email_to: str):
#     send_welcome_email.delay(email_to)
#     return {"message": f"Email sent to {email_to} successfully."}
 