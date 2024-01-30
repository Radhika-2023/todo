from typing import List
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Locations
from fastapi import APIRouter
from database import get_db

from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix='/location',
    tags=['Location']
)

# -- 1. Create New Location
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=List[Locations.CreateLocation])
def create_location(create_location_request:Locations.CreateLocation, db: Session = Depends(get_db)):
    new_location = models.Locations(**create_location_request.model_dump())
    db.add(new_location)
    db.commit()
    db.refresh(new_location)

    return [new_location]


# -- 2. Edit Location
@router.put('/{request_id}', response_model=Locations.CreateLocation)
def update_location(update_location_req: Locations.LocationsBase, request_id: int, db: Session = Depends(get_db)):
    existing_location = db.query(models.Locations).filter(models.Locations.id == request_id)

    if existing_location.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The id:{request_id} does not exist")

    existing_location.update(update_location_req.dict(), synchronize_session=False)
    db.commit()

    return existing_location


# -- 3. Delete Location
@router.delete('/{request_id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_location(request_id: int, db: Session = Depends(get_db)):
    deleted_location = db.query(models.Locations).filter(models.Locations.id == request_id)
    if deleted_location.first() is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {request_id} you requested for does not exist")
    deleted_location.delete(synchronize_session=False)
    db.commit()


# -- 4. Get Single Location
@router.get('/{request_id}', response_model=Locations.CreateLocation, status_code=status.HTTP_200_OK)
def get_one_location(request_id: int, db: Session = Depends(get_db)):
    db_entry = db.query(models.Locations).filter(models.Locations.id == request_id).first()

    if db_entry is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"The id: {request_id} you requested for does not exist")
    return db_entry


# -- 5. Get all Locations
@router.get('/', response_model=List[Locations.LocationsBase])
def get_all_locations(db: Session = Depends(get_db)):
    return db.query(models.Locations).all()