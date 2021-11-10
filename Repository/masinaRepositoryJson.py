import jsonpickle

from Domain.masina import Masina
from Repository.masinaRepository import MasinaRepository


class MasinaRepositoryJson(MasinaRepository):
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
            f.write(jsonpickle.dumps(self.masini, indent=2))

    def read(self, idMasina=None):
        self.masini = self.__readFile()
        return super().read(idMasina)

    def adauga(self, masina: Masina):
        self.masini = self.__readFile()
        super().adauga(masina)
        self.__writeFile()

    def sterge(self, idMasina):
        self.masini = self.__readFile()
        super().sterge(idMasina)
        self.__writeFile()

    def modifica(self, masina: Masina):
        self.masini = self.__readFile()
        super().modifica(masina)
        self.__writeFile()
