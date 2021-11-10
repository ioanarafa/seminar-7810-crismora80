from Service.comandaService import ComandaService
from Service.locatieService import LocatieService
from Service.masinaService import MasinaService


class Consola:
    def __init__(self,
                 masinaService: MasinaService,
                 locatieService: LocatieService,
                 comandaService: ComandaService):
        self.__masinaService = masinaService
        self.__locatieService = locatieService
        self.__comandaService = comandaService

    def runMenu(self):
        while True:
            print("1. CRUD masini")
            print("2. CRUD locatii")
            print("3. CRUD comenzi")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDMasiniMenu()
            elif optiune == "2":
                self.runCRUDLocatiiMenu()
            elif optiune == "3":
                self.runCRUDComenziMenu()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDMasiniMenu(self):
        while True:
            print("1. Adauga masina")
            print("2. Sterge masina")
            print("3. Modifica masina")
            print("a. Afiseaza toate masinile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaMasina()
            elif optiune == "2":
                self.uiStergeMasina()
            elif optiune == "3":
                self.uiModificaMasina()
            elif optiune == "a":
                self.showAllMasini()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDLocatiiMenu(self):
        while True:
            print("1. Adauga locatie")
            print("2. Sterge locatie")
            print("3. Modifica locatie")
            print("a. Afiseaza toate locatiile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaLocatie()
            elif optiune == "2":
                self.uiStergeLocatie()
            elif optiune == "3":
                self.uiModificaLocatie()
            elif optiune == "a":
                self.showAllLocatie()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii: ")
            indicativ = input("Dati indicativul masinii: ")
            nivelConfort = input("Dati nivelul de confort al masinii "
                                 "(standard, ridicat, premium): ")
            plataCard = input("Dati plata card (da/nu) a masinii: ")
            model = input("Dati modelul masinii: ")

            self.__masinaService.adauga(
                idMasina, indicativ, nivelConfort, plataCard, model)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de sters: ")

            self.__masinaService.sterge(idMasina)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de modificat: ")
            indicativ = input("Dati noul indicativ al masinii: ")
            nivelConfort = input("Dati noul nivel de confort al masinii "
                                 "(standard, ridicat, premium) : ")
            plataCard = input("Dati noua plata card (da/nu) a masinii: ")
            model = input("Dati noul modelul al masinii: ")

            self.__masinaService.modifica(
                idMasina, indicativ, nivelConfort, plataCard, model)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllMasini(self):
        for masina in self.__masinaService.getAll():
            print(masina)

    def uiAdaugaLocatie(self):
        try:
            idLocatie = input("Dati id-ul locatiei: ")
            numeStrada = input("Dati numele strazii: ")
            numar = int(input("Dati numarul: "))
            bloc = input("Dati blocul: ")
            scara = input("Dati scara: ")
            alteIndicatii = input("Dati alte indicatii: ")

            self.__locatieService.adauga(
                idLocatie, numeStrada, numar, bloc, scara, alteIndicatii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeLocatie(self):
        try:
            idLocatie = input("Dati id-ul locatiei de sters: ")

            self.__locatieService.sterge(idLocatie)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaLocatie(self):
        try:
            idLocatie = input("Dati id-ul locatiei de modificat: ")
            numeStrada = input("Dati noul nume al strazii: ")
            numar = int(input("Dati noul numar: "))
            bloc = input("Dati noul bloc: ")
            scara = input("Dati noua scara: ")
            alteIndicatii = input("Dati noile indicatii: ")

            self.__locatieService.modifica(
                idLocatie, numeStrada, numar, bloc, scara, alteIndicatii)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllLocatie(self):
        for locatie in self.__locatieService.getAll():
            print(locatie)

    def runCRUDComenziMenu(self):
        while True:
            print("1. Adauga comanda")
            print("2. Sterge comanda")
            print("3. Modifica comanda")
            print("a. Afiseaza toate comenzile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaComanda()
            elif optiune == "2":
                self.uiStergeComanda()
            elif optiune == "3":
                self.uiModificaComanda()
            elif optiune == "a":
                self.showAllComenzi()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaComanda(self):
        try:
            idComanda = input("Dati id-ul comenzii: ")
            idMasina = input("Dati id-ul masinii: ")
            idLocatie = input("Dati id-ul locatiei: ")
            timpFinal = float(input("Dati timpul final: "))
            costPerKm = float(input("Dati costul/km: "))
            distantaParcursa = float(input("Dati distanta parcursa: "))
            status = input("Dati statusul: ")

            self.__comandaService.adauga(
                idComanda,
                idMasina,
                idLocatie,
                timpFinal,
                costPerKm,
                distantaParcursa,
                status)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeComanda(self):
        try:
            idComanda = input("Dati id-ul comenzii de sters: ")

            self.__comandaService.sterge(idComanda)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaComanda(self):
        try:
            idComanda = input("Dati id-ul comenzii de modificat: ")
            idMasina = input("Dati noul id al masinii: ")
            idLocatie = input("Dati noul id al locatiei: ")
            timpFinal = float(input("Dati noul timp final: "))
            costPerKm = float(input("Dati noul cost/km: "))
            distantaParcursa = float(input("Dati noua distanta parcursa: "))
            status = input("Dati noul status: ")

            self.__comandaService.modifica(
                idComanda,
                idMasina,
                idLocatie,
                timpFinal,
                costPerKm,
                distantaParcursa,
                status)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllComenzi(self):
        for comanda in self.__comandaService.getAll():
            print(comanda)
