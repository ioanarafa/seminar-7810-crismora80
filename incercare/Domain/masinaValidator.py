class MasinaValidator:
    def valideaza(self, masina):
        '''

        :param masina:
        :return:
        '''
        erori = []
        if masina.nivelConfort not in ['standard', 'ridicat', 'remium']:
            erori.append(
                "Nivelul de confort nu este unul dintre: "
                "'standard', 'ridicat', 'premium'"
            )
        if masina.plataCard not in ["da", "nu"]:
            erori.append(
                "Plata cu cardul trebuie sa aiba valorile "
                "'da' sau 'nu'"
            )
        if len(erori) > 0:
            raise ValueError(erori)
