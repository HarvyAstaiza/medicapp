from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPaciente import ControladorPaciente
from Controladores.ControladorDiagnostico import ControladorDiagnostico
from  Controladores.ContoladorEvaluador import ControladorEvaluador
app=Flask(__name__)

cors=CORS(app)
miControladorPaciente=ControladorPaciente()
miControladorEvaluador=ControladorEvaluador()
miControladorDiagnostico=ControladorDiagnostico()

@app.route("/", methods=['GET'])
def test():
    json={}
    json["message"]="Server running ..."
    return jsonify(json)


# Pacientes

@app.route("/pacientes", methods=['GET'])
def getPacientes():
    json=miControladorPaciente.index()
    return jsonify(json)


@app.route("/pacientes/<string:id>", methods=['GET'])
def getPaciente(id):
    json=miControladorPaciente.show(id)
    return jsonify(json)


@app.route("/pacientes", methods=['POST'])
def crearPacientes():
    data=request.get_json()
    json=miControladorPaciente.create(data)
    return jsonify(json)


@app.route("/pacientes/<string:id>", methods=['PUT'])
def modificarPacientes(id):
    data=request.get_json()
    json=miControladorPaciente.update(id, data)
    return jsonify(json)


@app.route("/pacientes/<string:id>", methods=['DELETE'])
def eliminarPacientes(id):
    json=miControladorPaciente.delete(id)
    return jsonify(json)


# evaluador
@app.route("/evaluadores", methods=['GET'])
def getEvaluadores():
    json=miControladorEvaluador.index()
    return jsonify(json)


@app.route("/evaluadores/<string:id>", methods=['GET'])
def getEvaluador(id):
    json=miControladorEvaluador.show(id)
    return jsonify(json)


@app.route("/evaluadores", methods=['POST'])
def crearEvaluadores():
    data=request.get_json()
    json=miControladorEvaluador.create(data)
    return jsonify(json)


@app.route("/evaluadores/<string:id>", methods=['PUT'])
def modificarEvaluadores(id):
    data=request.get_json()
    json=miControladorEvaluador.update(id, data)
    return jsonify(json)


@app.route("/evaluadores/<string:id>", methods=['DELETE'])
def eliminarEvaluador(id):
    json=miControladorEvaluador.delete(id)
    return jsonify(json)


# Diagnostico
@app.route("/diagnosticos", methods=['GET'])
def getDiagnosticos():
    json=miControladorDiagnostico.index()
    return jsonify(json)


@app.route("/diagnosticos/<string:id>", methods=['GET'])
def getDiagnostico(id):
    json=miControladorDiagnostico.show(id)
    return jsonify(json)


@app.route("/diagnosticos", methods=['POST'])
def crearDiagnosticos():
    data=request.get_json()
    json=miControladorDiagnostico.create(data)
    return jsonify(json)


@app.route("/diagnosticos/<string:id>", methods=['PUT'])
def modificarDiagnosticos(id):
    data=request.get_json()
    json=miControladorDiagnostico.update(id, data)
    return jsonify(json)


@app.route("/diagnosticos/<string:id>", methods=['DELETE'])
def eliminarDiagnosticos(id):
    json=miControladorDiagnostico.delete(id)
    return jsonify(json)

def loadFileConfig():
    with open('config.json') as f:
        data=json.load(f)
    return data


if __name__ == '__main__':
    dataConfig=loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])


    app.run()
