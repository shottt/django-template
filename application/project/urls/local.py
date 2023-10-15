"""ローカル環境用のルーティング"""
from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from project.urls.base import urlpatterns

urlpatterns += [
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # SwaggerUIの設定
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Redocの設定
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
