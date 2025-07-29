from sqlalchemy.orm import Session
import models,db,schemas
from models import Blog, User
from fastapi import APIRouter,Depends,Response, status, HTTPException


def create(request: schemas.Blog,db:Session = Depends(db.get_db)):
    user = db.query(User).filter(User.id == 1).first()
    if not user:
        # Create dummy user with id=1
        user = User(name="Test User", email="test@example.com", password="password")
        db.add(user)
        db.commit()
        db.refresh(user)

    # Now create the blog with user_id=1
    new_blog = Blog(title=request.title, body=request.body, user_id=user.id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show(id,response:Response,db:Session=Depends(db.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first()
    if  not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    return blog

def destroy(id,db:Session=Depends(db.get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {"detail":"Blog deleted successfully" }

def update(id,request:schemas.Blog,db:Session=Depends(db.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).update({'title':request.title, 'body': request.body}, synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with the id {id} is not found")
    db.commit()
    return 'Updated successfully'