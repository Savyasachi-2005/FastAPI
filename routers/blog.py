
from fastapi import APIRouter,Depends,Response, status, HTTPException
from sqlalchemy.orm import Session
import models,db,schemas
from db import get_db
from repo import blog


router=APIRouter(
    prefix="/blogs",
    tags=['Blogs']
)

@router.get('/')
def get_all(db:Session=Depends(db.get_db)):
    blogs=db.query(models.Blog).all()
    return blogs

@router.post('/', status_code=status.HTTP_201_CREATED, )
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    # Check if user with id=1 exists
    return blog.create(request,db);
    

@router.get('/id',status_code=200,response_model=schemas.showBlog)
def show(id,response:Response,db:Session=Depends(get_db)):
    return blog.show(id,response,db);

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session=Depends(get_db)):
    return blog.destroy(id,db);

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def update(id,request:schemas.Blog,db:Session=Depends(get_db)):
    return blog.update(id,request,db);