# Generated by Django 2.1.2 on 2018-11-08 19:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0035_auto_20181108_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=890, null=True)),
                ('realizacao', models.CharField(blank=True, max_length=890, null=True)),
                ('local', models.CharField(blank=True, max_length=890, null=True)),
                ('participacao', models.CharField(blank=True, max_length=1290, null=True)),
                ('data', models.DateTimeField(blank=True, help_text='data do evento', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FotosEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='fotos-das-atividades/')),
                ('comentario', models.CharField(blank=True, max_length=1290, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipanteEvento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=490, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='publicacoes',
            options={'verbose_name': 'Publicacoes', 'verbose_name_plural': 'Publicacoes'},
        ),
        migrations.AlterField(
            model_name='atividadesporano',
            name='dataAtividade',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='documentosestaduais',
            name='descricao',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='documentosestaduais',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='documentosinternacionais',
            name='descricao',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='documentosinternacionais',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='documentosnacionais',
            name='descricao',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='documentosnacionais',
            name='link',
            field=models.URLField(blank=True, help_text='link do documento', null=True),
        ),
        migrations.AlterField(
            model_name='documentosnacionais',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='eventoscinedebate',
            name='data',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, help_text='data do evento', null=True),
        ),
        migrations.AlterField(
            model_name='legislacaoestadual',
            name='descricao',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='legislacaoestadual',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='legislacaonacional',
            name='descricao',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='legislacaonacional',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='publicacoes',
            name='descricao',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='publicacoes',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='subdocumento',
            name='titulo',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
    ]
