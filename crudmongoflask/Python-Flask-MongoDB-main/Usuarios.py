class Usuarios:
    def __init__(self, idUsuarios, Nombre, Apellido, Celular, Correo, Ocupacion_idOcupacion, Fecha_nacimiento):
        self.idUsuarios = idUsuarios
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Celular = Celular
        self.Correo = Correo
        self.Ocupacion_idOcupacion = Ocupacion_idOcupacion
        self.Fecha_nacimiento = Fecha_nacimiento

    def toDBCollection(self):
        return{
            'idUsuarios': self.idUsuarios,
            'Nombre': self.Nombre,
            'Apellido': self.Apellido,
            'Celular': self.Celular,
            'Correo': self.Correo,
            'Ocupacion_idOcupacion': self.Ocupacion_idOcupacion,
            'Fecha_nacimiento': self.Fecha_nacimiento

        }
