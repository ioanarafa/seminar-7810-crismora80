import jsonpickle
from Domain.locatie import Locatie
from Repository.locatieRepository import LocatieRepository


class LocatieRepositoryJson(LocatieRepository):
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
            f.write(jsonpickle.dumps(self.locatii, indent=2))

    def read(self, idLocatie=None):
        self.locatii = self.__readFile()
        return super().read(idLocatie)

    def adauga(self, locatie: Locatie):
        self.locatii = self.__readFile()
        super().adauga(locatie)
        self.__writeFile()

    def sterge(self, idLocatie):
        self.locatii = self.__readFile()
        super().sterge(idLocatie)
        self.__writeFile()

    def modifica(self, locatie: Locatie):
        self.locatii = self.__readFile()
        super().modifica(locatie)
        self.__writeFile()
