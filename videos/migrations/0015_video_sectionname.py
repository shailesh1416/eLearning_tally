# Generated by Django 4.0.5 on 2022-10-06 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0014_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='sectionName',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='videos.section'),
        ),
    ]