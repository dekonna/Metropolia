# importataan random moduuli.
import random

# kysytään käyttäjältä pisteiden kokonaismäärä.
pisteiden_maara = int(input("Kuinka monta pistettä arvotaan? "))

# alustetaan laskuri ympyrän sisälle osuville pisteille.
osumat = 0

# arvotaan pisteitä pisteiden_maara kappaletta.
kerrat = 0
while kerrat < pisteiden_maara:
    # arvotaan x ja y koordinaatit väliltä [-1, 1].
    # random.uniform() arpoo myös desimaalilukuja toisin kuin random.randint, joka arpoo vain kokonaislukuja.
    # määrittää neliön rajat (leveys/korkeus välillä -1|1 vaaka/pysty)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # tarkistetaan pythagoraan lauseella onko pisteen etäisyys origosta eli 0.0 alle 1
    # yhtälö: x^2 + y^2 < 1, Jos x^2 + y^2 < 1, piste on ympyrän sisällä
    if x ** 2 + y ** 2 < 1:
        osumat = osumat + 1

    # kasvatetaan kierrosmäärää yhdellä joka silmukan lopussa
    kerrat = kerrat + 1

# lasketaan piin likiarvo kaavalla: pi = 4 * osumat / pisteiden_maara.
pii_likiarvo = 4 * osumat / pisteiden_maara

print("Piin likiarvo on:", pii_likiarvo)