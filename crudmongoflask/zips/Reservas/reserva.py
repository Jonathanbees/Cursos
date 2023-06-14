class Reserva:
    def __init__(self, idReserva, Hora_fin, Hora_inicio, Motivo_idMotivo, Salones_idSalones, Usuarios_idUsuarios):
        self.idReserva = idReserva
        self.Hora_fin = Hora_fin
        self.Hora_inicio = Hora_inicio
        self.Motivo_idMotivo = Motivo_idMotivo
        self.Salones_idSalones = Salones_idSalones
        self.Usuarios_idUsuarios = Usuarios_idUsuarios

    def toDBCollection(self):
        return{
            'idReserva': self.idReserva,
            'Hora_fin': self.Hora_fin,
            'Hora_inicio': self.Hora_inicio,
            'Motivo_idMotivo': self.Motivo_idMotivo,
            'Salones_idSalones': self.Salones_idSalones,
            'Usuarios_idUsuarios': self.Usuarios_idUsuarios
        }
