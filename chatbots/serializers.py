from rest_framework import serializers
from customizations.serializers import SidesSerializer,FontSerializer

from chatbots.models import (
    ApiKey,
    BotType,
    ChatBot,
    ModelType,
    Scalations,
    SearchType,
    ToneType,
    VoiceType,
)


class BotTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BotType
        fields = (
            "name",
            "id",
        )


class SearchTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchType
        fields = (
            "name",
            "id",
        )


class ModelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelType
        fields = (
            "name",
            "id",
        )


class ToneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToneType
        fields = (
            "name",
            "id",
        )


class VoiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VoiceType
        fields = (
            "name",
            "id",
        )


class ApiKeySerializer(serializers.ModelSerializer):
    model = ModelTypeSerializer()

    class Meta:
        model = ApiKey
        fields = (
            "model",
            "id",
        )


class ChatBotSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = ChatBot
        fields = (
            "name",
            "id",
            "type",
            "api_key",
            "search",
            "model",
            "prompt",
            "language",
            "tone",
            "temperature",
            "material_core",
            "solar_url_host",
            "sources",
            "audio_response",
            "voice",
            "image_file",
            "user",
            "color",
            "font",
            "side",
        )
        read_only_fields = ("id", "user")
        extra_kwargs = {"material_core": {"write_only": True}}

    def create(self, validated_data):  # type: ignore
        
        instance = super().create(validated_data)
        instance.user = self.context["request"].user
        instance.search = SearchType.objects.get(value="brave")
        instance.save()
        return instance


class ScalationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scalations
        fields = ("name", "id", "value")
        read_only_fields = ("id",)


class ChatBotDetailSerialer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    type = BotTypeSerializer()
    model = ModelTypeSerializer()
    tone = ToneTypeSerializer()
    voice = VoiceTypeSerializer()
    prompt = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    temperature = serializers.SerializerMethodField()
    material_core = serializers.SerializerMethodField()
    solar_url_host = serializers.SerializerMethodField()
    sources = serializers.SerializerMethodField()
    audio_response = serializers.SerializerMethodField()
    image_file = serializers.SerializerMethodField()
    private = serializers.SerializerMethodField()
    published = serializers.SerializerMethodField()
    active = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    font = FontSerializer()
    side = SidesSerializer()

    def get_private(self, obj):  # type: ignore
        return obj.is_private

    def get_published(self, obj):  # type: ignore
        return obj.is_published

    def get_active(self, obj):  # type: ignore
        return obj.is_active

    def get_name(self, obj):  # type: ignore
        return obj.name

    def get_id(self, obj):  # type: ignore
        return obj.id

    def get_type(self, obj):  # type: ignore
        return obj.type.name

    def get_model(self, obj):  # type: ignore
        return obj.model.name

    def get_tone(self, obj):  # type: ignore
        return obj.tone.name

    def get_voice(self, obj):  # type: ignore
        if obj.voice:
            return obj.voice.name
        else:
            return None

    def get_prompt(self, obj):  # type: ignore
        return obj.prompt

    def get_language(self, obj):  # type: ignore
        return obj.language

    def get_temperature(self, obj):  # type: ignore
        return obj.temperature

    def get_material_core(self, obj):  # type: ignore
        if obj.material_core:
            lista = str(obj.material_core).split(',')          
            return lista    

    def get_solar_url_host(self, obj):  # type: ignore
        return obj.solar_url_host

    def get_sources(self, obj):  # type: ignore
        return obj.sources

    def get_audio_response(self, obj):  # type: ignore
        return obj.audio_response

    def get_image_file(self, obj):  # type: ignore
        request = self.context["request"]
        if obj.image_file:
           return request.build_absolute_uri(obj.image_file.url)           
        return None 

    def get_color(self, obj):  # type: ignore
        if obj.color:
            return f"{obj.color}"
        return None

    def get_font(self, obj):  # type: ignore
        if obj.font:
            return obj.font.property_value
        return None

    def get_side(self, obj):  # type: ignore
        if obj.side:
            return obj.side.id
        return None

    class Meta:
        model = ChatBot
        fields = (
            "id",
            "name",
            "type",
            "api_key",
            "model",
            "prompt",
            "language",
            "tone",
            "temperature",
            "material_core",
            "solar_url_host",
            "sources",
            "audio_response",
            "voice",
            "image_file",
            "color",
            "font",
            "side",
            "active",
            "private",
            "published",
        )
