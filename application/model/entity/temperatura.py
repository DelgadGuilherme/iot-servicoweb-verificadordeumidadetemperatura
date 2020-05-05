class Temperatura:
    def __init__(self,valor):
        self._valor = valor

    def get_id(self):
        return self._id

    def get_valor(self):
        return self._valor

    def get_data(self):
        return self._data

    def set_id(self, id):
        self._id = id

    def set_data(self,data):
        self._data = data