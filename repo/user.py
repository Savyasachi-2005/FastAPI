from fastapi import Depends
from sqlalchemy.orm import Session
import models,db,schemas,hashing
from models import Blog,User
from db import get_db




def create_user(request:schemas.users,db:Session=Depends(get_db)):
    hashed_pwd=hashing.Hash.bcrypt(request.password)
    new_user=models.User(name=request.username,email=request.email,password=hashed_pwd, role=request.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user(db:Session=Depends(get_db)):
    user=db.query(models.User).all()
    return [schemas.userShow.from_orm(us) for us in user]

def delete(user_id:int=None,db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return {"message":"User not found"}
    db.delete(user)
    db.commit()
    return {"message": f"{user.name} deleted successfully"}