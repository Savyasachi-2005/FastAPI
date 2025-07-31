from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from utils.exceptions import APIException
from models import Hospital, User
from schemas import HospitalCreate, HospitalResponse
from core.rbac import require_role



router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)
@router.post("/",response_model=HospitalResponse)
def create_hospital(request:HospitalCreate, db: Session = Depends(get_db),current_user: User= Depends(require_role("admin"))):
    hospital=Hospital(name=request.name)
    db.add(hospital)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.get("/{hospital_id}/doctors/{user_id}")
def get_hospital(hospital_id: int,user_id: int,db:Session = Depends(get_db),current_user: User= Depends(require_role("admin"))):
    hospital=db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise APIException(404, "arrey bhai hospital nahi hai")
    doctor = db.query(User).filter(User.id == user_id).first()
    if not doctor:
        raise APIException(404, "arrey bhai doctor nahi hai")
    if doctor.role != "doctor":
        raise APIException(400, "arrey bhai user doctor nahi hai")
    if doctor not in hospital.doctors:
        hospital.doctors.append(doctor)
        db.commit()
        
    return {"message": f"Doctor {doctor.name} added to Hospital {hospital.name}"}
