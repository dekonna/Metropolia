import random
# yliluokka
class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus < 0:
            self.nopeus = 0

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

    def kulje(self, tuntia):
        self.kuljettu_matka += self.nopeus * tuntia

# aliluokka 1
class Sahkoauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


# aliluokka 2
class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatankki):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatankki = bensatankki

# pääohjelma
# luodaan autot
sahkoauto = Sahkoauto("ABC-15", 180, 52.5)
polttis = Polttomoottoriauto("ACD-123", 165, 32.3)

# asetetaan nopeudet
sahkoauto.kiihdyta(100)
polttis.kiihdyta(120)

# ajetaan 3 tuntia
sahkoauto.kulje(3)
polttis.kulje(3)

# tulostetaan matkat
print("Sähköauto kulki:", sahkoauto.kuljettu_matka, "km")
print("Polttomoottoriauto kulki:", polttis.kuljettu_matka, "km")

# notes:
# aliluokat käyttävät yliluokan metodeja kulje ja kiihdytä