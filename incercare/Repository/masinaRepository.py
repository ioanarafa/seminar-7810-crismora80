from copy import deepcopy

from Domain.masina import Masina


class MasinaRepository:
    def __init__(self):
        self._masini = {}

    def getAll(self):
        return list(self._masini.values())

    def getById(self, idMasina):
        '''

        :param idMasina:
        :return:
        '''
        if idMasina in self._masini:
            return self._masini[idMasina]
        else:
            return None

    def adauga(self, masina: Masina):
        '''

        :param masina:
        :return:
        '''
        if self.getById(masina.idMasina):
            raise KeyError(f"Exista deja o maisna cu id-ul {masina.idMasina}")

        self._masini[masina.idMasina] = masina

    def sterge(self, idMasina):
        '''

        :param idMasina:
        :return:
        '''
        if self.getById(idMasina) is None:
            raise KeyError(f"Nu exista deja o maisna cu id-ul {idMasina}")
        del self._masini[idMasina]

    def modifica(self, masina: Masina):
        if self.getById(masina.idMasina) is None:
            raise KeyError(
                f"Nu exista deja o maisna cu id-ul {masina.idMasina}"
            )
        self._masini[masina.idMasina] = masina
