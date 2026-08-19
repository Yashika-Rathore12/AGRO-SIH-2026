from sqlalchemy.orm import Session
from sqlalchemy import desc
from ..models import Buyer, MarketPrice

def match_buyers(db: Session, crop: str, quantity: float, target_price: float = 0):
    buyers = db.query(Buyer).all()
    results = []
    for b in buyers:
        crop_list = [x.strip().lower() for x in b.crops.split(",")]
        if crop.lower() not in crop_list:
            continue
        price_score = b.offered_price / max(target_price, 1) if target_price else 1
        demand_score = min(b.demand_tonnes / max(quantity, 1), 2) / 2
        distance_score = max(0, 1 - b.distance_km / 150)
        score = 0.55 * min(price_score, 1.25) / 1.25 + 0.30 * demand_score + 0.15 * distance_score
        results.append({
            "buyer_id": b.id,
            "buyer": b.name,
            "location": b.location,
            "offered_price": b.offered_price,
            "demand_tonnes": b.demand_tonnes,
            "distance_km": b.distance_km,
            "logistics_available": bool(b.logistics_available),
            "match_score": round(score * 100, 1)
        })
    return sorted(results, key=lambda x: x["match_score"], reverse=True)

def latest_market(db: Session, crop=None):
    q = db.query(MarketPrice)
    if crop:
        q = q.filter(MarketPrice.crop == crop)
    return q.order_by(desc(MarketPrice.id)).limit(20).all()
