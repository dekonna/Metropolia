class Auto:

    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):  # kasvattaa tai pienentää nopeutta ja pitää sen välillä 0 - huippunopeus
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        # lasketaan kuljettu matka
        lisatty_matka = self.tamanhetkinen_nopeus * tuntimaara
        # lisätään kuljettuun matkaan uusi matka
        self.kuljettu_matka += lisatty_matka

auto = Auto("ABC-123", 142)
auto.kuljettu_matka = 2000
auto.kiihdyta(60) # metodi kutsu
auto.kulje(1.5)
print(f"Uusi kuljettu matka: {auto.kuljettu_matka} km")