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

    def verificar_relacao(self,umi,cliente):
        return umi.get_cliente().get_id() == cliente.get_id


    #media das umidades no dia corrente e que sejam pertencentes ao cliente x
    def media_umidade(self, cliente):
        media = 0
        divisor = 0
        for umi in self._lista_umidade:
            if self.verificar_capturado_hoje(umi) and self.verificar_relacao(umi,cliente):
                divisor += 1
                media += umi.get_valor()
        media = media/divisor
        return media

    