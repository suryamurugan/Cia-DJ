# Generated by Django 2.0.10 on 2019-10-28 12:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_auto_20191002_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendregister',
            name='a_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 28, 12, 32, 22, 395269)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 28, 12, 32, 22, 396013)),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 28, 12, 32, 22, 396917)),
        ),
    ]
