from django.db import models

# Create your models here.


class Ocupacion(models.Model):
    idocupacion = models.IntegerField(db_column='idOcupacion', primary_key=True)  # Field name made lowercase.
    afiliacion = models.CharField(db_column='Afiliacion', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'ocupacion'


class Usuarios(models.Model):
    idusuarios = models.IntegerField(db_column='idUsuarios', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    apellido = models.CharField(db_column='Apellido', max_length=45)  # Field name made lowercase.
    celular = models.CharField(db_column='Celular', max_length=45)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', max_length=100)  # Field name made lowercase.
    fecha_nacimiento = models.DateField(db_column='Fecha_nacimiento')  # Field name made lowercase.
    ocupacion_idocupacion = models.ForeignKey(Ocupacion, models.DO_NOTHING, db_column='Ocupacion_idOcupacion')  # Field name made lowercase.
    class Meta:
        db_table = 'usuarios'
     

class Iluminacion(models.Model):
    idiluminacion = models.IntegerField(db_column='idIluminacion', primary_key=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=45)  # Field name made lowercase.
    origen = models.CharField(db_column='Origen', max_length=45)  # Field name made lowercase.
    regulacion = models.IntegerField(db_column='Regulacion')  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'iluminacion'

class Tablero(models.Model):
    idtablero = models.IntegerField(db_column='idTablero', primary_key=True)  # Field name made lowercase.
    tamaño = models.CharField(db_column='Tamaño', max_length=45)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'tablero'


class Mesas(models.Model):
    idmesas = models.IntegerField(db_column='idMesas', primary_key=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=45)  # Field name made lowercase.
    tamaño = models.CharField(db_column='Tamaño', max_length=45)  # Field name made lowercase.

    class Meta:
        db_table = 'mesas'


class Salones(models.Model):
    idsalones = models.IntegerField(db_column='idSalones', primary_key=True)  # Field name made lowercase.
    tamaño = models.CharField(db_column='Tamaño', max_length=45)  # Field name made lowercase.
    piso = models.IntegerField(db_column='Piso')  # Field name made lowercase.
    capacidad_estudiantes = models.IntegerField(db_column='Capacidad_estudiantes')  # Field name made lowercase.
    numero_salon = models.IntegerField()
    iluminacion_idiluminacion = models.ForeignKey(Iluminacion, models.DO_NOTHING, db_column='Iluminacion_idIluminacion')  # Field name made lowercase.
    tablero_idtablero = models.ForeignKey('Tablero', models.DO_NOTHING, db_column='tablero_idtablero')
    mesas_idmesas = models.ForeignKey(Mesas, models.DO_NOTHING, db_column='Mesas_idMesas')  # Field name made lowercase.

    class Meta:
        db_table = 'salones'

class Motivo(models.Model):
    idmotivo = models.IntegerField(db_column='idMotivo', primary_key=True)  # Field name made lowercase.
    indicacion = models.CharField(db_column='Indicacion', max_length=100)  # Field name made lowercase.

    class Meta:
        db_table = 'motivo'



class Reserva(models.Model):
    idreserva = models.IntegerField(db_column='idReserva', primary_key=True)  # Field name made lowercase.
    salones_idsalones = models.ForeignKey('Salones', models.DO_NOTHING, db_column='Salones_idSalones')  # Field name made lowercase.    
    usuarios_idusuarios = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='Usuarios_idUsuarios')  # Field name made lowercase.
    hora_inicio = models.TimeField(db_column='Hora_inicio')  # Field name made lowercase.
    hora_fin = models.TimeField(db_column='Hora_fin')  # Field name made lowercase.
    motivo_idmotivo = models.ForeignKey(Motivo, models.DO_NOTHING, db_column='Motivo_idMotivo')  # Field name made lowercase.       

    class Meta:
        db_table = 'reserva'
        unique_together = (('idreserva', 'salones_idsalones', 'usuarios_idusuarios'),)
