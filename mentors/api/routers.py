from rest_framework.routers import SimpleRouter
from djoser.views import UserViewSet

from .viewsets import CustomUserViewSet


router = SimpleRouter()
router.register("registration", UserViewSet)
router.register("users", CustomUserViewSet, basename="users")


routers = router.urls
