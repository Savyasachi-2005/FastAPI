from fastapi import FastAPI,Depends,Request
from sqlalchemy.orm import Session
from db import engine,get_db,base
from routers import blog,user,login,refresh,admin,hospitals,register
from repo import user as user_repo
import schemas,models
from utils.exceptions import APIException
from fastapi.responses import JSONResponse
app=FastAPI()

base.metadata.create_all(bind=engine)


@app.exception_handler(APIException)
async def api_exception_handler(request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        },
    )


app.include_router(admin.apirouter)
app.include_router(register.apirouter)
app.include_router(login.apirouter)
app.include_router(refresh.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(hospitals.router)
