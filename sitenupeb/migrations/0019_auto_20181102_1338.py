# Generated by Django 2.1.2 on 2018-11-02 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0018_auto_20181102_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventoscinedebate',
            name='local',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='localExibicao', to='sitenupeb.LocalExibicao'),
        ),
    ]
