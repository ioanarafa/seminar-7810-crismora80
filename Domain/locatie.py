from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Locatie(Entitate):
    numeStrada: str
    numar: int
    bloc: str
    scara: str
    alteIndicatii: str
