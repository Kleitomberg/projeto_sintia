from django.db import models  # type: ignore


class BaseModel(models.Model):
    created_on = models.DateTimeField('Data de criação', auto_now=True)
    updated_on = models.DateTimeField('Última atualização', auto_now_add=True)
