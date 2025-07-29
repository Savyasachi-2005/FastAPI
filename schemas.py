from pydantic import BaseModel
from typing import List
class Blog(BaseModel):
    title:str
    body:str

     
class BlogC(Blog):
    class Config:
        from_attributes=True
class users(BaseModel):
    username:str
    email:str
    password:str
    
class userShow(BaseModel):
    name:str
    email:str
    id:int
    blogs:List[BlogC]=[]
    class Config:
        from_attributes=True
        
class showBlog(BaseModel):
    title:str
    body:str
    creator:userShow
    class config:
        from_attributes=True
        
class Login(BaseModel):
    username:str
    password:str