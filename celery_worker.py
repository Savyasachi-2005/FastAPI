from celery import Celery
from fastapi_mail import MessageSchema
from core.email_config import fm
import logging

# Set up logging
logger = logging.getLogger(__name__)

celery_app = Celery(
    "Worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@celery_app.task(name="celery_worker.send_email_task", bind=True)
def send_email_task(self, email_to: str, verification_link: str):
    try:
        # Use environment variable or config for base URL
        import os
        base_url = os.getenv("BASE_URL", "http://localhost:8000")
        link = f"{base_url}/verify-email?token={verification_link}"
        
        html_body = f""" 
            <h2>Verify your email</h2>
            <p>Welcome to Sparsha! 🐾</p>
            <a href="{link}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Verify Email</a>
            <p>Thanks for joining our community ❤️</p>
            <p>If the button doesn't work, copy and paste this link: {link}</p>
        """
        
        msg = MessageSchema(
            subject="Hello from team Sparsha",
            recipients=[email_to],
            body=html_body,
            subtype="html"
        )
        
        # Proper async handling
        import asyncio
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        try:
            loop.run_until_complete(fm.send_message(msg))
            logger.info(f"✅ Email sent successfully to {email_to}")
            return {"status": "success", "email": email_to}
        finally:
            if loop.is_running():
                loop.close()
                
    except Exception as e:
        logger.error(f"❌ Failed to send email to {email_to}: {str(e)}")
        # Retry the task up to 3 times
        if self.request.retries < 3:
            raise self.retry(countdown=60, max_retries=3)
        return {"status": "failed", "email": email_to, "error": str(e)}