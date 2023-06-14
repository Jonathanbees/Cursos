class Iluminacion:
    def __init__(self,idIluminacion,Color,Origen,Regulacion, Ubicacion):
        self.idIluminacion = idIluminacion
        self.Color = Color
        self.Origen = Origen
        self.Regulacion = Regulacion
        self.Ubicacion = Ubicacion

    def toDBCollection(self):
        return{
            'idIluminacion': self.idIluminacion,
            'Color': self.Color,
            'Origen' : self.Origen,
            'Regulacion' : self.Regulacion,
            'Ubicacion' : self.Ubicacion
        }