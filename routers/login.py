from fastapi import APIRouter,Depends,HTTPException,status
import schemas,models,db,hashing
from hashing import Hash
from sqlalchemy.orm import Session
apirouter=APIRouter(
    prefix="/login",
    tags=["Login"]
)

@apirouter.post('/')
def login(request: schemas.Login,db:Session=Depends(db.get_db)):
    user=db.query(models.User).filter(models.User.name==request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="User not found")
        
    if not Hash.verify(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Incorrect Password")
    
    return user