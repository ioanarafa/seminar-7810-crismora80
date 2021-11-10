from dataclasses import dataclass


@dataclass
class Comanda:
    idComanda: str
    idMasina: str
    idLocatie: str
    timpFinal: float
    costPerKm: float
    distantaParcursa: float
    status: str
