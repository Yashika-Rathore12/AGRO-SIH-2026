
# AgroConnect AI — SIH 2026 Architecture

```text
Farmer / Sensor / Market Feed
          |
          v
  Responsive PWA Frontend
  HTML + CSS + Vanilla JS
          |
          v
       FastAPI
  REST API + Validation
     /      |       \
    v       v        v
SQLite   AI Engine  Forecast
    \       |        /
     \      |       /
      v     v      v
      Advisory + Market Linkage
               |
               v
       Buyer + Logistics Match
```

## Why this is SIH-friendly

- Clear mapping from problem statement to working modules.
- Simple enough to run locally during judging.
- Modular enough to migrate to cloud services.
- Offline-first behavior is visible in the UI.
- Explainable advisory output instead of unexplained black-box recommendations.
- AI service is isolated behind an API-compatible function, making model replacement easy.
- Market and buyer modules create an end-to-end farm-to-market story instead of stopping at disease detection.

## Production upgrade path

- SQLite -> PostgreSQL + TimescaleDB
- Local image storage -> S3/Azure Blob/GCP Cloud Storage
- FastAPI process -> Docker + Kubernetes/Azure Container Apps
- Demo AI adapter -> MobileNetV3/EfficientNet trained on PlantVillage + local field images
- Forecast baseline -> XGBoost/LightGBM/LSTM with weather, soil, crop stage and historical mandi features
- Manual seed data -> Agmarknet/official mandi feeds where legally and technically available
- LocalStorage queue -> IndexedDB + background sync
- No-auth demo -> OAuth2/JWT + role based access
- Background jobs -> Celery/RQ + Redis
- Alerts -> Firebase Cloud Messaging / Web Push
- Observability -> structured logging + Prometheus/Grafana
