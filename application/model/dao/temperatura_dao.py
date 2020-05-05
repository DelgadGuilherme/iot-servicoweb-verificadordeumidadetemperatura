from application.model.entity.temperatura import Temperatura
from datetime import date

class TemperaturaDao:
    def __init__(self):
        self._lista_temperatura = []

    def inserir(self, temp):
        temp.set_id(len(self._lista_temperatura)+1)
        temp.set_data(date.today())
        self._lista_temperatura.append(temp)
        return temp

    def verificar_capturado_hoje(self,temp):
        today = date.today()
        return today == temp.get_data()
    
    def max_temperatura(self):
        max_temp = self._lista_temperatura[0]
        for temp in self._lista_temperatura:
            if self.verificar_capturado_hoje(temp) and temp.get_valor() > max_temp.get_valor():
                max_temp = temp
        return max_temp
        
    def min_temperatura(self):
        min_temp = self._lista_temperatura[0]
        for temp in self._lista_temperatura:
            if self.verificar_capturado_hoje(temp) and temp.get_valor() < min_temp.get_valor():
                min_temp = temp
        return min_temp

     def media_temperatura(self):
        media = 0
        divisor = 0
        for temp in self._lista_temperatura:
            if self.verificar_capturado_hoje(temp):
                divisor += 1
                media += temp.get_valor()
        media = media/divisor
        return media