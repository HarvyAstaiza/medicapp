from Modelos.Paciente import Paciente
from Repositorios.RepositorioPaciente import RepositorioPaciente

class ControladorPaciente():

    def __init__(self):
        self.repositorioPaciente = RepositorioPaciente()

    def index(self):
        return self.repositorioPaciente.findAll()

    def create(self, infoPaciente):
        nuevaPaciente = Paciente(infoPaciente)
        return self.repositorioPaciente.save(nuevaPaciente)

    def show(self, id):
        elPaciente = Paciente(self.repositorioPaciente.findById(id))
        return elPaciente.__dict__

    def update(self, id, infoPaciente):
        pacienteActual = Paciente(self.repositorioPaciente.findById(id))
        pacienteActual.name = infoPaciente["name"]
        pacienteActual.lastname = infoPaciente["lastname"]
        pacienteActual.weigth = infoPaciente["weigth"]
        pacienteActual.size = infoPaciente["size"]
        return self.repositorioPaciente.save(pacienteActual)

    def delete(self, id):
        return self.repositorioPaciente.delete(id)

