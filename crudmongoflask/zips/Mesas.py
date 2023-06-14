class Mesas:
    def __init__(self,idMesas,Color,Tamano):
        self.idMesas = idMesas
        self.Color = Color
        self.Tamano = Tamano

    def toDBCollection(self):
        return{
            'idMesas': self.idMesas,
            'Color': self.Color,
            'Tamano' : self.Tamano
        }