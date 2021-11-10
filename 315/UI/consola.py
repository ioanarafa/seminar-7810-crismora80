from Service.masinaService import MasinaService


class Consola:
    def __init__(self, masinaService: MasinaService):
        self.__masinaService = masinaService

    def runMenu(self):
        while True:
            print("1. CRUD masini")
            print("2. CRUD locatii")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDMasiniMenu()
            elif optiune == "2":
                self.runCRUDLocatiiMenu()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati")


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
                print("Optiune gresita! Reincercati")

    def runCRUDLocatiiMenu(self):
        pass

    def uiAdaugaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii: ")
            indicativ = input("Dati indicativul masinii: ")
            nivelConfort = input("Dati nivelul de confort [standard, ridicat, premium]: ")
            plataCard = input("Dati plata card [da/nu]: ")
            model = input("Dati modelul masinii: ")

            self.__masinaService.adauga(idMasina, indicativ, nivelConfort, plataCard, model)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def uiStergeMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de sters: ")

            self.__masinaService.sterge(idMasina)
        except KeyError as e:
            print(e)

    def uiModificaMasina(self):
        try:
            idMasina = input("Dati id-ul masinii de modificat: ")
            indicativ = input("Dati noul indicativ al masinii: ")
            nivelConfort = input("Dati noul nivel de confort [standard, ridicat, premium]: ")
            plataCard = input("Dati noua plata card [da/nu]: ")
            model = input("Dati noul model masinii: ")

            self.__masinaService.modifica(idMasina, indicativ, nivelConfort, plataCard, model)
        except KeyError as e:
            print(e)
        except ValueError as e:
            print(e)

    def showAllMasini(self):
        for masina in self.__masinaService.getAll():
            print(masina)