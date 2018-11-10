# Generated by Django 2.1.2 on 2018-11-10 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0050_pesquisasemandamento_pesquisasrealizadas'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContatoPpge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, help_text='link do mestrado', null=True)),
                ('linkFace', models.URLField(blank=True, help_text='link do mestrado no face', null=True)),
                ('telefone', models.CharField(blank=True, help_text='telefone contato mestrado', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DocentesPpge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='nome do docente', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EmailPpge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, default=None, max_length=70, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='LinhaPpge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, help_text='descrição da linha', max_length=500, null=True)),
                ('descricao', models.CharField(blank=True, help_text='descrição da linha', max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ppge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(blank=True, help_text='descrição do mestrado', max_length=1500, null=True)),
                ('rodape', models.CharField(blank=True, help_text='descrição do mestrado', max_length=1500, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='pesquisasemandamento',
            options={'verbose_name': 'PesquisasEmAndamento', 'verbose_name_plural': 'Pesquisas em Andamento'},
        ),
        migrations.AlterModelOptions(
            name='pesquisasrealizadas',
            options={'verbose_name': 'PesquisasRealizadas', 'verbose_name_plural': 'Pesquisas Realizadas'},
        ),
    ]