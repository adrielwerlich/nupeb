# Generated by Django 2.1.2 on 2018-11-09 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0045_temafilme_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeituraPorTema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, help_text='titulo/descrição da leitura', max_length=5000, null=True)),
                ('link', models.URLField(blank=True, help_text='link da leitura', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TemaLeitura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tema', models.CharField(blank=True, help_text='tema da leitura', max_length=5000, null=True)),
                ('comentario', models.CharField(blank=True, help_text='comentário sobre o contexto', max_length=15000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='leituraportema',
            name='tema',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='temaDaleitura', to='sitenupeb.TemaLeitura'),
        ),
    ]
