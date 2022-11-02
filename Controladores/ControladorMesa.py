from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,id):
        elMesa=Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__
    def update(self,id,infoMesa):
        mesaActual=Mesa(self.repositorioMesa.findById(id))
        mesaActual.numero_mesa=infoMesa["numero_mesa"]
        mesaActual.numero_cedulas_inscritas = infoMesa["numero_cedulas_inscritas"]
        return self.repositorioMesa.save(mesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)

