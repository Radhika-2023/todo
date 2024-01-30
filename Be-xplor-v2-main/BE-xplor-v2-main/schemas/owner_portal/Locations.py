import datetime
from typing import Union

from pydantic import BaseModel
from datetime import datetime


# ------------------------------------ Locations ------------------------------------
class LocationsBase(BaseModel):
    id: Union[int, None] = None
    name: str
    org_id: int
    latitude: float
    longitude: float
    is_active: Union[bool, None] = None
    created_at: Union[datetime, None] = None
    updated_at: Union[datetime, None] = None

    class Config:
        orm_mode = True


class CreateLocation(LocationsBase):
    class Config:
        orm_mode = True


class CreateLocationRequest(BaseModel):
    name: str
    org_id: int
    latitude: float
    longitude: float