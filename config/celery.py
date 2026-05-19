import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

app = Celery("bitcoin_predict")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# 주기적 데이터 수집: 5분마다 시세 갱신
app.conf.beat_schedule = {
    "fetch-bitcoin-price": {
        "task": "apps.market.tasks.fetch_and_store_price",
        "schedule": 300.0,
    },
}
