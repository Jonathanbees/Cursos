class hijueputa:
    def __init__(self,idTablero,Tamano,Tipo):
        self.idTablero = idTablero
        self.Tamano = Tamano
        self.Tipo = Tipo

    def toDBCollection(self):
        return{
            'idTablero': self.idTablero,
            'Tamano': self.Tamano,
            'Tipo' : self.Tipo
        }