from Domain.masinaValidator import MasinaValidator
from Repository.locatieRepositoryJson import LocatieRepositoryJson
from Repository.masinaRepositoryJson import MasinaRepositoryJson
from Service.locatieService import LocatieService
from Service.masinaService import MasinaService
from UI.consola import Consola


def main():
    masinaRepositoryJson = MasinaRepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson, masinaValidator)

    locatieRepositoryJson = LocatieRepositoryJson("locatii.json")
    locatieService = LocatieService(locatieRepositoryJson)

    consola = Consola(masinaService, locatieService)

    consola.runMenu()


main()
