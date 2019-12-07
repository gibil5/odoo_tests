# Generated by Django 3.0 on 2019-12-07 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20191207_0006'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='patient',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='sale',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='sale',
            name='x_type',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]