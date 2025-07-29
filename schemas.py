from pydantic import BaseModel
from typing import List, Optional
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
    
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    username: Optional[str]=None