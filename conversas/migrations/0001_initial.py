# Generated by Django 5.1.7 on 2025-03-21 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome do documento', max_length=255, verbose_name='Nome')),
                ('arquivo', models.FileField(help_text='Arquivo do documento', upload_to='documentos/', verbose_name='Arquivo')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
    ]
