from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models

"""
Modelos de la base de datos de Aray.
"""


class GeoModelo(models.Model):
    """
    Modelo abstracto que incluye maneras de representar geográficamente
    un objeto genérico: latitud, longitud y (opcionalmente) radio.
    """

    latitud = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name="Latitud"
    )

    longitud = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name="Longitud"
    )

    # Arbitrariamente asumimos que el radio será recibido en metros
    radio = models.IntegerField(
        verbose_name="Radio (en metros)",
        blank=True,
        null=True
    )

    class Meta:
        """
        Permite configurar el modelo como abstracto.
        """

        abstract = True

class Incidencia(GeoModelo):
    """
    Representa una incidencia reportada en alguna punto geográfico.
    Hereda la información geográfica de la clase abstracta GeoModelo.
    """

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre de la Incidencia"
    )

    # Posibles estados para la incidencia
    ESTADO_NUEVA = 0
    ESTADO_CONFIRMADA = 1
    ESTADO_ATENDIDA = 2
    ESTADO_RESUELTA = 3

    ESTADO_CHOICES = (
        (ESTADO_NUEVA, "Nueva"),
        (ESTADO_CONFIRMADA, "Confirmada"),
        (ESTADO_ATENDIDA, "Atendida"),
        (ESTADO_RESUELTA, "Resuelta"),
    )

    estado = models.IntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_NUEVA,
        verbose_name="estado"
    )

    fecha_de_reporte = models.DateTimeField(
        verbose_name="Fecha de Reporte",
        auto_now_add=True
    )

    fecha_de_resolucion = models.DateTimeField(
        verbose_name="Fecha de Resolución",
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Retorna una representación en cadena de caracteres de la incidencia.
        """

        return self.nombre

    def esta_en_curso(self):
        """
        Determina si una incidencia se encuentra en curso.
        """

        return self.estado != Incidencia.ESTATUS_RESUELTA

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de una incidencia a un estado dado, si es válido,
        y marca las fechas importantes en caso de ser requeridas.
        """

        estados_validos = [estado[0] for estado in Incidencia.ESTATUS_CHOICES]

        # Si el nuevo estado no es válido, no hacemos ningún cambio
        if nuevo_estado not in estados_validos:
            return

        self.estado = nuevo_estado

        # Marcamos la fecha de resolución, si aplica
        if nuevo_estado == Incidencia.ESTADO_RESUELTA:
            self.fecha_de_resolucion = datetime.now()

        self.save()

class Reporte(GeoModelo):
    """
    Representa un reporte asociado a alguna incidencia.
    """

    incidencia = models.ForeignKey(
        Incidencia,
        on_delete=models.CASCADE,
        related_name="reportes",
        verbose_name="Incidencia asociada"
    )

    contenido = models.TextField(
        verbose_name="Contenido del Reporte"
    )

    # Posibles estados para el reporte
    ESTADO_SIN_CONFIRMAR = 0
    ESTADO_CONFIRMADO = 1

    ESTADO_CHOICES = (
        (ESTADO_SIN_CONFIRMAR, "Sin confirmar"),
        (ESTADO_CONFIRMADO, "Confirmado")
    )

    estado = models.IntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_SIN_CONFIRMAR,
        verbose_name="Estado"
    )

    # Si el reporte lo generó algún usuario, lo guardamos para futuros usos
    reportado_por = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Reportado por"
    )

    def __str__(self):
        """
        Retorna una representación como cadena de caracteres del reporte.
        """

        return "{0} ({1})".format(
            self.contenido,
            self.estado
        )

    def confirmar_reporte(self):
        """
        Permite confirmar un reporte de manera rápida.
        """

        if self.estado == Reporte.ESTADO_CONFIRMADO:
            return

        self.estado = Reporte.ESTADO_CONFIRMADO
        self.save()

