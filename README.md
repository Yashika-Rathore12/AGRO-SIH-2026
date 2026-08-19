# AgroConnect AI — SIH 2026 Prototype

A simple, human-readable, cloud-ready Agro-Advisory & Market Linkage platform built with:

- Backend: Python + FastAPI
- Database: SQLite + SQLAlchemy
- Frontend: HTML + CSS + Vanilla JavaScript
- AI: pluggable disease classifier + lightweight yield/price forecasting
- Mobile/PWA: responsive UI, service worker, localStorage offline queue
- API: REST endpoints suitable for later GraphQL integration

## Core SIH problem coverage

1. Farmer registration/profile
2. Crop and farm records
3. Leaf image upload
4. AI disease analysis endpoint
5. Soil NPK recommendation
6. Irrigation recommendation using soil moisture + weather/telemetry
7. Microclimate and soil telemetry ingestion
8. Mandi price tracking
9. Harvest/yield window forecast
10. Buyer matching
11. Logistics recommendation
12. Multilingual English/Hindi UI
13. Offline-first advisory/telemetry queue
14. Dashboard with explainable recommendations

## Important AI note

The included disease engine is a DEMO inference adapter so the project runs without downloading a large model. It uses image statistics to demonstrate the complete AI pipeline and explicitly labels the result as a screening estimate.

For a final SIH submission, replace `app/services/ai_service.py`'s demo adapter with a trained PlantVillage/custom field-image model (for example a MobileNetV3/EfficientNet model) and save the model under `models/`. The API contract does not need to change.

The forecasting service is intentionally lightweight and deterministic so judges can run the project locally. It can later be replaced by XGBoost/LightGBM/LSTM/Temporal Fusion Transformer without changing the frontend.

## Run

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:
http://127.0.0.1:8000

API docs:
http://127.0.0.1:8000/docs

## Demo login

The prototype does not require authentication for a fast SIH demo. A production version should add OAuth2/JWT and role-based access for Farmer, Buyer, FPO, Admin and Logistics Partner.

## Suggested SIH demo flow

1. Open Dashboard and show crop health + telemetry.
2. Upload a leaf image and show disease screening.
3. Enter N/P/K and moisture; generate advisory.
4. Show mandi trends and predicted price.
5. Generate harvest forecast.
6. Match the forecast with buyers and logistics.
7. Turn browser offline and demonstrate queued telemetry/advisory actions.
8. Switch language to Hindi.

## Production architecture

Browser/PWA -> FastAPI API -> PostgreSQL/TimescaleDB -> AI model service -> Redis/Celery -> cloud object storage -> market/mandi feeds -> buyer/logistics services.

SQLite is used here because it is the simplest reliable local demo database.
