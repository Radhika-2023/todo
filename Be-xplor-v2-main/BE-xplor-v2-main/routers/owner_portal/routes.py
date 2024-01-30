from typing import List
from fastapi import HTTPException, Depends
from flask import sessions
from sqlalchemy.orm import Session
from starlette import status
import models
from schemas.owner_portal import Routes
from fastapi import APIRouter
from database import get_db

router = APIRouter(
    prefix='/erp',
    tags=["Vehicles"]

)

# -- 5. Get all Routes
@router.get("/routes/all", response_model=List[models.Route], status_code=status.HTTP_200_OK)
def get_all_routes(db: Session = Depends(get_db)):
    routes = db.query(models.Route).all()
    return routes