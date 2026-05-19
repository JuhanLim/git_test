from django.urls import path
from . import views

urlpatterns = [
    path("price/", views.CurrentPriceView.as_view(), name="current-price"),
    path("candles/", views.CandleListView.as_view(), name="candle-list"),
]
