# Generated by Django 2.1.2 on 2018-11-02 19:54

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('sitenupeb', '0021_auto_20181102_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventoscinedebate',
            name='video',
        ),
        migrations.AddField(
            model_name='iframeslinks',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, default=None, help_text='This is a help text', null=True, verbose_name='My video'),
        ),
    ]
