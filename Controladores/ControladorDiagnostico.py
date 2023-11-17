from   Modelos.Diagnostico import  Diagnostico
from Repositorios.RepositorioDiagnostico import RepositorioDiagnostico


class ControladorDiagnostico():
    def __init__(self):
        self.repositorioDiagnostico = RepositorioDiagnostico()

    def index(self):
        return self.repositorioDiagnostico.findAll()

    def create(self, infoDiagnostico):
        nuevaDiagnostico = Diagnostico(infoDiagnostico)
        return self.repositorioDiagnostico.save(nuevaDiagnostico)

    def show(self, id):
        elDiagnostico = Diagnostico(self.repositorioDiagnostico.findById(id))
        return elDiagnostico.__dict__

    def update(self, id, infoDiagnostico):
        diagnosticoActual = Diagnostico(self.repositorioDiagnostico.findById(id))
        diagnosticoActual.code= infoDiagnostico["code"]
        diagnosticoActual.description = infoDiagnostico["description"]
        diagnosticoActual.typeofmalnutrition = infoDiagnostico["typeofmalnutrition"]
        return self.repositorioDiagnostico.save(diagnosticoActual)

    def delete(self, id):
        return self.repositorioDiagnostico.delete(id)
