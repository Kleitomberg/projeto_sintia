# Generated by Django 5.0.4 on 2024-04-12 04:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot_messages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='message_session',
            new_name='session',
        ),
    ]