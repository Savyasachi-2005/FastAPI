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
    role:str="user"
    
class userShow(BaseModel):
    name:str
    email:str
    id:int
    role:str="user"
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
    role: Optional[str]=None
    
class HospitalCreate(BaseModel):
    name:str

class HospitalResponse(BaseModel):
    id:int
    name:str
    class Config:
        from_attributes=True
        
class passwordResetRequest(BaseModel):
    email:str

class passwordResetConfirm(BaseModel):
    token:str
    new_password:str
    
