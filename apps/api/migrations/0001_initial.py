# Generated by Django 2.2.1 on 2019-05-12 22:53

import apps.api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Incidencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitud')),
                ('radio', models.IntegerField(blank=True, null=True, verbose_name='Radio (en metros)')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la Incidencia')),
                ('descripcion', models.TextField(blank=True, default='', verbose_name='Descripción')),
                ('estado', models.IntegerField(choices=[(-1, 'Rechazada'), (0, 'Nueva'), (1, 'Confirmada'), (2, 'Atendida'), (3, 'Resuelta')], default=0, verbose_name='estado')),
                ('fecha_de_reporte', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Reporte')),
                ('fecha_de_resolucion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Resolución')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Organizacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitud')),
                ('radio', models.IntegerField(blank=True, null=True, verbose_name='Radio (en metros)')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre de la Organización')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre')),
                ('tipo', models.IntegerField(choices=[(0, 'Salud'), (1, 'Alimentación'), (2, 'Transporte'), (999, 'Otros')], default=999, verbose_name='Tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Voluntario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=15, validators=[apps.api.models.ValidadorDeTelefono])),
                ('tipo_identidad', models.IntegerField(choices=[(0, 'V'), (1, 'E')], default=0, verbose_name='Tipo de Documento de Identidad')),
                ('nro_identidad', models.IntegerField(verbose_name='Nro. de Documento de Identidad')),
                ('organizaciones', models.ManyToManyField(related_name='voluntarios', to='api.Organizacion', verbose_name='Organizaciones asociadas')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario asociado')),
            ],
            options={
                'unique_together': {('tipo_identidad', 'nro_identidad')},
            },
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('descripcion', models.TextField(blank=True, default='', verbose_name='Descripción')),
                ('fecha_limite', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Límite')),
                ('fecha_de_resolucion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de Resolución')),
                ('estado', models.IntegerField(choices=[(0, 'Nueva'), (1, 'En progreso'), (2, 'Resuelta')], default=0, verbose_name='Estado')),
                ('asignada_a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='api.Voluntario', verbose_name='Voluntario asignado')),
                ('asignada_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tareas_que_ha_asignado', to='api.Voluntario', verbose_name='Asignada por')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitud')),
                ('radio', models.IntegerField(blank=True, null=True, verbose_name='Radio (en metros)')),
                ('contenido', models.TextField(verbose_name='Contenido del Reporte')),
                ('estado', models.IntegerField(choices=[(0, 'Sin confirmar'), (1, 'Confirmado')], default=0, verbose_name='Estado')),
                ('fecha_de_reporte', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Reporte')),
                ('incidencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reportes', to='api.Incidencia', verbose_name='Incidencia asociada')),
                ('reportado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Voluntario', verbose_name='Reportado por')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecursoAsignado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=7, max_digits=10, verbose_name='Longitud')),
                ('radio', models.IntegerField(blank=True, null=True, verbose_name='Radio (en metros)')),
                ('cantidad', models.IntegerField(default=1, verbose_name='Cantidad')),
                ('organizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recursos', to='api.Organizacion', verbose_name='Organización asignada')),
                ('recurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='asignaciones', to='api.Recurso', verbose_name='Recurso asignado')),
                ('voluntario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recursos', to='api.Voluntario', verbose_name='Voluntario asignado')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='organizacion',
            name='dirigida_por',
            field=models.ManyToManyField(related_name='dirige', to='api.Voluntario', verbose_name='Dirigida por'),
        ),
    ]
