# Generated by Django 3.0 on 2019-12-07 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20191207_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='management',
            options={'ordering': ('-date',)},
        ),
    ]
