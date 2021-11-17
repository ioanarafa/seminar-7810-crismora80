from Domain.comanda import Comanda
from Repository.repository import Repository
from ViewModels.masinaCostMediuViewModel import MasinaCostMediuViewModel
from ViewModels.locatieComandaViewModel import LocatieComandaViewModel
from ViewModels.locatieComenziViewModel import LocatieComenziViewModel
from ViewModels.locatieDistantaComandaViewModel import LocatieDistantaComandaViewModel


class ComandaService:
    def __init__(self,
                 comandaRepository: Repository,
                 masinaRepository: Repository,
                 locatieRepository: Repository):
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
        if comanda.distantaParcursa > 100:
            comanda.timpFinal = 0.9*comanda.timpFinal
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

    def ordoneazaMasiniDupaCostMediu(self):
        costuriPerMasini = {}
        rezultat = []
        for masina in self.__masinaRepository.read():
            costuriPerMasini[masina.idEntitate] = []
        for comanda in self.__comandaRepository.read():
            costuriPerMasini[comanda.idMasina].append(comanda.costPerKm)

        for idMasina in costuriPerMasini:
            costuri = costuriPerMasini[idMasina]
            rezultat.append(MasinaCostMediuViewModel(
                self.__masinaRepository.read(idMasina),
                sum(costuri) / len(costuri) if costuri else 0
            ))

        return sorted(rezultat, key=lambda costPerMasina: costPerMasina.costMediu)

    def locatieCuComandaCeaMaiLunga(self):
        '''
        determina locatia cu loaatia cea mai lunga (daca sunt mai multe, se gaseste doar una din ele)
        :return: o locatie, impreuna cu comanda ei ce reprezinta cea ami lunga comanda
        '''
        comenzi = self.__comandaRepository.read()

        if not comenzi:
            return None

        comandaDistantaMax = max(comenzi, key=lambda comanda: comanda.distantaParcursa)
        return self.__locatieRepository.read(comandaDistantaMax.idLocatie)

    def locatiiCuCeleMaiLungiComenzi(self):
        '''
        determinaa toate locatiile care au cel putin o comanda cu distanta egala cu distanta maxima a comenzilor (per toate comenzile)
        :return: o lista de locatii, impreuna cu comanda aferenta ei cu distanta maxima (per toate comenzile) sau None, daca nu exista
        '''
        comenzi = self.__comandaRepository.read()

        if not comenzi:
            return None

        rezultat = []
        comandaDistantaMax = max(comenzi, key=lambda comanda: comanda.distantaParcursa)
        distantaMax = comandaDistantaMax.distantaParcursa

        for comanda in comenzi:
            if comanda.distantaParcursa == distantaMax:
                rezultat.append(LocatieComandaViewModel(
                    self.__locatieRepository.read(comanda.idLocatie),
                    comanda
                ))
        return rezultat

    def locatieCuCeaMaiLungaSumaAComenzilor(self):
        '''
        determina locatia care are suma maxima a distantelor comenzilor
        :return: o locatie, impreuna cu suma comenzilor sale sau None, daca nu exista o astfel de locatie
        '''
        distantaPentruLocatii = {}

        for comanda in self.__comandaRepository.read():
            if comanda.idLocatie not in distantaPentruLocatii:
                distantaPentruLocatii[comanda.idLocatie] = comanda.distantaParcursa
            else:
                distantaPentruLocatii[comanda.idLocatie] = \
                    distantaPentruLocatii[comanda.idLocatie] + comanda.distantaParcursa

        if not distantaPentruLocatii:
            return None

        idLocatieCuCeleMaiLungiComenzi = max(
            distantaPentruLocatii.keys(),
            key=lambda idLocatie: distantaPentruLocatii[idLocatie]
        )
        return LocatieDistantaComandaViewModel(
            self.__locatieRepository.read(idLocatieCuCeleMaiLungiComenzi),
            distantaPentruLocatii[idLocatieCuCeleMaiLungiComenzi]
        )

    def locatiiComenziMaiLungiDecat(self, distantaMax):
        '''
        determina toate locatiile care au cel putin o comanda cu distanta mai mica decat o distanta data
        :param distantaMax: float
        :return: o lista continand locatii, impreuna cu comenzile lor mai scurte decat distantaMax
        '''
        locatiiComenzi = {}
        rezultat=[]
        for comanda in self.__comandaRepository.read():
            if comanda.distantaParcursa < distantaMax:
                if comanda.idLocatie not in locatiiComenzi:
                    locatiiComenzi[comanda.idLocatie] = [comanda]
                else:
                    locatiiComenzi[comanda.idLocatie].append(comanda)
        for idLocatie in locatiiComenzi:
            rezultat.append(LocatieComenziViewModel(
                self.__locatieRepository.read(idLocatie),
                locatiiComenzi[idLocatie]
            ))
        return rezultat


