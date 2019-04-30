from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
import datetime



def valid_date(date):
    today = datetime.date.today()
    if date > today:
        raise ValidationError('La fecha de registro de este recurso debe ser posterior a hoy.')

class Resource(models.Model):

    RESOURCE_TYPE = (
        (0, 'Medicina'),
        (1, 'Vehículo'),
        (2, 'Alimento'),
        (3, 'Artículo de Rescate'),
    )

    name = models.CharField(
        max_length=50, 
        name='Nombre del Bien'
    )

    resource_type = models.IntegerField(
        choices=RESOURCE_TYPE,
        default=3
    )

    register_date = models.DateField(
        validators=[valid_date],
        verbose_name='Fecha de Registro de este bien'
    )

    purchase_prize = models.IntegerField(
        verbose_name='Precio de los bienes introducidos en este registro',
        validators=[MinValueValidator(1)],
    )

    items_cuantity = models.IntegerField(
        verbose_name='Cantidad de artículos de este bien',
        validators=[MinValueValidator(1)],
    )

    """
        thumbnail = models.ImageField(
            upload_to='',
            blank=True,
            null=True
        )
    """

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'

    def __str__(self):
        return str(self.resource_type) + ' - ' + str(self.name)


