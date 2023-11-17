from Modelos.PacienteEvaluador import  PacienteEvaluador


class ControladorPacienteEvaluador():

    def __init__(self):
        print("Creando ControladorPacienteEvaluador")

    def index(self):
        print("Listar  PacienteEvaluador")
        unPacienteEvaluador= {
                "_date": "71192020",
                "observation": "Mal estar general cefalea",

        }
        return [unPacienteEvaluador]

    def create(self, elPacienteEvaluador):
        print("Crear pacienteEvaluador")
        elPacienteEvaluador = PacienteEvaluador(elPacienteEvaluador)
        return elPacienteEvaluador.__dict__

    def show(self, date):
        print("Mostrando un pacienteEvaluador", date)
        elPacienteEvaluador = {
                "_date": date,
                "observation": "Mal estar general cefalea"
        }
        return elPacienteEvaluador

    def update(self, date, elPacienteEvaluador):
        print("Actualizando PacienteEvaluador por medio delcodigo",date)
        elPacienteEvaluador = PacienteEvaluador(elPacienteEvaluador)
        return elPacienteEvaluador.__dict__

    def delete(self, date):
        print("Elimiando PacienteEvaluador por medio del codigo ", date)
        return {"deleted_count": 1}