from Domain.locatie import Locatie


class LocatieRepository:
    def __init__(self):
        self.locatii = {}

    def read(self, idLocatie=None):
        if idLocatie is None:
            return list(self.locatii.values())

        if idLocatie in self.locatii:
            return self.locatii[idLocatie]
        else:
            return None

    def adauga(self, locatie: Locatie):
        if self.read(locatie.idLocatie) is not None:
            raise KeyError("Exista deja o locatie cu id-ul dat!")
        self.locatii[locatie.idLocatie] = locatie

    def sterge(self, idLocatie: str):
        if self.read(idLocatie) is None:
            raise KeyError("Nu exista nicio locatie cu id-ul dat!")
        del self.locatii[idLocatie]

    def modifica(self, locatie: Locatie):
        if self.read(locatie.idLocatie) is None:
            raise KeyError("Nu exista nicio locatie cu id-ul dat!")
        self.locatii[locatie.idLocatie] = locatie
