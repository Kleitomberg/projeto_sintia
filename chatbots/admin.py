from django.contrib import admin

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

# Register your models here.


@admin.register(BotType)
class BotTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ToneType)
class ToneTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(VoiceType)
class VoiceTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(SearchType)
class SearchTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ModelType)
class ModelTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(ChatBot)
class ChatBotAdmin(admin.ModelAdmin):
    pass


@admin.register(Scalations)
class ScalationsAdmin(admin.ModelAdmin):
    pass


@admin.register(ApiKey)
class APIkeyAdmin(admin.ModelAdmin):
    pass
