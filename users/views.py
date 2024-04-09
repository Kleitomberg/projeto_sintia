from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework import authentication  # type: ignore
from rest_framework import generics  # type: ignore
from rest_framework import permissions  # type: ignore
from rest_framework import status  # type: ignore
from rest_framework.exceptions import PermissionDenied  # type: ignore
from rest_framework.views import APIView, Response  # type: ignore

from users.serializers import UserSerializer, loginSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
    serializer_class = loginSerializer

    @extend_schema(
        request=loginSerializer,
        responses={
            200: OpenApiTypes.OBJECT,
            400: OpenApiTypes.OBJECT,
        },
    )
    def post(self, request):
        login = loginSerializer(data=request.data)
        if login.is_valid():
            return Response({'Token': login.validated_data.auth_token.key})
        else:
            return Response(
                {'error': 'Credenciais inválidas'},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return UserSerializer.Meta.model.objects.filter(id=self.request.user.id)


class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = UserSerializer.Meta.model.objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    # lookup_field = "id"

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        if self.request.user == user:
            return super().destroy(request, *args, **kwargs)
        else:
            raise PermissionDenied('Você não tem permissão para excluir este usuário')

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        if self.request.user == user:
            return super().update(request, *args, **kwargs)
        else:
            raise PermissionDenied('Você não tem permissão para editar este usuário')
