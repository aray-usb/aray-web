"""
Módulo que incluye los distintos modelos de la base de datos
de Aray, incluyendo validadores y funciones adicionales.
"""

from datetime import datetime

from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

"""
Validadores
"""

class ValidadorDeTelefono(RegexValidator):
    """
    Validador que verifica que el formato de un número de teléfono
    sea el prestablecido: (0XXX) XXX-XXXX
    """

    regex = r'\(0\d{3}\)\ \d{3}\-\d{4}'
    message = "El número de teléfono no sigue el formato válido. Formato: (0XXX) XXX-XXXX"

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

class Voluntario(models.Model):
    """
    Representa la información de un voluntario, modelo que regula el "perfil" de un
    usuario. De su usuario asociado, podemos obtener: nombre, apellido, correo electrónico.
    """

    usuario = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name="Usuario asociado"
    )

    organizaciones = models.ManyToManyField(
        "Organizacion",
        related_name="voluntarios",
        verbose_name="Organizaciones asociadas"
    )

    # El número de teléfono usa un validador personalizado
    telefono = models.CharField(
        max_length=15,
        validators=[ValidadorDeTelefono]
    )

    # Tipos de documento de identidad
    TIPO_VENEZOLANO = 0
    TIPO_EXTRANJERO = 1

    TIPO_CHOICES = (
        (TIPO_VENEZOLANO, "V"),
        (TIPO_EXTRANJERO, "E"),
    )

    tipo_identidad = models.IntegerField(
        choices=TIPO_CHOICES,
        default=TIPO_VENEZOLANO,
        verbose_name="Tipo de Documento de Identidad"
    )

    nro_identidad = models.IntegerField(
        verbose_name="Nro. de Documento de Identidad"
    )

    class Meta:
        """
        Permite definir configuraciones para el modelo Voluntario
        """

        unique_together = ("tipo_identidad", "nro_identidad")

    @property
    def identificacion(self):
        """
        Retorna una representación apropiada de la identificación del usuario.
        """

        return "{0}-{1}".format(
            self.get_tipo_identidad_display(),
            self.nro_identidad
        )

    @property
    def nombre(self):
        """
        Alias para el nombre del voluntario en español.
        """

        return self.usuario.first_name

    @property
    def nombre(self):
        """
        Alias para el apellido del voluntario en español.
        """

        return self.usuario.last_name

    @property
    def email(self):
        """
        Alias para el email del voluntario a partir del usuario asociado.
        """

        return self.usuario.email

    @property
    def es_director(self):
        """
        Determina si un voluntario es director de alguna organización asociada.
        """

        # 'dirige' es la relación inversa a Organizacion.dirigida_por
        return self.dirige.all().count() > 0

    def __str__(self):
        """
        Retorna una representación como string del Voluntario.
        """

        return "{0} {1}".format(
            self.nombre,
            self.apellido
        )

class Tarea(models.Model):
    """
    Representa una tarea asignada a un usuario.
    """

    titulo = models.CharField(
        max_length=100,
        verbose_name="Título"
    )

    descripcion = models.TextField(
        default="",
        verbose_name="Descripción"
    )

    fecha_limite = models.DateTimeField(
        verbose_name="Fecha Límite",
        blank=True,
        null=True
    )

    fecha_de_resolucion = models.DateTimeField(
        verbose_name="Fecha de Resolución",
        blank=True,
        null=True
    )

    # Posibles estados para una tarea
    ESTADO_NUEVA = 0
    ESTADO_EN_PROGRESO = 1
    ESTADO_RESUELTA = 2

    ESTADO_CHOICES = (
        (ESTADO_NUEVA, "Nueva"),
        (ESTADO_EN_PROGRESO, "En progreso"),
        (ESTADO_RESUELTA, "Resuelta")
    )

    estado = models.IntegerField(
        choices=ESTADO_CHOICES,
        default=ESTADO_NUEVA,
        verbose_name="Estado"
    )

    asignada_a = models.ForeignKey(
        Voluntario,
        on_delete=models.CASCADE,
        related_name="tareas",
        verbose_name="Voluntario asignado"
    )

    asignada_por = models.ForeignKey(
        Voluntario,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="tareas_que_ha_asignado",
        verbose_name="Asignada por"
    )

    def __str__(self):
        """
        Retorna una representación como string de la Tarea.
        """

        return "{0}: {1}".format(
            self.asignada_a,
            self.titulo
        )

    def completar(self):
        """
        Marca la tarea como completa y marca la fecha de resolución.
        """

        if self.estado == Tarea.ESTADO_RESUELTA:
            return

        self.estado = Tarea.ESTADO_RESUELTA
        self.fecha_de_resolucion = datetime.now()
        self.save()

