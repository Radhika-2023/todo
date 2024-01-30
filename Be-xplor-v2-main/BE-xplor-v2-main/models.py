from database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean, text, REAL, ForeignKey, Float, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.ext.declarative import declarative_base

class Organizations(Base):
    __tablename__ = "organizations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    is_active = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class Locations(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    org_id = Column(Integer, ForeignKey('organizations.id'), nullable=False)
    latitude = Column(REAL, nullable=False)
    longitude = Column(REAL, nullable=False)
    is_active = Column(Boolean, server_default='TRUE')
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))
    updated_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'))

class vehicles(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey('organizations.id'))
    reg_no = Column(String, unique=True, index=True)
    driver_user_id = Column(Integer, ForeignKey('users.id'))
    vehicle_capacity = Column(Integer)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_number = Column(String)
    type = Column(String)
    org_id = Column(Integer, ForeignKey('organizations.id'))

class Vehicle_route_mapping(Base):
    __tablename__ = "vehicle_route_mapping"

    id = Column(Integer, primary_key=True, index=True)  
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))

class vehicle_route_schedule(Base):
    __tablename__ = "vehicle_route_schedule"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    location_id = Column(Integer, ForeignKey('locations.id'))
    location_time = Column(DateTime)

class Routes(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    org_id = Column(Integer, ForeignKey('organizations.id'))
    created_by = Column(Integer, ForeignKey('users.id'))
    ticket_prices = Column(Float)

    