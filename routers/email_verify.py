from fastapi import APIRouter, Depends,status
from fastapi.responses import HTMLResponse
from db import get_db
import models
from sqlalchemy.orm import Session
from utils.exceptions import APIException
from JWTtoken import verify_email_token

apirouter= APIRouter(tags=["Email Verification"])

@apirouter.get("/verify-email")
def verify_email(token: str,db:Session=Depends(get_db)):
    try:
        email=verify_email_token(token)
    except Exception:
        raise APIException(400,"Bhai Invalid Token Hai")
    user = db.query(models.User).filter(models.User.email == email).first()
    if not user:
        raise APIException(404, "Bhai User Nahi Mila")
    if user.is_verified:
        return HTMLResponse("Bhai Email Pehle Se Hi Verify Ho Chuka Hai")
    user.is_verified = True
    db.commit()
    return HTMLResponse("Bhai Email Verify Ho Gaya Hai")