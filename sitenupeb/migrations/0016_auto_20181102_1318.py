# Generated by Django 2.1.2 on 2018-11-02 16:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0015_remove_eventoscinedebate_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventoscinedebate',
            name='data',
            field=models.DateField(blank=True, default=datetime.datetime.today, null=True),
        ),
    ]
