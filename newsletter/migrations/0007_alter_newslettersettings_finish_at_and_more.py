# Generated by Django 5.0.3 on 2024-05-21 11:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0006_alter_newslettersettings_finish_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newslettersettings',
            name='finish_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 6, 20, 11, 33, 18, 90352, tzinfo=datetime.timezone.utc), verbose_name='дата окончания'),
        ),
        migrations.AlterField(
            model_name='newslettersettings',
            name='start_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 21, 14, 33, 18, 90352), verbose_name='дата начала'),
        ),
    ]
