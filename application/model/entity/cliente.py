class Cliente:
    def __init__(self,nome):
        self._nome = nome

    def get_nome(self):
        return self._nome
    
    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id