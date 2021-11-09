from Service.masinaService import MasinaService


class Consola:
    def __init__(self, masinaService: MasinaService):
        self.__masinaService = masinaService

    def runMenu(self):
        while True:
            print("1. CRUD masini")
            print("x. Iesire")
            optiune = input("Dati optiunea")
            if optiune == "1":
                self.run_crud_masini()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida!")

    def run_crud_masini(self):
        while True:
            print("1. Adaugare masina")
            print("2. Stergere masina")
            print("3. Modificare masina")
            print("a. Afiseaza toate masinile")
            print("x. Inapoi")
            optiune = input("Dati optiunea")
            if optiune == "1":
                self.ui_adaugare_masina()
            elif optiune == "2":
                self.ui_stergere_masina()
            elif optiune == "3":
                self.ui_modificare_masina()
            elif optiune == "a":
                self.ui_afisare_masini()
            elif optiune == "x":
                break
            else:
                print("Optiune invalida")

    def ui_adaugare_masina(self):
        try:
            id_masina = input("Dati id-ul masinii")
            indicativ = int(input(
                "Dati indicativul masinii"))
            nivel_confort = input(
                "Dati nivelul de confort al masinii "
                "(standard, ridicat, premium)")
            plata_card = input(
                "Mentionati daca plata se face cu cardul (da, nu)")
            model = input("Dati modelul masinii")

            self.__masinaService.adauga(
                id_masina, indicativ, nivel_confort, plata_card, model)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_stergere_masina(self):
        try:
            id_masina = input("Dati id-ul masinii de sters")

            self.__masinaService.sterge(id_masina)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_modificare_masina(self):
        try:
            id_masina = input("Dati id-ul masinii de modificat")
            indicativ = int(input("Dati noul indicativ al masinii"
                                  " sau 0 pt. a nu il modifica"))
            nivel_confort = input(
                "Dati nou; nivelul de confort al masinii"
                " (standard, ridicat, premium) sau stirng gol "
                "pt. a nu il modifica")
            plata_card = input("Mentionati daca plata se face cu cardul"
                               " (da, nu) sau stirng gol "
                               "pt. a nu il modifica")
            model = input("Dati noul model masinii "
                          "sau stirng gol pt. a nu il modifica")

            self.__masinaService.modifica(
                id_masina, indicativ, nivel_confort, plata_card, model)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def ui_afisare_masini(self):
        masini = self.__masinaService.getAll()
        for masina in masini:
            print(masina)
