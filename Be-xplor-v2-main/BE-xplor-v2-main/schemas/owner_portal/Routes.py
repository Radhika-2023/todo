import datetime

from pydantic import BaseModel
from datetime import datetime


# ------------------------------------ Routes ------------------------------------
class Routes(BaseModel):
    id = int
    org_id = int
    created_by = int
    ticket_prices = float
    
    class Config:
        orm_mode = True


class CreateRoutes(RoutesBase):
    class Config:
        orm_mode = True


class CreateRoutesRequest(BaseModel):
    id = int
    org_id = int
    created_by = int
    ticket_prices = float