# Generated by Django 5.0.4 on 2024-04-12 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbots', '0007_alter_chatbot_is_private_alter_chatbot_is_published_and_more'),
        ('customizations', '0002_alter_colors_options_alter_fontfamilies_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatbot',
            name='color',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customizations.colors'),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='font',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customizations.fontfamilies'),
        ),
        migrations.AddField(
            model_name='chatbot',
            name='side',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='customizations.screensides'),
        ),
    ]
