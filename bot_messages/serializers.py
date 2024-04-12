import requests
from rest_framework import serializers

from bot_messages.models import Message, Session
from utils import email


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = (
            "request",
            "response",
            "session",
            "prompt_tokens",
            "response_tokens",
            "prompt_cost",
            "response_cost",
        )

    def create(self, validated_data):  # type: ignore
        USDBRL = float(self.get_dolar_value())
        instance = super().create(validated_data)
        instance.prompt_cost = (
            instance.prompt_tokens
            / 1000
            * instance.session.bot.model.input_price
            * USDBRL
            * (1 + 0.0438)
        )
        instance.response_cost = (
            instance.response_tokens
            / 1000
            * instance.session.bot.model.output_price
            * USDBRL
            * (1 + 0.0438)
        )
        instance.save()
        if instance.total_cost > 0:
            instance.session.user.debit(instance.session.bot.model.credits_cost)
        return instance

    def get_dolar_value(self) -> str:
        r = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL")
        return r.json()["USDBRL"]["bid"]


class SessionSerializer(serializers.ModelSerializer):

    messages = serializers.SerializerMethodField()

    def get_messages(self, obj):  # type: ignore
        return MessageSerializer(Message.objects.filter(session=obj), many=True).data

    def create(self, validated_data):  # type: ignore
        instance = super().create(validated_data)
        instance.user = instance.bot.user
        instance.save()
        return instance

    class Meta:
        model = Session
        fields = ("bot", "uuid", "id", "user", "messages")
        read_only_fields = ("id", "uuid", "user", "messages")
