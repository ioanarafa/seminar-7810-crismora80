import jsonpickle

from Domain.comanda import Comanda
from Repository.comandaRepository import ComandaRepository


class ComandaRepositoryJson(ComandaRepository):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as f:
            f.write(jsonpickle.dumps(self.comenzi, indent=2))

    def read(self, idComanda=None):
        self.comenzi = self.__readFile()
        return super().read(idComanda)

    def adauga(self, comanda: Comanda):
        self.comenzi = self.__readFile()
        super().adauga(comanda)
        self.__writeFile()

    def sterge(self, idComanda):
        self.comenzi = self.__readFile()
        super().sterge(idComanda)
        self.__writeFile()

    def modifica(self, comanda: Comanda):
        self.comenzi = self.__readFile()
        super().modifica(comanda)
        self.__writeFile()
