# Generated by Django 2.0.10 on 2020-02-04 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200204_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='e_image',
            field=models.ImageField(default='events/no-img.jpg', upload_to='images/events/'),
        ),
        migrations.AlterField(
            model_name='attendregister',
            name='a_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 4, 16, 55, 20, 527444)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 4, 16, 55, 20, 528338)),
        ),
        migrations.AlterField(
            model_name='project',
            name='p_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 2, 4, 16, 55, 20, 529594)),
        ),
    ]
