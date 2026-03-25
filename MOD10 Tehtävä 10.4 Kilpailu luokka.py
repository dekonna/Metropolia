import random

class Auto: # auton perustiedot
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos # muutetaan auton nopeutta annetun arvon verran
        if self.nopeus < 0: # varmistetaan ettei nopeus mene negatiiviseksi
            self.nopeus = 0
        if self.nopeus > self.huippunopeus: # varmistetaan ettei nopeus ylitä huippunopeutta
            self.nopeus = self.huippunopeus

    def kulje(self, tuntia): # kasvattaa kuljettua matkaa
        self.kuljettu_matka += self.nopeus * tuntia


class Kilpailu: # alustetaan kilpailun tiedot
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus # kilpailun kokonaispituus kilometreinä
        self.autot = autot # lista autoolioista

    def tunti_kuluu(self):
        for auto in self.autot:
            muutos = random.randint(-10, 15) # satunnainen nopeuden muutos
            auto.kiihdyta(muutos) # muuttaa auton nopeutta
            auto.kulje(1) # auto kulkee yhden tunnin ajan

    def tulosta_tilanne(self):
        print("\nTilanne:") # tuloste tilanteesta
        print("Rekisteri | Nopeus | Matka")
        for auto in self.autot: # tulostaa jokaisen auton tiedot
            print(f"{auto.rekisteritunnus:10} {auto.nopeus:7} km/h {auto.kuljettu_matka:7.1f} km")

    def kilpailu_ohi(self): # tarkistetaan onko jokin auto saavuttanut maalin
        for auto in self.autot:
            if auto.kuljettu_matka >= self.pituus:
                return True
        return False

# luodaan autot
autot = []
for i in range(10):
    rekisteri = f"ABC-{i+1}" # luodaan rekisteritunnus
    huippunopeus = random.randint(100, 200) # satunnainen huippunopeus
    autot.append(Auto(rekisteri, huippunopeus)) # lisätään uusi auto listaan

# luodaan kilpailu
kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunnit = 0 # kulunut aika tunteina

# simuloidaan kilpailua
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu() # yksi tunti kuluu kilpailussa
    tunnit += 1 # kasvatetaan tuntien määrää

    # tulostus 10 tunnin välein
    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()

# lopputilanne
print("\n🏁 Kilpailu päättyi!")
kilpailu.tulosta_tilanne()