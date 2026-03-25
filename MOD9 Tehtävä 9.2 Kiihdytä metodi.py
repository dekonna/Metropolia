class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, nopeuden_muutos):
        # uusi nopeus
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos

        # tarkistaa ettei ylitä huippunopeutta
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        # tarkistaa ettei nopeus laske alle 0
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

uusi_auto = Auto("ABC-123", 142)

uusi_auto.kiihdyta(30)
uusi_auto.kiihdyta(70)
uusi_auto.kiihdyta(50)

print(f"Auton nopeus kiihdytysten jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")
# jarrutus
uusi_auto.kiihdyta(-200)

print(f"Auton nopeus hätäjarrutuksen jälkeen: {uusi_auto.tamanhetkinen_nopeus} km/h")