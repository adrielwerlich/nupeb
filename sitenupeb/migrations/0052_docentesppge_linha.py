# Generated by Django 2.1.2 on 2018-11-10 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0051_auto_20181110_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='docentesppge',
            name='linha',
            field=models.ForeignKey(blank=True, help_text='linha do docente', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='linhaPpge', to='sitenupeb.LinhaPpge'),
        ),
    ]