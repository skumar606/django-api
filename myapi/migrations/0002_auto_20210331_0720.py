# Generated by Django 3.1.7 on 2021-03-31 01:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userloginhistory',
            name='login_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 7, 20, 15, 313093)),
        ),
    ]
