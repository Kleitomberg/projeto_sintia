# Generated by Django 5.0.4 on 2024-04-12 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatbots', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatbot',
            old_name='bot_owner',
            new_name='user',
        ),
    ]
