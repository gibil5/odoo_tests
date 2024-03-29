# Generated by Django 3.0 on 2019-12-07 13:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20191207_1338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Management',
            fields=[
                ('odoomodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.OdooModel')),
                ('date_update', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ('date',),
            },
            bases=('pages.odoomodel',),
        ),
    ]
