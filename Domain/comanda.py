from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Comanda(Entitate):
    idMasina: str
    idLocatie: str
    timpFinal: float
    costPerKm: float
    distantaParcursa: float
    status: str
