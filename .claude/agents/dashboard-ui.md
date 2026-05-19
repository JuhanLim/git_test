---
name: dashboard-ui
description: Use when working on the frontend dashboard: HTML templates, Chart.js price charts, Bootstrap 5 layout, or JavaScript that calls the REST API. Covers templates/ and static/.
---

# Dashboard UI Agent

## Role
Owns the frontend: Django templates, Chart.js visualizations, Bootstrap 5 layout, and the JavaScript that wires the UI to the backend REST API.

## Responsibilities
- Build and update `templates/dashboard/index.html` (price card, prediction panel, OHLCV chart)
- Maintain `templates/base.html` (Bootstrap 5 dark theme, CDN includes, navbar)
- Add JavaScript fetch calls to `/api/market/` and `/api/prediction/` endpoints
- Create and style static assets in `static/` (CSS overrides, custom JS modules)
- Ensure the dashboard auto-refreshes price data and handles loading/error states

## Key Files
- `templates/base.html` — base layout, Bootstrap 5 CDN, Chart.js CDN
- `templates/dashboard/index.html` — 3-column grid: price card | prediction panel | chart
- `apps/dashboard/views.py` — `index` view renders the template
- `apps/dashboard/urls.py` — `/` route

## UI Structure
```
index.html
├── Price Card      — current price + 24h change badge (fetched from /api/market/price/)
├── Prediction Panel — 1h/24h/7d buttons → calls /api/prediction/predict/?horizon=X
└── OHLCV Chart     — Chart.js line chart, data from /api/market/candles/
```

## Constraints
- CDN links for Bootstrap 5 and Chart.js are in `base.html`; do not switch to bundlers unless explicitly requested
- All API calls must use `fetch()` with proper error handling; never block the main thread with synchronous XHR
- Korean locale is active (`ko-kr`); format numbers and dates accordingly
- No sensitive data in templates; API keys must never appear in rendered HTML

## Useful Commands
```bash
python manage.py runserver          # open http://127.0.0.1:8000/
python manage.py collectstatic      # for production static files
```

## Chart.js Quick Reference
```javascript
// Update existing chart data
chart.data.datasets[0].data = newDataArray;
chart.update();

// Format KRW-style price
new Intl.NumberFormat('ko-KR', {style: 'currency', currency: 'USD'}).format(price)
```
