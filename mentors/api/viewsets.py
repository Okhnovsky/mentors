from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from users.models import CustomUser
from .serializers import (ListUserSerialiser, UserSerializer,
                          UpdateUserSerializer)
from .permissions import UpdateUserPermission


class CustomUserViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):

    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ListUserSerialiser
        if self.action == "retrieve":
            return UserSerializer
        if self.action == "partial_update":
            return UpdateUserSerializer

    def get_permissions(self):
        if self.action == "partial_update":
            return [UpdateUserPermission()]
        else:
            return [IsAuthenticated()]
