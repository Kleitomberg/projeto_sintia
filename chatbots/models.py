import json
import uuid

import requests
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import InternalError, models

from users.models import User
from customizations.models import colors, fontFamilies, screenSides

from config import Config

config = Config()


class BaseChatbotModel(models.Model):
    created_on = models.DateTimeField("Data de criação", auto_now_add=True)
    updated_on = models.DateTimeField("Última atualização", auto_now=True)

    class Meta:
        abstract = True


class BotType(BaseChatbotModel):
    name = models.CharField("Tipo do bot", max_length=100)
    route = models.CharField("Rota do bot", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tipo do bot"
        verbose_name_plural = "Tipos de bots"


class SearchType(BaseChatbotModel):
    name = models.CharField("Tipo de busca", max_length=100)
    value = models.CharField("Valor da busca", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tipo de busca"
        verbose_name_plural = "Tipos de busca"


class ModelType(BaseChatbotModel):
    name = models.CharField("Tipo de modelo", max_length=100)
    value = models.CharField("Valor do modelo", max_length=100)
    default_api_key = models.CharField("Chave", max_length=100, null=True)
    input_price = models.FloatField(
        "Custo de entrada",
        default=0,
        help_text="Informe o custo de tokens de entrada do modelo em Dolar. $/1k tokens",
    )
    output_price = models.FloatField(
        "Custo de saída",
        default=0,
        help_text="Informe o custo de tokens de saída do modelo em Dolar. $/1k tokens",
    )
    credits_cost = models.IntegerField("Créditos por mensagem", default=1)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tipo de modelo"
        verbose_name_plural = "Tipos de modelos"


class ToneType(BaseChatbotModel):
    name = models.CharField("Tipo de tom", max_length=100)
    value = models.CharField("Valor do tom", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tipo de tom"
        verbose_name_plural = "Tipos de tons"


class VoiceType(BaseChatbotModel):
    name = models.CharField("Tipo de voz", max_length=100)
    value = models.CharField("Valor da voz", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Tipo de voz"
        verbose_name_plural = "Tipos de vozes"


class ApiKey(BaseChatbotModel):
    model = models.ForeignKey(ModelType, on_delete=models.CASCADE)
    key = models.CharField("Chave", max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.model.name


class Scalations(BaseChatbotModel):
    name = models.CharField("Nome", max_length=100)
    value = models.CharField("Valor", max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Escalação"
        verbose_name_plural = "Escalações"


class ChatBot(BaseChatbotModel):

    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    name = models.CharField("Nome do bot", max_length=100)
    type = models.ForeignKey(BotType, on_delete=models.SET_NULL, null=True)
    api_key = models.ForeignKey(
        ApiKey,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    search = models.ForeignKey(
        SearchType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    model = models.ForeignKey(ModelType, on_delete=models.SET_NULL, null=True)
    prompt = models.TextField("Prompt do bot", null=False, blank=False)
    language = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        default="português brasileiro",
    )
    tone = models.ForeignKey(ToneType, on_delete=models.SET_NULL, null=True)
    temperature = models.FloatField(default=0.3)
    material_core = models.TextField(
        "Fontes de busca do bot",
        help_text="""Aqui estão indicadas as URL's em que o bot fará a busca, caso seja 
        um chatbot do tipo web. Caso não seja informado o bot irá pesquisar em toda a internet.""",
        blank=True,
        null=True,
        default="",
    )
    solar_url_host = models.CharField(
        "URL do host SOLR",
        max_length=100,
        blank=True,
        null=True,
    )
    sources = models.IntegerField(
        "Fontes",
        default=3,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ],
    )
    audio_response = models.BooleanField("Resposta em áudio", default=False)
    voice = models.ForeignKey(VoiceType, on_delete=models.SET_NULL, null=True)
    image_file = models.ImageField(
        "Imagem do bot",
        upload_to="bots/",
        null=True,
        blank=True,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField("Ativo", default=True)
    is_private = models.BooleanField("Privado", default=False)
    is_published = models.BooleanField("Publicado", default=False)

    color = models.CharField("Color", max_length=7, default="#536cbc")
    font = models.ForeignKey(
        fontFamilies, on_delete=models.SET_NULL, null=True, blank=True
    )
    side = models.ForeignKey(
        screenSides, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self) -> str:
        return self.name

    def request_message(self, message: str, conversations: list, scalations: list):  # type: ignore
        params = {}
        params["query"] = message
        if self.user.partnership:
            params["api_key"] = self.api_key.key
        else:
            params["api_key"] = self.model.default_api_key
        if self.search:
            params["busca"] = self.search.value
        params["model"] = self.model.value
        params["prompt"] = self.prompt
        params["language"] = self.language
        params["tone"] = self.tone.value
        params["temperature"] = self.temperature
        if self.material_core:
            if self.material_core:
                params["material_core"] = json.dumps(
                    self.material_core.replace("[", "")
                    .replace("]", "")
                    .replace('"', "")
                    .split(", "),
                )
            else:
                params["material_core"] = json.dumps([])
        if self.sources:
            params["sources"] = self.sources

        if self.voice:
            params["voice"] = self.voice.value
        else:
            params["voice"] = "nova"

        url = f"{config.chatbot_url}{self.type.route}"
        body = {
            "conversation": json.dumps(conversations),
            "scalations": json.dumps(scalations),
            "memory": json.dumps([]),
        }
        file = {"image_file": (None, "")}
        try:
            session = requests.Session()
            session.auth = (
                config.chatbot_username,
                config.chatbot_password,
            )
            r = session.post(url, data=body, params=params, files=file)
            if json.loads(r.text)["scalations"]:
                return {
                    "response": json.loads(r.text)["response"]["content"],
                    "prompt_tokens": 0,
                    "response_tokens": 0,
                    "status": 202,
                }
            else:
                return {
                    "response": json.loads(r.text)["response"]["content"],
                    "prompt_tokens": (
                        json.loads(r.text)["usage"]["prompt_tokens"]
                        if json.loads(r.text)["usage"]["prompt_tokens"]
                        else 0
                    ),
                    "response_tokens": (
                        json.loads(r.text)["usage"]["completion_tokens"]
                        if json.loads(r.text)["usage"]["completion_tokens"]
                        else 0
                    ),
                    "status": 200,
                }
        except:
            raise InternalError("Erro ao obter resposta do agente. Tente novamente!")

    def get_session_messages(self, queryset):  # type: ignore
        conversations = []
        for m in queryset:
            conversations.append({"role": "user", "content": m.request})
            conversations.append({"role": "assistant", "content": m.response})
        return conversations

    def get_scalations(self):  # type: ignore
        scalations = []
        for s in Scalations.objects.all():
            scalations.append(
                {
                    "resposta": s.resposta,
                    "sentenca": s.sentenca,
                },
            )
            return scalations
