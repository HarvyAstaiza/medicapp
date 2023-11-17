from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorPaciente import ControladorPaciente

app=Flask(__name__)

cors=CORS(app)
miControladorPaciente=ControladorPaciente()


@app.route("/", methods=['GET'])
def test():
    json={}
    json["message"]="Server running ..."
    return jsonify(json)


#Pacientes

@app.route("/pacientes",methods=['GET'])
def getPacientes():
    json=miControladorPaciente.index()
    return jsonify(json)


def loadFileConfig():
    with open('config.json') as f:
        data=json.load(f)
    return data


if __name__ == '__main__':
    dataConfig=loadFileConfig()  # Se asigna lo que retorna el metodo a la variable dataConfig
    print("Server running : "+"http://"+dataConfig["url-backend"]+":"+str(dataConfig["port"]))
    app.run()
