from application.model.dao.umidade_dao import UmidadeDAO
from application.model.entity.umidade import Umidade
from application.model.entity.cliente import Cliente
from flask import  request, jsonify
from application import app

@app.route("/umidade")
def umidade():
    valor = request.json['valor']
    cliente_id = request.json['cliente']['id']
    
    cliente = Cliente()
    cliente.set_id(cliente_id)
    umidade = Umidade(valor,cliente)
    umidade_cadastrada = UmidadeDAO().inserir(umidade)
    return jsonify(umidade_cadastrada.toDict())
