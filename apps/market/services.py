"""CoinGecko API 래퍼. 외부 HTTP 호출은 이 모듈에서만 한다."""

import requests
from django.conf import settings


COINGECKO_BASE = "https://api.coingecko.com/api/v3"


def _headers() -> dict:
    h = {"Accept": "application/json"}
    if settings.COINGECKO_API_KEY:
        h["x-cg-demo-api-key"] = settings.COINGECKO_API_KEY
    return h


def get_current_price() -> dict:
    """Bitcoin 현재 USD 가격과 24h 변동률 반환."""
    url = f"{COINGECKO_BASE}/simple/price"
    params = {
        "ids": "bitcoin",
        "vs_currencies": "usd",
        "include_24hr_change": "true",
    }
    resp = requests.get(url, params=params, headers=_headers(), timeout=10)
    resp.raise_for_status()
    data = resp.json()["bitcoin"]
    return {"price_usd": data["usd"], "change_24h": data["usd_24h_change"]}


def get_ohlcv(days: int = 30) -> list[dict]:
    """일봉 OHLCV 데이터. days 최대 90 (무료 티어)."""
    url = f"{COINGECKO_BASE}/coins/bitcoin/ohlc"
    params = {"vs_currency": "usd", "days": days}
    resp = requests.get(url, params=params, headers=_headers(), timeout=15)
    resp.raise_for_status()
    # [[timestamp_ms, open, high, low, close], ...]
    return [
        {"timestamp_ms": row[0], "open": row[1], "high": row[2], "low": row[3], "close": row[4]}
        for row in resp.json()
    ]
