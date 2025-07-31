from fastapi import APIRouter,Depends
import schemas,models,db,hashing,JWTtoken
from hashing import Hash
from utils.exceptions import APIException
from sqlalchemy.orm import Session
from db import get_db
from JWTtoken import create_email_token
from core.email_config import send_email
import asyncio
apirouter=APIRouter(
    prefix="/register",
    tags=["Login"]
)

@apirouter.post('/')
async def register(request:schemas.users,db:Session=Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    if existing_user:
        raise APIException(400,"Bhai email pahele se register hai")
    
    new_user = models.User(
        name=request.username,
        email=request.email,
        password=hashing.Hash.bcrypt(request.password),
        role=request.role,
        is_verified=False  # Default to False until email is verified
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    try:
        token= create_email_token(new_user.email)
        verification_link = f"http://localhost:8000/verify-email?token={token}"
        await send_email(email_to=new_user.email,verification_link=verification_link)
        return {"message": f"User {new_user.name} registered successfully, role: {new_user.role}. Please check your email for verification."}
    except Exception as e:
        # If email fails, still create user but inform about email issue
        return {"message": f"User {new_user.name} registered successfully, but email verification failed. Please contact support."}
    