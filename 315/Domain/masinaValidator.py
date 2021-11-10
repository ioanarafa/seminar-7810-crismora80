from Domain.masina import Masina


class MasinaValidator:
    def valideaza(self, masina: Masina):
        erori = []
        if masina.nivelConfort not in ["standard", "ridicat", "premium"]:
            erori.append("Nivelul de confort al masinii poate fi "
                         "'standard', 'ridicat' sau 'premium'")
        if masina.plataCard not in ["da", "nu"]:
            erori.append("Plata card poate fi 'da' sau 'nu'")
        if len(erori) > 0:
            raise ValueError(erori)
