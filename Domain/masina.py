from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Masina(Entitate):
    indicativ: str
    nivelConfort: str
    plataCard: str
    model: str
