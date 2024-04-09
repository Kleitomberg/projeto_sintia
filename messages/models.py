import uuid

from django.db import models

from users.base_model import BaseModel
from users.models import User


class Session(BaseModel):
    session_id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Messages(BaseModel):
    message = models.CharField("Content", max_length=500)
    response = models.CharField("Content", max_length=500)
    prompt_tokens = models.IntegerField(name='Tokens de entrada')
    response_tokens = models.IntegerField(name='Tokens de Resposta')
    session = models.CharField(max_length=100)
