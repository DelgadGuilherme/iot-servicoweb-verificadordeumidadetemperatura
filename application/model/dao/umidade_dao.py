from application.model.entity.umidade import Umidade
from datetime import date

class UmidadeDAO:
 
    def __init__(self):
        self._lista_umidade = []

    def inserir(self, umi):
        umi.set_id(len(self._lista_umidade)+1)
        umi.set_data(date.today())
        self._lista_umidade.append(umi)
        return umi

    def verificar_capturado_hoje(self,umi):
        today = date.today()
        return today == umi.get_data()

    def max_umidade(self):
        max_umi = self._lista_umidade[0]
        for umi in self._lista_umidade:
            if self.verificar_capturado_hoje(umi) and umi.get_valor() > max_umi.get_valor():
                max_umi = umi
        return max_umi
        
    def min_umidade(self):
        min_umi = self._lista_umidade[0]
        for umi in self._lista_umidade:
            if self.verificar_capturado_hoje(umi) and umi.get_valor() < min_umi.get_valor():
                min_umi = umi
        return min_umi

    def media_umidade(self):
        media = 0
        divisor = 0
        for umi in self._lista_umidade:
            if self.verificar_capturado_hoje(umi):
                divisor += 1
                media += umi.get_valor()
        media = media/divisor
        return media