from pathlib import Path
from fastapi import FastAPI, Depends, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from PIL import Image
from io import BytesIO

from .database import Base, engine, get_db
from .models import Farmer, Farm, Telemetry, Advisory, DiseaseScan
from .schemas import FarmerCreate, FarmCreate, TelemetryCreate, AdvisoryRequest, ForecastRequest, BuyerMatchRequest
from .seed import seed
from .services.ai_service import analyze_leaf
from .services.advisory_service import generate_advisory
from .services.forecast_service import price_forecast, yield_forecast
from .services.market_service import match_buyers, latest_market

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

app = FastAPI(
    title="AgroConnect AI",
    version="1.0.0",
    description="SIH 2026 prototype for multimodal agro-advisory and market linkage."
)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)
    seed()

@app.get("/", response_class=HTMLResponse)
def home():
    return (STATIC_DIR / "index.html").read_text(encoding="utf-8")

@app.get("/api/health")
def health():
    return {"status": "ok", "service": "AgroConnect AI"}

@app.get("/api/dashboard")
def dashboard(db: Session = Depends(get_db)):
    farmer = db.query(Farmer).first()
    farm = db.query(Farm).first()
    telemetry = db.query(Telemetry).order_by(Telemetry.id.desc()).first()
    market = latest_market(db, farm.crop if farm else "Wheat")
    return {
        "farmer": {"id": farmer.id, "name": farmer.name, "village": farmer.village, "language": farmer.language} if farmer else None,
        "farm": {"id": farm.id, "crop": farm.crop, "area_acres": farm.area_acres, "soil_type": farm.soil_type} if farm else None,
        "telemetry": {
            "soil_moisture": telemetry.soil_moisture,
            "temperature": telemetry.temperature,
            "humidity": telemetry.humidity,
            "nitrogen": telemetry.nitrogen,
            "phosphorus": telemetry.phosphorus,
            "potassium": telemetry.potassium,
        } if telemetry else None,
        "market": [
            {"crop": x.crop, "mandi": x.mandi, "price": x.price, "arrival_tonnes": x.arrival_tonnes, "date": x.date}
            for x in market
        ]
    }

@app.post("/api/farmers")
def create_farmer(payload: FarmerCreate, db: Session = Depends(get_db)):
    farmer = Farmer(**payload.model_dump())
    db.add(farmer)
    db.commit()
    db.refresh(farmer)
    return {"id": farmer.id, "message": "Farmer profile created"}

@app.post("/api/farms")
def create_farm(payload: FarmCreate, db: Session = Depends(get_db)):
    farm = Farm(**payload.model_dump())
    db.add(farm)
    db.commit()
    db.refresh(farm)
    return {"id": farm.id, "message": "Farm saved"}

@app.post("/api/telemetry")
def ingest_telemetry(payload: TelemetryCreate, db: Session = Depends(get_db)):
    row = Telemetry(**payload.model_dump())
    db.add(row)
    db.commit()
    db.refresh(row)
    return {"id": row.id, "message": "Telemetry stored", "timestamp": row.timestamp}

@app.post("/api/advisory")
def advisory(payload: AdvisoryRequest, db: Session = Depends(get_db)):
    result = generate_advisory(payload)
    row = Advisory(
        farm_id=payload.farm_id,
        type="soil-irrigation",
        severity=result["severity"],
        title=f"{payload.crop} advisory",
        message=" ".join(result["actions"])
    )
    db.add(row)
    db.commit()
    return result

@app.post("/api/ai/disease")
async def disease_scan(
    farm_id: int = 1,
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    if image.content_type not in {"image/jpeg", "image/png", "image/webp"}:
        raise HTTPException(400, "Upload JPG, PNG or WEBP image.")
    data = await image.read()
    if len(data) > 8 * 1024 * 1024:
        raise HTTPException(413, "Image must be smaller than 8 MB.")
    try:
        pil = Image.open(BytesIO(data))
        result = analyze_leaf(pil)
    except Exception as exc:
        raise HTTPException(400, f"Could not process image: {exc}")

    row = DiseaseScan(
        farm_id=farm_id,
        filename=image.filename or "leaf.jpg",
        diagnosis=result["diagnosis"],
        confidence=result["confidence"],
        explanation=result["explanation"]
    )
    db.add(row)
    db.commit()
    return result

@app.post("/api/forecast")
def forecast(payload: ForecastRequest):
    return {
        "crop": payload.crop,
        "yield": yield_forecast(payload.crop, payload.area_acres),
        "price": price_forecast(payload.crop)
    }

@app.get("/api/market")
def market(crop: str = "Wheat", db: Session = Depends(get_db)):
    rows = latest_market(db, crop)
    return {"crop": crop, "prices": [
        {"mandi": r.mandi, "price": r.price, "arrival_tonnes": r.arrival_tonnes, "date": r.date}
        for r in rows
    ]}

@app.post("/api/buyers/match")
def buyers(payload: BuyerMatchRequest, db: Session = Depends(get_db)):
    return {
        "crop": payload.crop,
        "quantity_tonnes": payload.quantity_tonnes,
        "matches": match_buyers(db, payload.crop, payload.quantity_tonnes, payload.target_price)
    }
