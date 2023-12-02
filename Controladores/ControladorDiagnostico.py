from   Modelos.Diagnostico import  Diagnostico
from   Modelos.Paciente import  Paciente
from   Modelos.Evaluador import  Evaluador
from Repositorios.RepositorioDiagnostico import RepositorioDiagnostico
from Repositorios.RepositorioPaciente import RepositorioPaciente
from Repositorios.RepositorioEvaluador import RepositorioEvaluador


class ControladorDiagnostico():
    def __init__(self):
        self.repositorioDiagnostico = RepositorioDiagnostico()
        self.repositorioPaciente= RepositorioPaciente()
        self.repositorioEvaluador = RepositorioEvaluador()

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

    """
    Relación Diagnostico y Paciente
    """

    def asignarPaciente(self, id, id_paciente):
        diagnosticoActual = Diagnostico(self.repositorioDiagnostico.findById(id))
        pacienteActual = Paciente(self.repositorioPaciente.findById(id_paciente))
        diagnosticoActual.paciente = pacienteActual
        return self.repositorioDiagnostico.save(diagnosticoActual)

    """
        Relación Diagnostico y Evaluador
        """

    def asignarEvaluador(self, id, id_evaluador):
        diagnosticoActual = Diagnostico(self.repositorioDiagnostico.findById(id))
        EvaluadorActual = Evaluador(self.repositorioEvaluador.findById(id_evaluador))
        diagnosticoActual.evaluador = EvaluadorActual
        return self.repositorioDiagnostico.save(diagnosticoActual)