# Generated by Django 5.0.4 on 2024-04-12 03:18

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chatbots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
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
                    'uuid',
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                (
                    'bot',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to='chatbots.chatbot',
                    ),
                ),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
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
                ('request', models.TextField(verbose_name='Mensagem')),
                ('response', models.TextField(verbose_name='Resposta')),
                (
                    'prompt_tokens',
                    models.IntegerField(verbose_name='Tokens de entrada'),
                ),
                (
                    'prompt_cost',
                    models.FloatField(
                        blank=True, null=True, verbose_name='Custo de entrada'
                    ),
                ),
                (
                    'response_tokens',
                    models.IntegerField(verbose_name='Tokens de saída'),
                ),
                (
                    'response_cost',
                    models.FloatField(
                        blank=True, null=True, verbose_name='Custo de entrada'
                    ),
                ),
                (
                    'message_session',
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to='bot_messages.session',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Mensagem',
                'verbose_name_plural': 'Mensagens',
            },
        ),
    ]
