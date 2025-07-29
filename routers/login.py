from fastapi import APIRouter,Depends,HTTPException,status
import schemas,models,db,hashing,JWTtoken
from hashing import Hash
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
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
        
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Password")
    
    access_token=JWTtoken.create_access_token(data={"sub":user.email})
    return {"access_token": access_token,"token_type":"bearer"}