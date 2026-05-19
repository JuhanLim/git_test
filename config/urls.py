from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.dashboard.urls")),
    path("api/market/", include("apps.market.urls")),
    path("api/prediction/", include("apps.prediction.urls")),
]
