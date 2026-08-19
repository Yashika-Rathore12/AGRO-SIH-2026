from typing import Optional
from pydantic import BaseModel, Field

class FarmerCreate(BaseModel):
    name: str
    village: str = ""
    language: str = "en"
    phone: str = ""

class FarmCreate(BaseModel):
    farmer_id: int = 1
    crop: str
    area_acres: float = Field(gt=0)
    sowing_date: str = ""
    soil_type: str = "Loamy"

class TelemetryCreate(BaseModel):
    farm_id: int = 1
    soil_moisture: float
    temperature: float
    humidity: float
    nitrogen: float
    phosphorus: float
    potassium: float

class AdvisoryRequest(BaseModel):
    farm_id: int = 1
    crop: str = "Wheat"
    soil_moisture: float
    nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float = 28
    humidity: float = 60

class ForecastRequest(BaseModel):
    crop: str = "Wheat"
    area_acres: float = 2.0
    sowing_date: str = ""

class BuyerMatchRequest(BaseModel):
    crop: str
    quantity_tonnes: float
    target_price: float = 0
    village: str = ""
