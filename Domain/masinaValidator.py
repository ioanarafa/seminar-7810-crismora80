from Domain.masina import Masina
from Domain.masinaError import MasinaError


class MasinaValidator:
    def valideaza(self, masina: Masina):
        erori = []
        if masina.nivelConfort not in ["standard", "ridicat", "premium"]:
            erori.append("Nivelul de confort trebuie sa fie "
                         "'standard', 'ridicat', 'premium'!")
        if masina.plataCard not in ['da', 'nu']:
            erori.append("Plata card poate fi 'da' sau 'nu!")
        if len(erori) > 0:
            raise MasinaError(erori)
