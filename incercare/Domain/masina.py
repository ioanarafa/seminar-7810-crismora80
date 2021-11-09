from dataclasses import dataclass


@dataclass
class Masina:
    '''
    descrie entitatea masina
    '''
    idMasina: str
    indicativ: str
    nivelConfort: str
    plataCard: str
    model: str
