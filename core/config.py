from pydantic import EmailStr
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()
class Settings(BaseSettings):
    MAIL_USERNAME: EmailStr
    MAIL_PASSWORD: str
    MAIL_FROM: EmailStr
    MAIL_PORT: int
    MAIL_SERVER:str
    MAIL_FROM_NAME:str
    
    class config:
        env_file = ".env"
    
settings=Settings()