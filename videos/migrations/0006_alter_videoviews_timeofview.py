# Generated by Django 4.0.5 on 2022-09-28 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0005_alter_videoviews_timeofview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videoviews',
            name='timeOfView',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]