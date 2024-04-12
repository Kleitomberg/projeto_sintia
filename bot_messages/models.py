import uuid

from django.db import models

from chatbots.models import ChatBot
from users.models import User


# Create your models here.
class BaseMessageModel(models.Model):
    created_on = models.DateTimeField('Data de criação', auto_now_add=True)
    updated_on = models.DateTimeField('Última atualização', auto_now=True)

    class Meta:
        abstract = True


class Session(BaseMessageModel):
    bot = models.ForeignKey(ChatBot, on_delete=models.SET_NULL, null=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.uuid}'


class Message(BaseMessageModel):
    request = models.TextField('Mensagem')
    response = models.TextField('Resposta')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, null=True)
    prompt_tokens = models.IntegerField('Tokens de entrada')
    prompt_cost = models.FloatField('Custo de entrada', null=True, blank=True)
    response_tokens = models.IntegerField('Tokens de saída')
    response_cost = models.FloatField('Custo de saída', null=True, blank=True)

    @property
    def total_cost(self) -> float:
        if self.prompt_cost is None or self.response_cost is None:
            return 0
        return self.prompt_cost + self.response_cost

    @property
    def credits_cost(self) -> int:
        if self.total_cost is None or self.total_cost == 0:
            return 0
        return self.session.bot.model.credits_cost

    class Meta:
        verbose_name = 'Mensagem'
        verbose_name_plural = 'Mensagens'
