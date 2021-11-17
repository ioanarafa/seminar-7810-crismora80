from dataclasses import dataclass

from Domain.masina import Masina


@dataclass
class MasinaCostMediuViewModel:
    masina: Masina
    costMediu: float

    def __str__(self):
        return f'{self.masina} are costul mediu per km {self.costMediu}'
