---
name: add-api-service
description: Add a new external API data source (e.g. Binance, CryptoCompare) following the project's services.py encapsulation pattern.
---

# Skill: Add API Service

Add an external API integration to `apps/market/services.py` following project conventions.

## Steps

1. **Add credentials to `.env.example`** (and your local `.env`):
   ```
   NEW_API_KEY=
   NEW_API_SECRET=
   ```

2. **Read credentials in `config/settings.py`** via django-environ:
   ```python
   NEW_API_KEY = env('NEW_API_KEY', default='')
   ```

3. **Write the service function in `apps/market/services.py`**:
   ```python
   import httpx
   from django.conf import settings

   def get_<source>_price() -> dict:
       """Fetch current BTC price from <Source> API."""
       url = 'https://api.<source>.com/...'
       headers = {'X-API-Key': settings.NEW_API_KEY}
       response = httpx.get(url, headers=headers, timeout=10)
       response.raise_for_status()
       data = response.json()
       return {
           'price': float(data['price']),
           'timestamp': data['time'],
       }
   ```
   - Use `httpx` (already in requirements) for HTTP calls
   - Always set `timeout=10`; let `raise_for_status()` propagate HTTP errors
   - Return a plain dict; no ORM calls inside service functions

4. **Call from a Celery task** in `apps/market/tasks.py` if periodic collection is needed:
   ```python
   from .services import get_<source>_price

   @shared_task
   def fetch_<source>_price():
       data = get_<source>_price()
       PriceCandle.objects.create(**data)
   ```

5. **Register the Beat schedule** in `config/celery.py` if it should run automatically.

6. **Write a test** in `apps/market/tests/test_services.py` using `responses` or `httpx` mock.

## Checklist
- [ ] `.env.example` updated
- [ ] `settings.py` reads the new env var
- [ ] Service function is in `services.py`, not in views or tasks
- [ ] `raise_for_status()` called on every response
- [ ] API key never hardcoded
- [ ] Test added
