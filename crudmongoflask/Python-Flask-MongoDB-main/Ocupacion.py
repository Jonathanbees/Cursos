class Ocupacion: 
    def __init__ (self,idOcupacion,Afiliacion):
        self.idOcupacion = idOcupacion
        self.Afiliacion = Afiliacion

    def toDBCollection(self):
        return{
            'idOcupacion' : self.idOcupacion,
            'Afiliacion': self.Afiliacion

        }