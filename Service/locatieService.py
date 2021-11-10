from Domain.locatie import Locatie
from Repository.locatieRepository import LocatieRepository


class LocatieService:
    def __init__(self, locatieRepository: LocatieRepository):
        self.__locatieRepository = locatieRepository

    def getAll(self):
        return self.__locatieRepository.read()

    def adauga(self, idLocatie, numeStrada, numar, bloc, scara, alteIndicatii):
        locatie = Locatie(
            idLocatie,
            numeStrada,
            numar,
            bloc,
            scara,
            alteIndicatii)
        self.__locatieRepository.adauga(locatie)

    def sterge(self, idLocatie):
        self.__locatieRepository.sterge(idLocatie)

    def modifica(self,
                 idLocatie,
                 numeStrada,
                 numar,
                 bloc,
                 scara,
                 alteIndicatii):
        locatie = Locatie(
            idLocatie,
            numeStrada,
            numar,
            bloc,
            scara,
            alteIndicatii)
        self.__locatieRepository.modifica(locatie)
