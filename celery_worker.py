from celery import Celery
from fastapi_mail import MessageSchema
from core.email_config import fm
celery_app = Celery(
    "Worker",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)


@celery_app.task(name="celery_worker.send_email_task")
def send_email_task(email_to: str,verfication_link:str):
    link="http://localhost:8000/email_verify?token="+verfication_link
    html_body = f""" 
        <h2>Verify your email</h2>
        <p>Welcome to Sparsha! 🐾</p>
        <a href="{link}" style="background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px;">Verify Email</a>
        <p>Thanks for joining our community ❤️</p>
    """
    msg=MessageSchema(
        subject="Hello from team Sparsha",
        recipients=[email_to],
        body=html_body,
        subtype="html"
    )
    import asyncio
    loop=asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(fm.send_message(msg))
    loop.close()