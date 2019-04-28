# Generated by Django 2.1.7 on 2019-03-18 04:11

import apps.api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitud')),
                ('radio', models.IntegerField(blank=True, null=True, verbose_name='Radio (en metros)')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la Organización')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15, validators=[api.models.ValidadorDeTelefono])),
                ('tipo_identidad', models.CharField(choices=[('V', 'Venezolano'), ('E', 'Extranjero')], default='V', max_length=1, verbose_name='Tipo de Documento de Identidad')),
                ('nro_identidad', models.IntegerField(max_length=8, verbose_name='Nro. de Documento de Identidad')),
                ('organizaciones', models.ManyToManyField(related_name='voluntarios', to='api.Organizacion', verbose_name='Organizaciones asociadas')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario asociado')),
            ],
        ),
        migrations.AlterField(
            model_name='reporte',
            name='reportado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Voluntario', verbose_name='Reportado por'),
        ),
        migrations.AddField(
            model_name='organizacion',
            name='dirigida_por',
            field=models.ManyToManyField(related_name='dirige', to='api.Voluntario', verbose_name='Dirigida por'),
        ),
    ]