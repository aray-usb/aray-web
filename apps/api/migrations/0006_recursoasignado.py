# Generated by Django 2.1.7 on 2019-03-18 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190318_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecursoAsignado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Latitud')),
                ('longitud', models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Longitud')),
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
    ]