# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Digeek(models.Model):
    digeekid = models.AutoField(primary_key=True)
    edicion = models.CharField(unique=True, max_length=100)
    fecha = models.DateField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'digeek'


class Eventos(models.Model):
    eventosid = models.AutoField(primary_key=True)
    expositor = models.ForeignKey('Expositor', models.DO_NOTHING)
    digeek = models.ForeignKey(Digeek, models.DO_NOTHING)
    fecha = models.DateField()
    descripcion = models.TextField()
    hora_inicio = models.TimeField()
    hora_final = models.TimeField()
    titulo = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'eventos'


class Expositor(models.Model):
    expositorid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    autobiografia = models.TextField()
    carrera = models.CharField(max_length=100)
    last_update = models.DateTimeField()
    empresa = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'expositor'


class Imagenes(models.Model):
    imagenesid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    url = models.CharField(max_length=255)
    last_update = models.DateTimeField()
    expositor = models.ForeignKey(Expositor, models.DO_NOTHING, null=True)

    class Meta:
        managed = False
        db_table = 'imagenes'


class RedesSociales(models.Model):
    redes_socialesid = models.AutoField(primary_key=True)
    expositor = models.ForeignKey(Expositor, models.DO_NOTHING)
    red_social = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'redes_sociales'


class RegistroDigeek(models.Model):
    digeek = models.ForeignKey(Digeek, models.DO_NOTHING)
    visitante = models.OneToOneField('Visitante', models.DO_NOTHING, primary_key=True)
    eventos = models.ForeignKey(Eventos, models.DO_NOTHING)
    last_update = models.DateTimeField()
    presencial = models.BooleanField(default=False)

    class Meta:
        managed = False
        db_table = 'registro_digeek'
        unique_together = (('visitante', 'digeek'),)


class Visitante(models.Model):
    visitanteid = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    edad = models.IntegerField()
    proviene_de = models.CharField(max_length=100)
    matricula = models.CharField(max_length=7, blank=True, null=True)
    url_comprobante_pago = models.ImageField(upload_to='media/', blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'visitante'


