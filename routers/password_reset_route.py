from fastapi import APIRouter,Depends,BackgroundTasks
from sqlalchemy.orm import Session
from schemas import passwordResetRequest, passwordResetConfirm
from db import get_db
from core.security import create_password_access_token,verify_password_reset_token
from utils.exceptions import APIException

from services.password_reset import send_reset_email
from models import User
from hashing import Hash

apirouter=APIRouter(
    tags=['Password Reset']
)

@apirouter.post('/request-password-reset')
async def request_password_reset(request: passwordResetRequest,bg:BackgroundTasks,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.email == request.email).first()
    if user :
        token = create_password_access_token(user.email)
        reset_link = f"http://localhost:8000/reset-password?token={token}"
        bg.add_task(send_reset_email, email_to=user.email, reset_link=reset_link)
    return {"message" : "If the email is registered, a password reset link has been sent to your email."}

@apirouter.post('/reset-password')
def reset_password(data: passwordResetConfirm,db:Session = Depends(get_db)):
    email= verify_password_reset_token(data.token)
    if not email:
        raise APIException(400,"Bhai token Invalid hai")
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise APIException(404,"Bhai user nahi mila")
    user.password=Hash.bcrypt(data.new_password)
    print("New hashed password:", user.password)

    db.add(user)
    db.commit()
    return {"message": "Bhai Congrats! Password reset ho gayaaaaa"}

    
    