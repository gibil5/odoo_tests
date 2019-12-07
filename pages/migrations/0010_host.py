# Generated by Django 3.0 on 2019-12-07 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_auto_20191207_1201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('hostname', models.CharField(max_length=200)),
                ('database', models.CharField(max_length=200)),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
