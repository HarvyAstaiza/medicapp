from Modelos.Evaluador import  Evaluador
from Repositorios.RepositorioEvaluador import RepositorioEvaluador

class ControladorEvaluador():
    def __init__(self):
        self.repositorioEvaluador = RepositorioEvaluador()

    def index(self):
        return self.repositorioEvaluador.findAll()

    def create(self, infoEvaluador):
        nuevoEvaluador = Evaluador(infoEvaluador)
        return self.repositorioEvaluador.save(nuevoEvaluador)

    def show(self, id):
        elEvaluador = Evaluador(self.repositorioEvaluador.findById(id))
        return elEvaluador.__dict__

    def update(self, id, infoEvaluador):
        evaluadorActual = Evaluador(self.repositorioEvaluador.findById(id))
        evaluadorActual.name = infoEvaluador["name"]
        evaluadorActual.lastname = infoEvaluador["lastname"]
        evaluadorActual.job = infoEvaluador["job"]
        return self.repositorioEvaluador.save(evaluadorActual)

    def delete(self, id):
        return self.repositorioEvaluador.delete(id)
