from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import get_db
import models

router = APIRouter(prefix="/erp", tags=["Vehicles"])


@router.get("/{request_id}", response_model=models.Vehicle, status_code=status.HTTP_200_OK)
def get_one_vehicle(request_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Vehicle).filter(models.Vehicle.id == request_id).first()

    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {request_id} you requested for does not exist")
    return db_entry


@router.get("/vehicles/services", response_model=List[models.Service])
def get_vehicle_services(vehicle_id: int, db: Session = Depends(get_db)):
    services = db.query(models.Service).filter(models.Service.vehicle_id == vehicle_id).all()
    if not services:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No services found for this vehicle")
    return services
