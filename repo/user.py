from fastapi import APIRouter, Depends, Response, status, HTTPException
from sqlalchemy.orm import Session
import models,db,schemas
from models import Blog,User
from db import get_db
from passlib.context import CryptContext


pwd_cxt=CryptContext(schemes=["bcrypt"],deprecated="auto")
def create_user(request:schemas.users,db:Session=Depends(get_db)):
    hashed_pwd=pwd_cxt.hash(request.password)
    new_user=models.User(name=request.username,email=request.email,password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db:Session=Depends(get_db)):
    user=db.query(models.User).all()
    return [schemas.userShow.from_orm(us) for us in user]