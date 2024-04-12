from rest_framework import status, viewsets
from rest_framework.response import Response

from base.permissions import OwnProfilePermission, PostCreateOrAuthenticated
from bot_messages import serializers
from bot_messages.models import Message, Session

from utils import email


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = serializers.MessageSerializer
    permission_classes = [PostCreateOrAuthenticated, OwnProfilePermission]

    def create(self, request, *args, **kwargs):  # type: ignore
        query = request.data.get("request", "")
        session = Session.objects.get(pk=request.data.get("session", ""))
        queryset = Message.objects.filter(session=session)
        conversations = session.bot.get_session_messages(queryset)
        scalations = session.bot.get_scalations()
        user = request.user
        cost = session.bot.model.credits_cost
        if user.credits < cost:
            email.no_credits_email(user.email, f"{user.first_name} {user.last_name}")
            return Response(
                {"error": "Não há créditos suficientes"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        else:
            response = session.bot.request_message(query, conversations, scalations)
            data = {
                "request": query,
                "response": response["response"],
                "session": session.pk,
                "prompt_tokens": response["prompt_tokens"],
                "response_tokens": response["response_tokens"],
            }
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                headers=headers,
            )


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = serializers.SessionSerializer
    permission_classes = [PostCreateOrAuthenticated, OwnProfilePermission]

    def create(self, request, *args, **kwargs):  # type: ignore

        data = {
            "bot": request.query_params.get("bot", ""),
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    def list(self, request, *args, **kwargs):  # type: ignore
        queryset = self.filter_queryset(self.get_queryset())
        queryset = queryset.filter(user=request.user)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
