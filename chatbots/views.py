from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from chatbots.models import * VoiceType
from chatbots.serializers import (
    ApiKeySerializer,
    BotTypeSerializer,
    ChatBotSerializer,
    ModelTypeSerializer,
    SearchTypeSerializer,
    ToneTypeSerializer,
    VoiceTypeSerializer,
)

# Create your views here.


class ChatBotGetDataView(APIView):
    def get(self, request) -> Response:  # type: ignore
        bot_types = BotTypeSerializer(
            BotTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        search_types = SearchTypeSerializer(
            SearchTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        model_types = ModelTypeSerializer(
            ModelTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        tone_types = ToneTypeSerializer(
            ToneTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        voice_types = VoiceTypeSerializer(
            VoiceTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        api_keys = ApiKeySerializer(
            ApiKeySerializer().Meta.model.objects.filter(owner=self.request.user),
            many=True,
        ).data

        data = {
            'types': bot_types,
            'search': search_types,
            'model': model_types,
            'tones': tone_types,
            'voices': voice_types,
            'api_keys': api_keys,
        }
        return Response(data)


class ChatBotViewSet(generics.CreateAPIView):
    serializer_class = ChatBotSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = ChatBotSerializer().Meta.model.objects.all()
    
   
    def get_queryset(self):  # type: ignore
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)


class ChatBotRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChatBotSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    queryset = ChatBotSerializer().Meta.model.objects.all()

    def get_queryset(self):  # type: ignore
        queryset = super().get_queryset()
        queryset = queryset.filter(bot_owner=self.request.user)
        return queryset
