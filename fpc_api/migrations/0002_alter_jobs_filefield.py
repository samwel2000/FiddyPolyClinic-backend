# Generated by Django 3.2.4 on 2021-07-30 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpc_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='filefield',
            field=models.FileField(upload_to='jobs'),
        ),
    ]
