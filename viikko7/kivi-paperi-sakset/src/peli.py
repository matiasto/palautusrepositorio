from kps import KPS


class Peli(KPS):
    def __init__(self, tyyppi, kone = False) -> None:
        super().__init__()
        self.tyyppi = tyyppi
        self.kone = kone

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tyyppi.anna_siirto()
        if self.kone:
            print(f"Tietokone valitsi: {tokan_siirto}")
        self.tyyppi.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto