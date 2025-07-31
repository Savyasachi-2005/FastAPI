from jose import JWTError,jwt
from datetime import datetime, timedelta,timezone
import schemas
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

REFRESH_SECRET_KEY = "faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e709d25e094"
REFRESH_ALGORITHM = "HS256"
REFRESH_TOKEN_EXPIRE_DAYS = 30

EMAIL_SECRET_KEY = "a9563b93f7099f6f0f4caa6cf63b88e8d3e709d25e094faa6ca2556c818166b7"
EMAIL_ALGORITHM = "HS256"
EMAIL_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data:dict):
    to_encode=data.copy()
    expire= datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({
        "exp": expire
    })
    encode_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encode_jwt

def verify_token(data:str,credentials_exception):
    try:
        payload=jwt.decode(data,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        role:str = payload.get("role")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=email, role=role)
    except JWTError:
        raise credentials_exception
    return token_data

def create_refresh_tokens(data:dict):
    to_encode=data.copy();
    expire=datetime.now(timezone.utc)+timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    to_encode.update({
        "exp":expire,
        "role":data.get("role","user")
        })
    return jwt.encode(to_encode,REFRESH_SECRET_KEY,algorithm=REFRESH_ALGORITHM)

def verify_refresh_token(data:str,credentials_exception):
    try:
        payload=jwt.decode(data,REFRESH_SECRET_KEY,algorithms=[REFRESH_ALGORITHM])
        email:str=payload.get("sub")
        role:str=payload.get("role")
        if email is None or role is None:
            raise credentials_exception
        return schemas.TokenData(username=email, role=role)
    except jwt.JWTError:
        raise credentials_exception

def create_email_token(email:str):
    expire=datetime.now(timezone.utc)+timedelta(minutes=EMAIL_TOKEN_EXPIRE_MINUTES)
    payload = {
        "sub":email,
        "exp":expire
    }
    return jwt.encode(payload, EMAIL_SECRET_KEY, algorithm=EMAIL_ALGORITHM)

def verify_email_token(token:str):
    try:    
        payload= jwt.decode(token, EMAIL_SECRET_KEY, algorithms = [EMAIL_ALGORITHM])
        email:str=payload.get("sub")
        if email is None:
            raise ValueError("Invalid token")
        return email
    except JWTError:
        raise ValueError("Invalid or Expired token")
