from typing import List 
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Vehicles
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/erp/vehicle',
    tags=['Vehicle']
)


# -- 1. Create New vehicles
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[Vehicles.CreateVehicle])
def create_vehicle(request: Vehicles.CreateVehicle, db: Session = Depends(get_db)):
    new_vehicle = models.vehicles(**request.dict())
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return [new_vehicle]


# -- 2. Edit vehicles
# 
@router.put('/{request_id}', response_model=Vehicles.CreateVehicle)
def update_vehicle(update_vehicle_req: Vehicles.VehiclesBase, request_id: int, db: Session = Depends(get_db)):
    vehicle = db.query(models.Vehicles).filter(models.Vehicles.id == request_id).first()

    if vehicle is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{request_id} does not exist")
    
    # Update vehicle attributes
    for attr, value in update_vehicle_req.dict().items():
        setattr(vehicle, attr, value)

    db.commit()

    return vehicle



# -- 3. Delete vehicles
@router.delete('/{request_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_vehicle(request_id: int, db: Session = Depends(get_db)):
    deleted_vehicle = db.query(models.Vehicles).filter(models.Vehicles.id == request_id)
    if deleted_vehicle.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {request_id} you requested for does not exist")
    deleted_vehicle.delete(synchronize_session=False)
    db.commit()


# -- 4. Get Single vehicles
# @router.get('/{request_id}', response_model=VehicleRouteResponse, status_code=status.HTTP_200_OK)
# def get_one_vehicle(request_id: int, db: Session = Depends(get_db)):
#     db_entry = db.query(models.Routes).join(models.Vehicles).filter(models.Vehicles.id == request_id).first()

#     if db_entry is None:
#         raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
#                             detail=f"The id: {request_id} you requested for does not exist")
#     return db_entry

@router.get('/{request_id}', response_model=Vehicles.CreateVehicle, status_code=status.HTTP_200_OK)
def get_one_vehicle(request_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Vehicles).filter(models.Vehicles.id == request_id).first()


    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {request_id} you requested for does not exist")
    return db_entry


# -- 5. Get all vehicles
@router.get('/erp/vehicle/all', response_model=List[Vehicles.VehiclesBase])
def get_all_vehicles(db: Session = Depends(get_db)):
    return db.query(models.Vehicles).all()





