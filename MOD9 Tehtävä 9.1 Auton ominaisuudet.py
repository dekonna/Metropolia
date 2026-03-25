class Auto:

    # alustaja (konstruktori) -> suoritetaan automaattisesti kun uusi olio luodaan
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

# olio auto1
auto1 = Auto("ABC-123", 142)

print("Rekisteritunnus: ", auto1.rekisteritunnus)
print("Huippunopeus: ", auto1.huippunopeus, "km/h")
print("Tämänhetkinen nopeus:", auto1.nopeus, "km/h")
print("Kuljettu matka:", auto1.kuljettu_matka, "km")

# Auto luokkaa kutsutaan -> luodaan uusi olio
# __init__ suoritetaan automaattisesti ja asettaa olion arvot
