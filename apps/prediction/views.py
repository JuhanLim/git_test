from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.market.models import PriceCandle
from .predictor import predict_next_price
from .models import PricePrediction


class PredictView(APIView):
    def get(self, request):
        horizon = request.query_params.get("horizon", "1h")
        steps_map = {"1h": 1, "24h": 24, "7d": 168}
        steps = steps_map.get(horizon, 1)

        prices = list(
            PriceCandle.objects.order_by("timestamp").values_list("close", flat=True)
        )
        if len(prices) < 5:
            return Response({"error": "데이터 부족"}, status=status.HTTP_400_BAD_REQUEST)

        prices_float = [float(p) for p in prices]
        predicted = predict_next_price(prices_float, steps_ahead=steps)

        PricePrediction.objects.create(
            horizon=horizon,
            predicted_price=predicted,
            model_name="LinearRegression",
        )
        return Response({"horizon": horizon, "predicted_price": round(predicted, 2)})
