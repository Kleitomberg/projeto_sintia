import requests
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import CreateAPIView

from bot_messages.models import Session
from bot_messages.serializers import MessageSerializer

# Create your views here.


class MessageCreateView(CreateAPIView):
    serializer_class = MessageSerializer
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):  # type: ignore
        data = {}

        if "message_session" in self.request.data.keys():
            data.message_session = Session.objects.get(
                id=self.request.data["message_session"],
            )
        else:
            data.message_session = Session.objects.create()

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return super().post(request, *args, **kwargs)

    def perform_create(self, serializer):  # type: ignore
        serializer.save()
        return super().perform_create(serializer)

    def get_response(self, data):  # type: ignore
        r = requests.post()
