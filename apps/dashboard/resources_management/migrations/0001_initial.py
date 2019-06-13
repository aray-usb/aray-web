# Generated by Django 2.1.7 on 2019-04-30 18:33

import apps.dashboard.resources_management.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre del Bien', models.CharField(max_length=50)),
                ('resource_type', models.IntegerField(choices=[(0, 'Medicina'), (1, 'Vehículo'), (2, 'Alimento'), (3, 'Artículo de Rescate')], default=3)),
                ('register_date', models.DateField(validators=[apps.dashboard.resources_management.models.valid_date], verbose_name='Fecha de Registro de este bien')),
                ('purchase_prize', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Precio de los bienes introducidos en este registro')),
                ('items_cuantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad de artículos de este bien')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
            },
        ),
    ]