import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus): # tallentaa tiedot olion muuttujiksi (self)
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tamanhetkinen_nopeus = 0 # nollataan aina uudelle autolle
        self.kuljettu_matka = 0 # nollataan aina uudelle autolle

    def kiihdyta(self, nopeuden_muutos):
        uusi_nopeus = self.tamanhetkinen_nopeus + nopeuden_muutos # laskee uuden nopeuden
        # tarkistaa rajoitukset
        if uusi_nopeus > self.huippunopeus:
            self.tamanhetkinen_nopeus = self.huippunopeus
        elif uusi_nopeus < 0:
            self.tamanhetkinen_nopeus = 0
        else:
            self.tamanhetkinen_nopeus = uusi_nopeus

    def kulje(self, tuntimaara):
        self.kuljettu_matka += self.tamanhetkinen_nopeus * tuntimaara # lisätään matkaan nopeus * aika

# pääohjelma
# luodaan 10 autoa listaan
autot = []
for i in range(1, 11):
    huippu = random.randint(100, 200)
    uusi_auto = Auto(f"ABC-{i}", huippu) # luodaan olio
    autot.append(uusi_auto) # ja lisätään listaan

# silmukka
kilpailu_kaynnissa = True
while kilpailu_kaynnissa:
    for auto in autot: # käy listan autot löpi
        # nopeuden muutos
        muutos = random.randint(-10, 15) # arvotaan nopeudet
        auto.kiihdyta(muutos) # metodi kutsu

        # auto kulkee tunnin
        auto.kulje(1)

        # tarkistus onko joku auto ylittänyt 10000 rajan
        if auto.kuljettu_matka >= 10000:
            kilpailu_kaynnissa = False # kisa loppuu jos on

# tulosten tulostus taulukkona, <10 ja 8.1f = tekstin tasaus ja desimaalien määrä
# <10 = 10 merkkiä tilaa vasemmalle tasattuna
# >8.1f = 8 merkkiä leveä tila, 1 desimaali, oikealle tasattu liukuluku
print(f"{'Rekisteri':<10} | {'Huippu':<10} | {'Nopeus':<10} | {'Matka':<10}")
print("-" * 50)
for auto in autot:
    print(
        f"{auto.rekisteritunnus:<10} | {auto.huippunopeus:>3} km/h  | {auto.tamanhetkinen_nopeus:>3} km/h  | {auto.kuljettu_matka:>8.1f} km")