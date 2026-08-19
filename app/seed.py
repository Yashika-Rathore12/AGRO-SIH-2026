from .database import Base, engine, SessionLocal
from .models import Farmer, Farm, Telemetry, MarketPrice, Buyer

def seed():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        if db.query(Farmer).count() == 0:
            farmer = Farmer(name="Demo Farmer", village="Huzurganj", language="en", phone="")
            db.add(farmer)
            db.commit()
            db.refresh(farmer)
            db.add(Farm(farmer_id=farmer.id, crop="Wheat", area_acres=2.5, sowing_date="2026-11-10", soil_type="Loamy"))
            db.add(Telemetry(farm_id=1, soil_moisture=42, temperature=27, humidity=64, nitrogen=48, phosphorus=23, potassium=36))

            market_rows = [
                ("Wheat", "Bhopal Mandi", 2520, 420, "2026-08-19"),
                ("Wheat", "Indore Mandi", 2590, 510, "2026-08-19"),
                ("Wheat", "Sehore Mandi", 2550, 280, "2026-08-19"),
                ("Rice", "Bhopal Mandi", 2920, 390, "2026-08-19"),
                ("Soybean", "Indore Mandi", 4820, 620, "2026-08-19"),
                ("Maize", "Sehore Mandi", 2260, 240, "2026-08-19"),
            ]
            for row in market_rows:
                db.add(MarketPrice(crop=row[0], mandi=row[1], price=row[2], arrival_tonnes=row[3], date=row[4]))

            buyers = [
                ("GreenBasket Foods", "Bhopal", "Wheat,Rice,Maize", 30, 2650, 42, 1),
                ("Central Agro Traders", "Indore", "Wheat,Soybean", 50, 2620, 165, 1),
                ("FarmerDirect Foods", "Sehore", "Wheat,Maize", 20, 2580, 70, 1),
                ("MP Grain Hub", "Vidisha", "Wheat,Rice", 40, 2560, 95, 1),
            ]
            for b in buyers:
                db.add(Buyer(name=b[0], location=b[1], crops=b[2], demand_tonnes=b[3], offered_price=b[4], distance_km=b[5], logistics_available=b[6]))
            db.commit()
    finally:
        db.close()
