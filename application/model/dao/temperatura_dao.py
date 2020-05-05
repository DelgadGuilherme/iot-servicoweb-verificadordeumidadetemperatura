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

    def verificar_relacao(self,temp,cliente):
        return temp.get_cliente().get_id() == cliente.get_id

    def maior_que(self,temp,max_temp):
        return temp.get_valor() > max_temp.get_valor()

    def menor_que(self,temp,min_temp):
        return temp.get_valor() < min_temp.get_valor()

    #temperatura maxima do dia corrente informada por um cliente x
    def max_temperatura(self,cliente):
        max_temp = self._lista_temperatura[0]
        for temp in self._lista_temperatura:
            if self.verificar_capturado_hoje(temp) and self.maior_que(temp,max_temp) and self.verificar_relacao(temp,cliente):
                max_temp = temp
        return max_temp
        
    #temperatura minima do dia corrente informada por um cliente x    
    def min_temperatura(self,cliente):
        min_temp = self._lista_temperatura[0]
        for temp in self._lista_temperatura:
            if self.verificar_capturado_hoje(temp) and self.menor_que(temp,min_temp) and self.verificar_relacao(temp,cliente):
                min_temp = temp
        return min_temp

    def media_temperatura(self,cliente):
        media = 0
        divisor = 0
        for temp in self._lista_temperatura:
            if self.verificar_capturado_hoje(temp) and self.verificar_relacao(temp,cliente):
                divisor += 1
                media += temp.get_valor()
        media = media/divisor
        return media