from dataclasses import dataclass

from Domain.comanda import Comanda
from Domain.locatie import Locatie

@dataclass
class LocatieComandaViewModel:
    locatie: Locatie
    comanda: Comanda

    def __str__(self):
        return f'{self.locatie} \n\tcu comanda {self.comanda}'
