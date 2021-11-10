from dataclasses import dataclass


@dataclass
class Masina:
    '''
    descrie o masina
    '''
    idMasina: str
    indicativ: str
    nivelConfort: str
    plataCard: str
    model: str