from typing import Any

from rest_framework import status, viewsets
from rest_framework.response import Response

from base.permissions import PostCreateOrAuthenticated
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [PostCreateOrAuthenticated]
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()

    def update(self, request: dict, *args: Any, **kwargs: Any) -> Any:  # type: ignore
        if request.user == UserSerializer.Meta.model.objects.get(pk=kwargs["pk"]):
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request: dict, *args: Any, **kwargs: Any) -> Any:  # type: ignore
        if request.user == UserSerializer.Meta.model.objects.get(pk=kwargs["pk"]):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)
