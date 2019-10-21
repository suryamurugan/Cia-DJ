# Generated by Django 2.0.10 on 2019-09-26 17:31

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20190926_0610'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('p_id', models.AutoField(primary_key=True, serialize=False)),
                ('p_image', models.ImageField(default='projects/no-img.jpg', upload_to='images/projects/')),
                ('p_datetime', models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 26, 17, 31, 17, 213293))),
                ('p_desc', models.CharField(default='description', max_length=500)),
                ('p_medium_link', models.CharField(default='https://www.medium.com', max_length=250)),
                ('p_github_link', models.CharField(default='https://www.github.com', max_length=250)),
                ('u_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='attendregister',
            name='a_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 26, 17, 31, 17, 211058)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 9, 26, 17, 31, 17, 212141)),
        ),
        migrations.AlterField(
            model_name='news',
            name='n_image',
            field=models.ImageField(default='news/no-img.jpg', upload_to='images/news/'),
        ),
    ]