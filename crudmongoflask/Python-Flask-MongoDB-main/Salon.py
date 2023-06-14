class Salon:
    def __init__(self, idSalones, numero_salon, Piso, Capacidad_estudiantes, Iluminacion_idIluminacion, Mesas_idMesas, tablero_idtablero, Tamano):
        self.idSalones = idSalones
        self.numero_salon = numero_salon
        self.Piso = Piso
        self.Capacidad_estudiantes = Capacidad_estudiantes
        self.Iluminacion_idIluminacion = Iluminacion_idIluminacion
        self.Mesas_idMesas = Mesas_idMesas
        self.tablero_idtablero = tablero_idtablero
        self.Tamano = Tamano

    def toDBCollection(self):
        return {
            'idSalones': self.idSalones,
            'numero_salon': self.numero_salon,
            'Piso': self.Piso,
            'Capacidad_estudiantes': self.Capacidad_estudiantes,
            'Iluminacion_idIluminacion': self.Iluminacion_idIluminacion,
            'Mesas_idMesas': self.Mesas_idMesas,
            'tablero_idtablero': self.tablero_idtablero,
            'Tamano': self.Tamano
        }
