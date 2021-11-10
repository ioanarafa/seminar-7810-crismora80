from Domain.comanda import Comanda
from Repository.comandaRepository import ComandaRepository
from Repository.locatieRepository import LocatieRepository
from Repository.masinaRepository import MasinaRepository


class ComandaService:
    def __init__(self,
                 comandaRepository: ComandaRepository,
                 masinaRepository: MasinaRepository,
                 locatieRepository: LocatieRepository):
        self.__comandaRepository = comandaRepository
        self.__masinaRepository = masinaRepository
        self.__locatieRepository = locatieRepository

    def getAll(self):
        return self.__comandaRepository.read()

    def adauga(self,
               idComanda,
               idMasina,
               idLocatie,
               timpFinal,
               costPerKm,
               distantaParcursa,
               status):
        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__locatieRepository.read(idLocatie) is None:
            raise KeyError("Nu exista nicio locatie cu id-ul dat!")

        comanda = Comanda(
            idComanda,
            idMasina,
            idLocatie,
            timpFinal,
            costPerKm,
            distantaParcursa,
            status
        )
        self.__comandaRepository.adauga(comanda)

    def sterge(self, idComanda):
        self.__comandaRepository.sterge(idComanda)

    def modifica(self,
                 idComanda,
                 idMasina,
                 idLocatie,
                 timpFinal,
                 costPerKm,
                 distantaParcursa,
                 status):
        if self.__masinaRepository.read(idMasina) is None:
            raise KeyError("Nu exista nicio masina cu id-ul dat!")
        if self.__locatieRepository.read(idLocatie) is None:
            raise KeyError("Nu exista nicio locatie cu id-ul dat!")

        comanda = Comanda(
            idComanda,
            idMasina,
            idLocatie,
            timpFinal,
            costPerKm,
            distantaParcursa,
            status
        )
        self.__comandaRepository.modifica(comanda)
