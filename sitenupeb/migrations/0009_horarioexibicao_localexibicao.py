# Generated by Django 2.1.2 on 2018-11-01 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0008_auto_20181101_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='horarioexibicao',
            name='localExibicao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='localDaExibicao', to='sitenupeb.LocalExibicao'),
        ),
    ]
