from fastapi import APIRouter, Depends, status, Request
from fastapi.responses import HTMLResponse
from db import get_db
import models
from sqlalchemy.orm import Session
from utils.exceptions import APIException
from JWTtoken import verify_email_token
import logging

# Set up logging
logger = logging.getLogger(__name__)

apirouter = APIRouter(tags=["Email Verification"])

@apirouter.get("/verify-email")
def verify_email(token: str, request: Request, db: Session = Depends(get_db)):
    logger.info(f"✅ Reached verify-email endpoint with token: {token[:10]}...")
    logger.info(f"📡 Request URL: {request.url}")
    logger.info(f"🔍 Query params: {request.query_params}")

    if not token:
        logger.error("❌ No token provided")
        raise APIException(400, "Token is required")

    try:
        email = verify_email_token(token)
        logger.info(f"📧 Email extracted from token: {email}")
    except Exception as e:
        logger.error(f"❌ Token verification failed: {str(e)}")
        raise APIException(400, f"Invalid or expired token: {str(e)}")

    user = db.query(models.User).filter(models.User.email == email).first()
    logger.info(f"👤 User lookup result: {user.email if user else 'Not found'}")

    if not user:
        logger.error(f"❌ User not found for email: {email}")
        raise APIException(404, "User not found")

    if user.is_verified:
        logger.info(f"🔁 User {email} already verified")
        return HTMLResponse("""
            <html>
                <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
                    <h2>✅ Email Already Verified</h2>
                    <p>Your email has already been verified. You can now log in to your account.</p>
                    <a href="/login" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Go to Login</a>
                </body>
            </html>
        """)

    user.is_verified = True
    db.commit()
    logger.info(f"✅ Email verified successfully for user: {email}")

    return HTMLResponse("""
        <html>
            <body style="font-family: Arial, sans-serif; text-align: center; padding: 50px;">
                <h2>🎉 Email Verified Successfully!</h2>
                <p>Your email has been verified. You can now log in to your account.</p>
                <a href="/login" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Go to Login</a>
            </body>
        </html>
    """)
