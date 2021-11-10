from Domain.masinaValidator import MasinaValidator
from Repository.masinaRepositoryJson import MasinaRepositoryJson
from Service.masinaService import MasinaService
from UI.consola import Consola


def main():
    masinaValidator = MasinaValidator()
    masinaRepositoryJson = MasinaRepositoryJson("masini.json")
    masinaService = MasinaService(masinaRepositoryJson, masinaValidator)
    consola = Consola(masinaService)

    consola.runMenu()


main()
