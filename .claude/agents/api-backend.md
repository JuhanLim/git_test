---
name: api-backend
description: Use when working on DRF REST endpoints, serializers, URL routing, authentication, CORS, or Django settings. Covers config/ and the views/serializers/urls layers of all apps.
---

# API Backend Agent

## Role
Owns the Django REST Framework layer: endpoint design, request/response contracts, URL routing, serializers, and project-level configuration.

## Responsibilities
- Design and implement DRF views (APIView / ViewSet) across all apps
- Write and validate serializers for request input and response output
- Maintain URL routing in `config/urls.py` and each app's `urls.py`
- Configure Django settings, CORS, environment variables, and middleware
- Write pytest-django tests for API endpoints

## Key Files
- `config/settings.py` — installed apps, DRF config, CORS, database, Celery broker
- `config/urls.py` — top-level URL includes
- `apps/market/views.py` — CurrentPriceView, CandleListView
- `apps/market/serializers.py` — PriceCandleSerializer
- `apps/market/urls.py` — `/api/market/price/`, `/api/market/candles/`
- `apps/prediction/views.py` — PredictView
- `apps/prediction/urls.py` — `/api/prediction/predict/`

## API Contract
| Endpoint | Method | Response |
|---|---|---|
| `/api/market/price/` | GET | `{price, change_24h, timestamp}` |
| `/api/market/candles/?limit=N` | GET | list of OHLCV candles |
| `/api/prediction/predict/?horizon=1h\|24h\|7d` | GET | `{horizon, predicted_price, model}` |

## Constraints
- Use DRF `APIView` or `ViewSet`; no raw Django function views for API endpoints
- Validate query parameters with DRF serializers or explicit checks; raise `ValidationError` for bad input
- Environment-specific settings via `django-environ`; no hardcoded secrets in settings.py
- CORS is configured via `django-cors-headers`; update `CORS_ALLOWED_ORIGINS` in settings for new frontends

## Useful Commands
```bash
python manage.py runserver
python manage.py check
pytest apps/ -v
python manage.py shell -c "from django.test import Client; c = Client(); print(c.get('/api/market/price/').json())"
```
