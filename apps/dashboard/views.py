from django.shortcuts import render
from apps.market.services import get_current_price


def index(request):
    try:
        price_data = get_current_price()
    except Exception:
        price_data = {"price_usd": "N/A", "change_24h": 0}
    return render(request, "dashboard/index.html", {"price": price_data})
