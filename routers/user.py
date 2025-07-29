from fastapi import APIRouter,Depends,Response, status, HTTPException
from sqlalchemy.orm import Session
import models,db,schemas,oauth2
from models import Blog, User
from db import get_db
from passlib.context import CryptContext
from repo import user as user_repo
router=APIRouter(
    prefix="/users",
    tags=['Users']
)




@router.post('/',status_code=status.HTTP_201_CREATED)
def create_user(request:schemas.users,db:Session=Depends(get_db),get_current_user: schemas.users =Depends(oauth2.get_current_user)):
    return user_repo.create_user(request,db);

@router.get('/',status_code=200,response_model=list[schemas.userShow])
def get_user(db:Session=Depends(get_db),get_current_user: schemas.users =Depends(oauth2.get_current_user)):
    return user_repo.get_user(db);