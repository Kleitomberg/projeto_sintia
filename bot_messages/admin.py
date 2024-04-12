from django.contrib import admin

# Register your models here.
from bot_messages.models import Message, Session


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'request',
        'session',
        'prompt_tokens',
        'response_tokens',
        'total_cost',
        'credits_cost',
    )


class MessageInline(admin.TabularInline):
    model = Message
    extra = 0
    readonly_fields = (
        'request',
        'response',
        'session',
        'prompt_tokens',
        'response_tokens',
        'prompt_cost',
        'response_cost',
        'total_cost',
    )
    can_delete = False


class SessionAdmin(admin.ModelAdmin):
    list_display = ('uuid',)
    inlines = [MessageInline]


admin.site.register(Session, SessionAdmin)
