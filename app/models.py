from datetime import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime, Text

from .database import Base

class Farmer(Base):
    __tablename__ = "farmers"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    village = Column(String(120), default="")
    language = Column(String(10), default="en")
    phone = Column(String(30), default="")
    created_at = Column(DateTime, default=datetime.utcnow)

class Farm(Base):
    __tablename__ = "farms"
    id = Column(Integer, primary_key=True)
    farmer_id = Column(Integer, default=1)
    crop = Column(String(80), nullable=False)
    area_acres = Column(Float, default=1.0)
    sowing_date = Column(String(30), default="")
    soil_type = Column(String(80), default="Loamy")

class Telemetry(Base):
    __tablename__ = "telemetry"
    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer, default=1)
    soil_moisture = Column(Float)
    temperature = Column(Float)
    humidity = Column(Float)
    nitrogen = Column(Float)
    phosphorus = Column(Float)
    potassium = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

class MarketPrice(Base):
    __tablename__ = "market_prices"
    id = Column(Integer, primary_key=True)
    crop = Column(String(80), nullable=False)
    mandi = Column(String(120), nullable=False)
    price = Column(Float, nullable=False)
    arrival_tonnes = Column(Float, default=0)
    date = Column(String(30), nullable=False)

class Buyer(Base):
    __tablename__ = "buyers"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
    location = Column(String(120), default="")
    crops = Column(String(300), default="")
    demand_tonnes = Column(Float, default=0)
    offered_price = Column(Float, default=0)
    distance_km = Column(Float, default=0)
    logistics_available = Column(Integer, default=1)

class Advisory(Base):
    __tablename__ = "advisories"
    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer, default=1)
    type = Column(String(80), nullable=False)
    severity = Column(String(30), default="info")
    title = Column(String(200), nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

class DiseaseScan(Base):
    __tablename__ = "disease_scans"
    id = Column(Integer, primary_key=True)
    farm_id = Column(Integer, default=1)
    filename = Column(String(200), default="")
    diagnosis = Column(String(120), nullable=False)
    confidence = Column(Float, default=0)
    explanation = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.utcnow)
