from Domain.masinaValidator import MasinaValidator
from Repository.masinaRepositoryJson import MasinaRepositoryJson
from Service.masinaService import MasinaService
from UI.consola import Consola


def main():
    masinaRepositoryJson = MasinaRepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson, masinaValidator)
    consola = Consola(masinaService)

    consola.runMenu()

main()