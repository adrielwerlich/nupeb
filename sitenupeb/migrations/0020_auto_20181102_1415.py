# Generated by Django 2.1.2 on 2018-11-02 17:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0019_auto_20181102_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventoscinedebate',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
