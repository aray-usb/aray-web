# Generated by Django 2.2 on 2019-04-20 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190420_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidencia',
            name='estado',
            field=models.IntegerField(choices=[(-1, 'Rechazada'), (0, 'Nueva'), (1, 'Confirmada'), (2, 'Atendida'), (3, 'Resuelta')], default=0, verbose_name='estado'),
        ),
    ]
