from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Repository.masinaRepositoryJson import MasinaRepositoryJson


class MasinaService:
    def __init__(self,
                 masiniRepository: MasinaRepositoryJson,
                 masinaValidator: MasinaValidator):
        self.__masiniRepository = masiniRepository
        self.__masinaValidator = masinaValidator

    def getAll(self):
        return self.__masiniRepository.getAll()

    def adauga(self, idMasina, indicativ, nivelConfort, plataCard, model):
        '''

        :param idMasina:
        :param indicativ:
        :param nivelConfort:
        :param plataCard:
        :param model:
        :return:
        '''
        masina = Masina(idMasina, indicativ, nivelConfort, plataCard, model)
        self.__masinaValidator.valideaza(masina)
        self.__masiniRepository.adauga(masina)

    def sterge(self, idMasina):
        '''

        :param idMasina:
        :return:
        '''
        self.__masiniRepository.sterge(idMasina)

    def modifica(self, idMasina, indicativ, nivelConfort, plataCard, model):
        masina = Masina(idMasina, indicativ, nivelConfort, plataCard, model)
        self.__masinaValidator.valideaza(masina)
        self.__masiniRepository.modifica(masina)
