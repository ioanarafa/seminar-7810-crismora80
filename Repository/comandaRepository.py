from Domain.comanda import Comanda


class ComandaRepository:
    def __init__(self):
        self.comenzi = {}

    def read(self, idComanda=None):
        if idComanda is None:
            return list(self.comenzi.values())

        if idComanda in self.comenzi:
            return self.comenzi[idComanda]
        else:
            return None

    def adauga(self, comanda: Comanda):
        if self.read(comanda.idComanda) is not None:
            raise KeyError("Exista deja o comanda cu id-ul dat!")
        self.comenzi[comanda.idComanda] = comanda

    def sterge(self, idComanda: str):
        if self.read(idComanda) is None:
            raise KeyError("Nu exista nicio comanda cu id-ul dat!")
        del self.comenzi[idComanda]

    def modifica(self, comanda: Comanda):
        if self.read(comanda.idComanda) is None:
            raise KeyError("Nu exista nicio comanda cu id-ul dat!")
        self.comenzi[comanda.idComanda] = comanda
