from django.db import models


class PricePrediction(models.Model):
    HORIZON_CHOICES = [("1h", "1시간"), ("24h", "24시간"), ("7d", "7일")]

    created_at = models.DateTimeField(auto_now_add=True)
    horizon = models.CharField(max_digits=3, choices=HORIZON_CHOICES, max_length=3)
    predicted_price = models.DecimalField(max_digits=20, decimal_places=2)
    actual_price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    model_name = models.CharField(max_length=50)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.horizon} 예측={self.predicted_price} ({self.model_name})"
