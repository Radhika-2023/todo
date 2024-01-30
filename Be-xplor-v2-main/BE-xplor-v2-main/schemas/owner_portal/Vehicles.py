from pydantic import BaseModel

# ------------------------------------ Vehicles ------------------------------------
class VehiclesBase(BaseModel):
    id: int
    org_id: int
    reg_no: str
    driver_user_id: int
    vehicle_capacity: int

    class Config:
        orm_mode = True


class CreateVehicle(VehiclesBase):
    class Config:
        orm_mode = True


class CreateVehicleRequest(BaseModel):
    id: int
    org_id: int
    reg_no: str
    driver_user_id: int
    vehicle_capacity: int