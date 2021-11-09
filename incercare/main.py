from Domain.masinaValidator import MasinaValidator
from Repository.masinaRepositoryJson import MasinaRepositoryJson
from Service.masinaService import MasinaService
from UI.console import Consola


def main():
    masinaRepository = MasinaRepositoryJson('masini.json')
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepository, masinaValidator)

    console = Consola(masinaService)

    console.runMenu()


main()
