from typing import Any

from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from base.permissions import OwnProfilePermission
from chatbots import serializers
from chatbots.models import ChatBot

from customizations import serializers as custom_serializers
from customizations import models as custom_models


class ChatBotViewSet(viewsets.ModelViewSet):
    queryset = ChatBot.objects.all()
    serializer_class = serializers.ChatBotSerializer
    permission_classes = [IsAuthenticated, OwnProfilePermission]

    def get_queryset(self):  # type: ignore
        user = self.request.user
        return self.queryset.filter(user=user)

    def update(self, request: dict, *args: Any, **kwargs: Any) -> Any:
        if (
            request.user
            == serializers.ChatBotSerializer.Meta.model.objects.get(
                pk=kwargs["pk"],
            ).user
        ):
            return super().update(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def destroy(self, request: dict, *args: Any, **kwargs: Any) -> Any:
        if (
            request.user
            == serializers.ChatBotSerializer.Meta.model.objects.get(
                pk=kwargs["pk"],
            ).user
        ):
            return super().destroy(request, *args, **kwargs)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def list(self, request, *args, **kwargs):  # type: ignore
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = serializers.ChatBotDetailSerialer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = serializers.ChatBotDetailSerialer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):  # type: ignore
        instance = self.get_object()
        serializer = serializers.ChatBotDetailSerialer(instance)
        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def bot_data(self, request: dict) -> dict:
        bot_types = serializers.BotTypeSerializer(
            serializers.BotTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        search_types = serializers.SearchTypeSerializer(
            serializers.SearchTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        model_types = serializers.ModelTypeSerializer(
            serializers.ModelTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        tone_types = serializers.ToneTypeSerializer(
            serializers.ToneTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        voice_types = serializers.VoiceTypeSerializer(
            serializers.VoiceTypeSerializer().Meta.model.objects.all(),
            many=True,
        ).data
        api_keys = serializers.ApiKeySerializer(
            serializers.ApiKeySerializer().Meta.model.objects.filter(
                owner=self.request.user,
            ),
            many=True,
        ).data

        fonts = custom_serializers.PropertySerializer(
            custom_models.fontFamilies.objects.all(), many=True
        ).data
        sides = custom_serializers.PropertySerializer(
            custom_models.screenSides.objects.all(), many=True
        ).data
        colors = custom_serializers.PropertySerializer(
            custom_models.colors.objects.all(), many=True
        ).data

        data = {
            "types": bot_types,
            "search": search_types,
            "model": model_types,
            "tones": tone_types,
            "voices": voice_types,
            "api_keys": api_keys,
            "fonts": fonts,
            "sides": sides,
            "colors": colors,
        }
        return Response(data)
