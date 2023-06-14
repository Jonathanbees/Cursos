class Motivo:
    def __init__(self, IdMotivo, indicacion):
        self.IdMotivo = IdMotivo
        self.indicacion= indicacion

    def toDBCollection(self):
        return{
            'IdMotivo': self.IdMotivo,
            'indicacion': self.indicacion,
        }