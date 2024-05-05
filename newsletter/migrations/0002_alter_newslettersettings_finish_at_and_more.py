# Generated by Django 5.0.3 on 2024-05-05 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersettings',
            name='finish_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 4, 9, 9, 56, 289977, tzinfo=datetime.timezone.utc), verbose_name='дата окончания'),
        ),
        migrations.AlterField(
            model_name='newslettersettings',
            name='start_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 5, 12, 9, 56, 291981), verbose_name='дата начала'),
        ),
    ]
