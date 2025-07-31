from fastapi import FastAPI,Depends,Request
from sqlalchemy.orm import Session
from db import engine,get_db,base
from routers import blog,user,login,refresh,admin,hospitals,register,email_test,email_verify
from repo import user as user_repo
import schemas,models
from utils.exceptions import APIException
from fastapi.responses import JSONResponse
from core.middleware import HeaderMiddleware ,CustomASGIMiddleware
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.trustedhost import TrustedHostMiddleware
from core.config import settings
app=FastAPI()
base.metadata.create_all(bind=engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*",],
    allow_headers=["*"]
)
app.add_middleware(TrustedHostMiddleware,
                   allowed_hosts=["*"])
app.add_middleware(CustomASGIMiddleware)
app.add_middleware(HeaderMiddleware)
@app.exception_handler(APIException)
async def api_exception_handler(request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "success": False,
            "message": exc.detail
        },
    )

print("Loaded Email",settings.MAIL_USERNAME)

app.include_router(admin.apirouter)
app.include_router(register.apirouter)
app.include_router(login.apirouter)
app.include_router(email_test.apirouter)
app.include_router(email_verify.apirouter)
app.include_router(refresh.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(hospitals.router)
