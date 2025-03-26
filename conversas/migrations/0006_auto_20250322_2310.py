# Generated by Django 5.1.7 on 2025-03-23 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversas', '0005_vetordocumento_metadata'),
    ]

    operations = [
        migrations.RunSQL(
            sql='ALTER TABLE conversas_vetordocumento ALTER COLUMN metadata TYPE JSONB USING metadata::jsonb;',
            reverse_sql='ALTER TABLE conversas_vetordocumento ALTER COLUMN metadata TYPE JSON USING metadata::json;',
        ),
    ]
