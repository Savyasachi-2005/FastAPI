from fastapi import FastAPI
from db import engine,get_db,base
from routers import blog,user,login
app=FastAPI()
base.metadata.create_all(bind=engine)

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(login.apirouter)

