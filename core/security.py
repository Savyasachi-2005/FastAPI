from datetime import datetime, timedelta,timezone
from jose import jwt,JWTError

secret_key = "fwiuevuesbjkezdfshvjfwisbfsidjkfbsjk"
ALOGORITHM = "HS256"
access_token_expire_minutes = 15

def create_password_access_token(email:str) -> str :
    expire= datetime.now(timezone.utc)+timedelta(minutes=access_token_expire_minutes)
    payload={"sub":email,"exp":expire}
    return jwt.encode(payload,secret_key,algorithm=ALOGORITHM)

def verify_password_reset_token(token:str) -> str:
    try:
        payload = jwt.decode(token,secret_key,algorithms=[ALOGORITHM])
        return payload.get("sub")
    except JWTError:
        return None
    
