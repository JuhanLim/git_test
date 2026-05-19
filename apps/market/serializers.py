from rest_framework import serializers
from .models import PriceCandle


class PriceCandleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCandle
        fields = ["timestamp", "open", "high", "low", "close", "volume"]
