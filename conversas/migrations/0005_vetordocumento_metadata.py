# Generated by Django 5.1.7 on 2025-03-23 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversas', '0004_vetordocumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='vetordocumento',
            name='metadata',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
