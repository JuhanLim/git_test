from django.db import models


class PriceCandle(models.Model):
    """1분봉 OHLCV 데이터."""

    timestamp = models.DateTimeField(db_index=True)
    open = models.DecimalField(max_digits=20, decimal_places=2)
    high = models.DecimalField(max_digits=20, decimal_places=2)
    low = models.DecimalField(max_digits=20, decimal_places=2)
    close = models.DecimalField(max_digits=20, decimal_places=2)
    volume = models.DecimalField(max_digits=30, decimal_places=8)

    class Meta:
        ordering = ["-timestamp"]
        unique_together = [("timestamp",)]

    def __str__(self):
        return f"BTC {self.timestamp:%Y-%m-%d %H:%M} close={self.close}"