class Incidencia(GeoModelo):
    """
    Representa una incidencia reportada en alguna punto geográfico.
    Hereda la información geográfica de la clase abstracta GeoModelo.
    """

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre de la Incidencia"
    )

    descripcion = models.TextField(
        default="",
        verbose_name="Descripción"
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

        return self.estado != Incidencia.ESTADO_RESUELTA

    def cambiar_estado(self, nuevo_estado):
        """
        Cambia el estado de una incidencia a un estado dado, si es válido,
        y marca las fechas importantes en caso de ser requeridas.
        """

        estados_validos = [estado[0] for estado in Incidencia.ESTADO_CHOICES]

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

    # Si el reporte lo generó algún voluntario, lo guardamos para futuros usos
    reportado_por = models.ForeignKey(
        Voluntario,
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

class Organizacion(GeoModelo):
    """
    Representa la información asociada a una organización de apoyo ante incidencias.
    Hereda la ubicación geográfica de GeoModelo.
    """

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre de la Organización"
    )

    dirigida_por = models.ManyToManyField(
        Voluntario,
        related_name="dirige",
        verbose_name="Dirigida por"
    )

class Recurso(models.Model):
    """
    Representa un tipo de recurso que puede ser asignado a alguna organización.
    """

    nombre = models.CharField(
        max_length=200,
        verbose_name="Nombre"
    )

    # Posibles tipos de recursos
    # TODO: Refinar lista de tipos posibles
    TIPO_SALUD = 0
    TIPO_ALIMENTACION = 1
    TIPO_TRANSPORTE = 2
    TIPO_OTROS = 999

    TIPO_CHOICES = (
        (TIPO_SALUD, "Salud"),
        (TIPO_ALIMENTACION, "Alimentación"),
        (TIPO_TRANSPORTE, "Transporte"),
        (TIPO_OTROS, "Otros"),
    )

    tipo = models.IntegerField(
        choices=TIPO_CHOICES,
        default=TIPO_OTROS,
        verbose_name="Tipo"
    )

    def __str__(self):
        """
        Retorna una representación como cadena de caracteres
        del recurso.
        """

        return "{0} ({1})".format(
            self.nombre,
            self.get_tipo_display()
        )

class RecursoAsignado(GeoModelo):
    """
    Representa un recurso que ha sido asignado a una organización y/o a un voluntario,
    que puede tener una ubicación con una cantidad dada.
    Hereda información de ubicación geográfica de GeoModelo.
    """

    recurso = models.ForeignKey(
        Recurso,
        on_delete=models.CASCADE,
        related_name="asignaciones",
        verbose_name="Recurso asignado"
    )

    cantidad = models.IntegerField(
        default=1,
        verbose_name="Cantidad"
    )

    organizacion = models.ForeignKey(
        Organizacion,
        on_delete=models.CASCADE,
        related_name="recursos",
        verbose_name="Organización asignada"
    )

    voluntario = models.ForeignKey(
        Voluntario,
        on_delete=models.CASCADE,
        related_name="recursos",
        verbose_name="Voluntario asignado",
        blank=True,
        null=True
    )

    def __str__(self):
        """
        Retorna una representación legible en cadena de caracteres de
        la asignación de recursos representada por el modelo.
        """

        return "{0} de {1} (cant: {2})".format(
            self.recurso,
            self.organizacion,
            self.cantidad
        )
