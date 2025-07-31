from sqlalchemy import Column,Integer,String,ForeignKey,Table
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
    
    hospital_management= relationship(
        'Hospital',
        secondary='doctor',
        back_populates='doctors'
    )
    
doctor_table = Table(
    'doctor',
    base.metadata,
    Column('user_id',Integer, ForeignKey('users.id'), primary_key=True),
    Column('hospital_id',Integer, ForeignKey('hospitals.id'), primary_key=True)
)

class Hospital(base):
    __tablename__='hospitals'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    
    doctors = relationship(
        'User',
        secondary=doctor_table,
        back_populates='hospital_management'
    )
