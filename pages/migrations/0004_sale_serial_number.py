# Generated by Django 3.0 on 2019-12-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20191207_0015'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='serial_number',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]