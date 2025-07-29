from sqlalchemy import Column,Integer,String,ForeignKey
from db import base
from sqlalchemy.orm import relationship
class Blog(base):
    __tablename__='blog'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    body=Column(String,nullable=False)
    user_id=Column(Integer,ForeignKey('users.id'))
    creator=relationship('User',back_populates='blogs')
    
class User(base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    role=Column(String,default='user')
    blogs=relationship('Blog',back_populates='creator')
