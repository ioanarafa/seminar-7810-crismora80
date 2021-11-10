from Domain.masina import Masina
from Domain.masinaValidator import MasinaValidator
from Repository.masinaRepository import MasinaRepository


class MasinaService:
    def __init__(self, masinaRepository: MasinaRepository, masinaValidator: MasinaValidator):
        self.__masinaRepository = masinaRepository
        self.__masinaValidator = masinaValidator

    def getAll(self):
        return self.__masinaRepository.read()

    def adauga(self, idMasina, indicativ, nivelConfort, plataCard, model):
        masina = Masina(idMasina, indicativ, nivelConfort, plataCard, model)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.adauga(masina)

    def sterge(self, idMasina):
        self.__masinaRepository.sterge(idMasina)

    def modifica(self, idMasina, indicativ, nivelConfort, plataCard, model):
        masina = Masina(idMasina, indicativ, nivelConfort, plataCard, model)
        self.__masinaValidator.valideaza(masina)
        self.__masinaRepository.modifica(masina)