from dataclasses import dataclass
from typing import List

from Domain.comanda import Comanda
from Domain.locatie import Locatie


@dataclass
class LocatieComenziViewModel:
    locatie: Locatie
    comenzi: List[Comanda]

    def __str__(self):
        return f'{self.locatie} cu comenzile:\n\t' \
               f'{[comanda for comanda in self.comenzi]}'
