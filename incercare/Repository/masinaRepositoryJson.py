import jsonpickle

from Domain.masina import Masina
from Repository.masinaRepository import MasinaRepository


class MasinaRepositoryJson(MasinaRepository):
    def __init__(self, fileName):
        super().__init__()
        self.fileName = fileName

    def __readFile(self):
        try:
            with open(self.fileName, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.fileName, 'w') as f:
            f.write(jsonpickle.dumps(self._masini))

    def getAll(self):
        masini = self.__readFile()
        return list(masini.values())

    def getById(self, idMasina):
        masini = self.__readFile()
        if idMasina in masini:
            return masini[idMasina]
        else:
            return None

    def adauga(self, masina: Masina):
        '''

        :param masina:
        :return:
        '''
        self._masini = self.__readFile()
        super().adauga(masina)
        self.__writeFile()

    def sterge(self, idMasina):
        '''

        :param idMasina:
        :return:
        '''
        self._masini = self.__readFile()
        super().sterge(idMasina)
        self.__writeFile()

    def modifica(self, masina: Masina):
        self._masini = self.__readFile()
        super().modifica(masina)
        self.__writeFile()
