from datetime import date, timedelta

BASE_PRICES = {
    "Wheat": 2450,
    "Rice": 2850,
    "Soybean": 4700,
    "Cotton": 6900,
    "Maize": 2200,
    "Tomato": 1800
}

CROP_YIELD = {
    "Wheat": 1.7,
    "Rice": 2.1,
    "Soybean": 1.2,
    "Cotton": 1.0,
    "Maize": 2.4,
    "Tomato": 8.0
}

def price_forecast(crop):
    base = BASE_PRICES.get(crop, 2500)
    forecast = []
    for i in range(7):
        # Deterministic trend suitable for a repeatable demo.
        value = base * (1 + 0.012 * i - 0.002 * (i % 3))
        forecast.append({"day": i + 1, "expected_price": round(value, 0)})
    return forecast

def yield_forecast(crop, area_acres):
    base = CROP_YIELD.get(crop, 1.5)
    tonnes = base * area_acres
    return {
        "expected_yield_tonnes": round(tonnes, 2),
        "window_start_days": 7,
        "window_end_days": 18,
        "confidence": 74.0,
        "basis": "Crop baseline × farm area; replace with trained time-series model and local agronomic features for production."
    }
