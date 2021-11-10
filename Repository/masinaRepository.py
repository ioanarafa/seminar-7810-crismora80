from Domain.masina import Masina


class MasinaRepository:
    def __init__(self):
        self.masini = {}

    def read(self, idMasina=None):
        if idMasina is None:
            return list(self.masini.values())

        if idMasina in self.masini:
            return self.masini[idMasina]
        else:
            return None

    def adauga(self, masina: Masina):
        if self.read(masina.idMasina) is not None:
            raise KeyError("Exista deja o masina cu id-ul dat!")
        self.masini[masina.idMasina] = masina

    def sterge(self, idMasina: str):
        if self.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        del self.masini[idMasina]

    def modifica(self, masina: Masina):
        if self.read(masina.idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        self.masini[masina.idMasina] = masina
