from hashlib import md5
import re
from django.db import models

class REP_EMPRESA(models.Model):
    """Model definition for REP_EMPRESA."""
    id_empresa = models.BigAutoField(primary_key=True)
    nombre_empresa = models.CharField(null=False, max_length=50)
    nit = models.BigIntegerField(null=False)
    codigo = models.BigIntegerField(null=False,unique=True)
    direccion = models.CharField( max_length=50)
    telefono = models.BigIntegerField()

    class Meta:
        """Meta definition for REP_EMPRESA."""

        verbose_name = 'REP_EMPRESA'
        verbose_name_plural = 'REP_EMPRESAs'

    def __str__(self):
        return self.nombre_empresa


class REP_PERSONA(models.Model):
    """Model definition for RE_PERSONA."""
    dpi = models.BigIntegerField(null=False,primary_key=True)    
    orden_cedula = models.BigIntegerField()
    registro_cedula = models.BigIntegerField()
    nit = models.BigIntegerField(null=False)
    telefono = models.BigIntegerField()
    correo_electronico = models.CharField( max_length=250)

    class Meta:
        """Meta definition for RE_PERSONA."""

        verbose_name = 'REP_PERSONA'
        verbose_name_plural = 'REP_PERSONAs'

    def __str__(self):
        return f'{self.dpi}-{self.orden_cedula}-{self.registro_cedula}-{self.nit}-{self.telefono}-{self.correo_electronico}'

class REP_INFO_PERSONA(models.Model):
    """Model definition for REP_INFO_PERSONA."""
    primer_nombre = models.CharField( max_length=300)
    segundo_nombre = models.CharField( max_length=350)
    primer_apellido = models.CharField( max_length=300)
    segundo_apellido = models.CharField( max_length=300)
    apellido_casada = models.CharField( max_length=300)
    fecha_nacimiento = models.DateField( auto_now=False, auto_now_add=False)
    genero = models.CharField( max_length=50)
    direccion_residencia = models.CharField( max_length=350)
    persona = models.ForeignKey(REP_PERSONA,on_delete=models.CASCADE)

    class Meta:
        """Meta definition for REP_INFO_PERSONA."""

        verbose_name = 'REP_INFO_PERSONA'
        verbose_name_plural = 'REP_INFO_PERSONAs'

    def __str__(self):
        return self.primer_nombre


class REP_TRABAJO(models.Model):
    """Model definition for REP_TRABAJO."""
    id_trabajo = models.BigAutoField(primary_key=True)
    id_persona = models.ForeignKey(REP_PERSONA,on_delete=models.CASCADE,null=True)
    fecha_inicial = models.DateField(null=False, auto_now=False, auto_now_add=False)
    fecha_final = models.DateField(null=False, auto_now=False, auto_now_add=False)
    id_empresa = models.ForeignKey(REP_EMPRESA,on_delete=models.CASCADE)
    nombre_puesto = models.CharField( max_length=350)
    mes_planilla = models.CharField( max_length=350)
    salario = models.FloatField()
    status = models.CharField(max_length=255)
    class Meta:
        """Meta definition for REP_TRABAJO."""

        verbose_name = 'REP_TRABAJO'
        verbose_name_plural = 'REP_TRABAJOs'

    def __str__(self):
        return self.nombre_puesto

class REP_VACACIONES(models.Model):
    """Model definition for REP_VACACIONES."""

    fecha_inicio = models.DateField( auto_now=False, auto_now_add=False)
    fecha_fin = models.DateField( auto_now=False, auto_now_add=False)
    persona = models.ForeignKey(REP_PERSONA,on_delete=models.CASCADE)
    contrato = models.ForeignKey(REP_TRABAJO,on_delete=models.CASCADE)

    class Meta:
        """Meta definition for REP_VACACIONES."""

        verbose_name = 'REP_VACACIONES'
        verbose_name_plural = 'REP_VACACIONESs'

    def __str__(self):
        return "s"
