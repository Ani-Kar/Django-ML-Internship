# Generated by Django 4.0.4 on 2022-05-08 10:52

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='url',
            field=embed_video.fields.EmbedVideoField(default='www.youtube.com/watch?v=qDwdMDQ8oX4'),
        ),
    ]
