from fastapi import APIRouter, Depends, HTTPException, status
from oauth2 import get_current_user
from schemas import TokenData
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def require_role(required_role: list[str]):
    def role_checker(current_user: TokenData = Depends(get_current_user)):
        logger.debug(f"User role: {current_user.role}")
        logger.debug(f"Required roles: {required_role}")
        
        if not current_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not authenticated",
                headers={"WWW-Authenticate": "Bearer"}
            )
        
        if current_user.role not in required_role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Access denied. Required roles: {required_role}, User role: {current_user.role}",
                headers={"WWW-Authenticate": "Bearer"}
            )
            
        return current_user
    return role_checker