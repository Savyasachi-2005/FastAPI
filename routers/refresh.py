from fastapi import APIRouter,HTTPException,Body
import JWTtoken

router=APIRouter(
    prefix="/refresh",
    tags=["REFRESH"]
)

@router.post('/')
def refresh_token(refresh_token:str =Body(...)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate":"Bearer"},
    )
    email=JWTtoken.verify_refresh_token(refresh_token,credentials_exception)
    new_access_token = JWTtoken.create_access_token(data={"sub":email})
    return {"access_token":new_access_token}