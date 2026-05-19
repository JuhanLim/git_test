from celery import shared_task
from .services import get_current_price


@shared_task
def fetch_and_store_price():
    """5분마다 Celery Beat이 호출. 현재가를 DB에 저장."""
    from django.utils import timezone
    from .models import PriceCandle

    data = get_current_price()
    PriceCandle.objects.update_or_create(
        timestamp=timezone.now().replace(second=0, microsecond=0),
        defaults={
            "open": data["price_usd"],
            "high": data["price_usd"],
            "low": data["price_usd"],
            "close": data["price_usd"],
            "volume": 0,
        },
    )
    return data
