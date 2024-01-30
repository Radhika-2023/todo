import datetime

from pydantic import BaseModel
from datetime import datetime


# ------------------------------------ Vehicle_route_mapping ------------------------------------
class Vehicle_route_mapping(BaseModel):
    id = int
    vehicle_id = int
    route_id = int

    class Config:
        orm_mode = True


class CreateVehicle_route_mapping(Vehicle_route_mappingBase):
    class Config:
        orm_mode = True

class CreateVehicle_route_mappingRequest(BaseModel):
    id = int
    vehicle_id = int
    route_id = int