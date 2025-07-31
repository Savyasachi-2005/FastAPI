from fastapi import APIRouter,Depends
import schemas,models,db,hashing,JWTtoken
from hashing import Hash
from utils.exceptions import APIException
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
        raise APIException(400,"Bhai email pahele se register hai")
    
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
    