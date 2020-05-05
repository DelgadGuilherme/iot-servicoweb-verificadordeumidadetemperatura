class Temperatura:
    def __init__(self,valor, cliente):
        self._valor = valor
        self._cliente = cliente

    def get_id(self):
        return self._id

    def get_valor(self):
        return self._valor

    def get_data(self):
        return self._data

    def get_cliente(self):  
        return self._cliente 

    def set_id(self, id):
        self._id = id

    def set_data(self,data):
        self._data = data

    def set_cliente(self,cliente):
        self._cliente = cliente