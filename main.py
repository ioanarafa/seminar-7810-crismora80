from xmlrpc.client import DateTime

from Domain.masinaValidator import MasinaValidator
from Repository.repositoryJson import RepositoryJson
from Service.comandaService import ComandaService
from Service.locatieService import LocatieService
from Service.masinaService import MasinaService
from UI.consola import Consola


def main():
    masinaRepositoryJson = RepositoryJson("masini.json")
    masinaValidator = MasinaValidator()
    masinaService = MasinaService(masinaRepositoryJson, masinaValidator)

    locatieRepositoryJson = RepositoryJson("locatii.json")
    locatieService = LocatieService(locatieRepositoryJson)

    comandaRepositoryJson = RepositoryJson("comenzi.json")
    comandaService = ComandaService(
        comandaRepositoryJson,
        masinaRepositoryJson,
        locatieRepositoryJson)

    consola = Consola(masinaService, locatieService, comandaService)

    consola.runMenu()


main()
