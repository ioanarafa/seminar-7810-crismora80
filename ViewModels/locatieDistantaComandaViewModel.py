from Domain.locatie import Locatie
from dataclasses import dataclass


@dataclass
class LocatieDistantaComandaViewModel:
    locatie: Locatie
    distanta: float

    def __str__(self):
        return f'{self.locatie} are suma distantelor comenzilor ' \
               f'{self.distanta}'
