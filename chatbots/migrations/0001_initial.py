# Generated by Django 5.0.4 on 2024-04-12 02:38

import uuid

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BotType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Tipo do bot')),
                ('route', models.CharField(max_length=100, verbose_name='Rota do bot')),
            ],
            options={
                'verbose_name': 'Tipo do bot',
                'verbose_name_plural': 'Tipos de bots',
            },
        ),
        migrations.CreateModel(
            name='ModelType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=100, verbose_name='Tipo de modelo'),
                ),
                (
                    'value',
                    models.CharField(max_length=100, verbose_name='Valor do modelo'),
                ),
                (
                    'input_price',
                    models.FloatField(
                        default=0,
                        help_text='Informe o custo de tokens de entrada do modelo em Dolar. $/1k tokens',
                        verbose_name='Custo de entrada',
                    ),
                ),
                (
                    'output_price',
                    models.FloatField(
                        default=0,
                        help_text='Informe o custo de tokens de saída do modelo em Dolar. $/1k tokens',
                        verbose_name='Custo de saída',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Tipo de modelo',
                'verbose_name_plural': 'Tipos de modelos',
            },
        ),
        migrations.CreateModel(
            name='Scalations',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('value', models.CharField(max_length=100, verbose_name='Valor')),
            ],
            options={
                'verbose_name': 'Escalação',
                'verbose_name_plural': 'Escalações',
            },
        ),
        migrations.CreateModel(
            name='SearchType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                (
                    'name',
                    models.CharField(max_length=100, verbose_name='Tipo de busca'),
                ),
                (
                    'value',
                    models.CharField(max_length=100, verbose_name='Valor da busca'),
                ),
            ],
            options={
                'verbose_name': 'Tipo de busca',
                'verbose_name_plural': 'Tipos de busca',
            },
        ),
        migrations.CreateModel(
            name='ToneType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de tom')),
                (
                    'value',
                    models.CharField(max_length=100, verbose_name='Valor do tom'),
                ),
            ],
            options={
                'verbose_name': 'Tipo de tom',
                'verbose_name_plural': 'Tipos de tons',
            },
        ),
        migrations.CreateModel(
            name='VoiceType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de voz')),
                (
                    'value',
                    models.CharField(max_length=100, verbose_name='Valor da voz'),
                ),
            ],
            options={
                'verbose_name': 'Tipo de voz',
                'verbose_name_plural': 'Tipos de vozes',
            },
        ),
        migrations.CreateModel(
            name='ApiKey',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                ('key', models.CharField(max_length=100, verbose_name='Chave')),
                (
                    'owner',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'model',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='chatbots.modeltype',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChatBot',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                (
                    'created_on',
                    models.DateTimeField(
                        auto_now_add=True, verbose_name='Data de criação'
                    ),
                ),
                (
                    'updated_on',
                    models.DateTimeField(
                        auto_now=True, verbose_name='Última atualização'
                    ),
                ),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=100, verbose_name='Nome do bot')),
                ('prompt', models.TextField(verbose_name='Prompt do bot')),
                (
                    'language',
                    models.CharField(
                        blank=True,
                        default='português brasileiro',
                        max_length=255,
                        null=True,
                    ),
                ),
                ('temperature', models.FloatField(default=0.3)),
                (
                    'material_core',
                    models.TextField(
                        blank=True,
                        default='',
                        help_text="Aqui estão indicadas as URL's em que o bot fará a busca, caso seja \n        um chatbot do tipo web. Caso não seja informado o bot irá pesquisar em toda a internet.",
                        null=True,
                        verbose_name='Fontes de busca do bot',
                    ),
                ),
                (
                    'solar_url_host',
                    models.CharField(
                        blank=True,
                        max_length=100,
                        null=True,
                        verbose_name='URL do host SOLR',
                    ),
                ),
                (
                    'sources',
                    models.IntegerField(
                        default=3,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                        verbose_name='Fontes',
                    ),
                ),
                (
                    'audio_response',
                    models.BooleanField(
                        default=False, verbose_name='Resposta em áudio'
                    ),
                ),
                (
                    'image_file',
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to='bots/',
                        verbose_name='Imagem do bot',
                    ),
                ),
                (
                    'api_key',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='chatbots.apikey',
                    ),
                ),
                (
                    'bot_owner',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    'type',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to='chatbots.bottype',
                    ),
                ),
                (
                    'model',
                    models.ForeignKey(
                        default='standard',
                        on_delete=django.db.models.deletion.CASCADE,
                        to='chatbots.modeltype',
                    ),
                ),
                (
                    'search',
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='chatbots.searchtype',
                    ),
                ),
                (
                    'tone',
                    models.ForeignKey(
                        default='formal',
                        on_delete=django.db.models.deletion.CASCADE,
                        to='chatbots.tonetype',
                    ),
                ),
                (
                    'voice',
                    models.ForeignKey(
                        default='nova',
                        on_delete=django.db.models.deletion.SET_DEFAULT,
                        to='chatbots.voicetype',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
    ]