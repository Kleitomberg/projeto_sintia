# Generated by Django 5.0.4 on 2024-04-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0002_rename_message_session_message_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='response_cost',
            field=models.FloatField(
                blank=True, null=True, verbose_name='Custo de saída'
            ),
        ),
    ]
