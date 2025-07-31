from fastapi import APIRouter,Depends
import schemas,models,db,hashing,JWTtoken
from hashing import Hash
from utils.exceptions import APIException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import get_db
apirouter=APIRouter(
    prefix="/login",
    tags=["Login"]
)

@apirouter.post('/')
def login(request:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user=db.query(models.User).filter(models.User.email==request.username).first()
    if not user:
        raise APIException(404,"Bhai email register nahi hai")
        
    if not Hash.verify(request.password,user.password):
        raise APIException(400,"Bhai password galat hai")
    if not user.is_verified:
        raise APIException(400,"Bhai email verify nahi hua hai")
    access_token=JWTtoken.create_access_token(data={"sub":user.email,"role":user.role})
    refresh_token=JWTtoken.create_refresh_tokens(data={"sub":user.email,"role":user.role})
    return {"access_token": access_token,"refresh_token":refresh_token,"token_type":"bearer","role":user.role}