# Generated by Django 2.1.2 on 2018-11-04 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0029_auto_20181104_1315'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LinhasDePesquisa',
            new_name='LinhaDePesquisa',
        ),
        migrations.AlterField(
            model_name='egresso',
            name='nomeAmostrar',
            field=models.CharField(max_length=300, verbose_name='Nome a mostrar'),
        ),
        migrations.AlterField(
            model_name='integrate',
            name='nomeAmostrar',
            field=models.CharField(max_length=300, verbose_name='Nome a mostrar'),
        ),
        migrations.AlterField(
            model_name='pesquisador',
            name='nomeAmostrar',
            field=models.CharField(max_length=300, verbose_name='Nome a mostrar'),
        ),
    ]
