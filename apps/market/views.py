from rest_framework.views import APIView
from rest_framework.response import Response
from .models import PriceCandle
from .serializers import PriceCandleSerializer
from .services import get_current_price


class CurrentPriceView(APIView):
    def get(self, request):
        return Response(get_current_price())


class CandleListView(APIView):
    def get(self, request):
        limit = int(request.query_params.get("limit", 100))
        qs = PriceCandle.objects.all()[:limit]
        return Response(PriceCandleSerializer(qs, many=True).data)
