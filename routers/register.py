from fastapi import APIRouter,Depends,HTTPException,status
import schemas,models,db,hashing,JWTtoken
from hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db import get_db
apirouter=APIRouter(
    prefix="/register",
    tags=["Login"]
)

@apirouter.post('/')
def register(request:schemas.users,db:Session=Depends(get_db)):
    existing_user = db.query(models.User).filter(models.User.email == request.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already registered")
    
    new_user = models.User(
        name=request.username,
        email=request.email,
        password=hashing.Hash.bcrypt(request.password),
        role=request.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": f"User {new_user.name} registered successfully, role: {new_user.role}"}
    