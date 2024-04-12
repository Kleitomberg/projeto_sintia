from django.urls import include, path  # type: ignore
from rest_framework.authtoken.views import obtain_auth_token  # type: ignore
from rest_framework.routers import DefaultRouter  # type: ignore

from bot_messages import viewsets as MessagesViewSets
from chatbots import viewsets as ChatbotViewsets
from users import viewsets as UserViewSets

router = DefaultRouter()

router.register(r'users', UserViewSets.UserViewSet, basename='users'),
router.register(r'chatbots', ChatbotViewsets.ChatBotViewSet, basename='chatbots'),
router.register(r'messages', MessagesViewSets.MessageViewSet, basename='messages')
router.register(r'sessions', MessagesViewSets.SessionViewSet, basename='sessions')

urlpatterns = [path('', include(router.urls)), path('login/', obtain_auth_token)]
