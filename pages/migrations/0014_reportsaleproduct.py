# Generated by Django 3.0 on 2019-12-10 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20191210_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReportSaleProduct',
            fields=[
                ('odoomodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.OdooModel')),
            ],
            options={
                'ordering': ('-date',),
            },
            bases=('pages.odoomodel',),
        ),
    ]
