from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .routers import routers


app_name = "api"


urlpatterns = [
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("logout/", TokenRefreshView.as_view(), name="logout"),
]

urlpatterns += routers
