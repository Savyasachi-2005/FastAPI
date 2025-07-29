from fastapi import APIRouter, Depends, HTTPException, status
from core.rbac import require_role
apirouter=APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@apirouter.get('/')
def admin_dashboard(current_user=Depends(require_role(['admin']))):
    return {"message": "Access granted to admin dashboard", "user": current_user.username}