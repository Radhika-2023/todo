import datetime

from pydantic import BaseModel
from datetime import datetime


# ------------------------------------ Vehicle_route_schedule ------------------------------------
class VVehicle_route_scheduleBase(BaseModel):
    id = int
    vehicle_id = int
    route_id = int
    location_id = int
    location_time = datetime

    class Config:
        orm_mode = True


class CreateVehicle_route_schedule(Vehicle_route_scheduleBase):
    class Config:
        orm_mode = True


class CreateVehicle_route_scheduleRequest(BaseModel):
    id = int
    vehicle_id = int
    route_id = int
    location_id = int
    location_time = datetime