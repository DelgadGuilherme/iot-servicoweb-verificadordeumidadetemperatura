class Cliente:
    def __init__(self,nome=None):
        self._nome = nome
        self._id = id

    def get_nome(self):
        return self._nome
    
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    
    def toDict(self):
        return {
            'id' : self._id,
            'nome' : self._nome
        }