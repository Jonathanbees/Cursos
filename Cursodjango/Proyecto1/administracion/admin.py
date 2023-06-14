from django.contrib import admin
from administracion.models import Iluminacion, Mesas, Motivo, Ocupacion, Reserva, Salones, Tablero, Usuarios

#Clases para visualizar mejor los datos en el panel
class Iluminacionadmin(admin.ModelAdmin):
    list_display= ("idiluminacion", "color", "origen", "regulacion", "ubicacion")
    search_fields= ("color", "origen", "regulacion", "ubicacion")
class Mesasadmin(admin.ModelAdmin):
    list_display= ("idmesas", "color", "tamaño")
    search_fields= ("idmesas", "color", "tamaño")
class Motivoadmin(admin.ModelAdmin):
    list_display= ("idmotivo", "indicacion")
    search_fields= ("idmotivo", "indicacion")
class Ocupacionadmin(admin.ModelAdmin):
    list_display=("idocupacion", "afiliacion")
    search_fields = ("idocupacion", "afiliacion")
class Reservaadmin(admin.ModelAdmin):
    list_display=("idreserva", "salones_idsalones", "usuarios_idusuarios", "hora_inicio", "hora_fin", "motivo_idmotivo")
    search_fields= ("idreserva","hora_inicio", "hora_fin")
class Salonesadmin(admin.ModelAdmin):
    list_display= ("idsalones", "tamaño", "piso", "capacidad_estudiantes", "numero_salon","iluminacion_idiluminacion","tablero_idtablero", "mesas_idmesas")
    searh_fields= ("tamaño", "piso", "capacidad_estudiantes", "numero_salon")
class Tableroadmin(admin.ModelAdmin):
    list_display=("idtablero", "tamaño", "tipo")
    search_fields = ("tamaño", "tipo")
class Usuariosadmin(admin.ModelAdmin):
    list_display= ("idusuarios", "nombre", "apellido", "celular", "correo", "fecha_nacimiento", "ocupacion_idocupacion")
    search_fields = ("idusuarios", "nombre", "apellido", "celular", "correo", "fecha_nacimiento")



# Register your models here.
admin.site.register(Iluminacion, Iluminacionadmin)
admin.site.register(Mesas, Mesasadmin)
admin.site.register(Motivo, Motivoadmin)
admin.site.register(Ocupacion, Ocupacionadmin)
admin.site.register(Reserva, Reservaadmin)
admin.site.register(Salones, Salonesadmin)
admin.site.register(Tablero, Tableroadmin)
admin.site.register(Usuarios, Usuariosadmin)
