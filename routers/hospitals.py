from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from models import Hospital, User
from schemas import HospitalCreate, HospitalResponse



router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)
@router.post("/",response_model=HospitalResponse)
def create_hospital(request:HospitalCreate, db: Session = Depends(get_db)):
    hospital=Hospital(name=request.name)
    db.add(hospital)
    db.commit()
    db.refresh(hospital)
    return hospital

@router.get("/{hospital_id}/doctors/{user_id}")
def get_hospital(hospital_id: int,user_id: int,db:Session = Depends(get_db)):
    hospital=db.query(Hospital).filter(Hospital.id == hospital_id).first()
    if not hospital:
        raise HTTPException(status_code = 404,detail="Hospital not found")
    doctor = db.query(User).filter(User.id == user_id).first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    if doctor.role != "doctor":
        raise HTTPException(status_code=400, detail="User is not a doctor")
    if doctor not in hospital.doctors:
        hospital.doctors.append(doctor)
        db.commit()
        
    return {"message": f"Doctor {doctor.name} added to Hospital {hospital.name}"}
