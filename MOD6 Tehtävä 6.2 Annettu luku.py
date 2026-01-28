import random

# funktio
# määritellään funktio, joka saa tiedon tahkojen määrästä ja palauttaa satunnaisluvun väliltä 1 - tahkot
def funktio_1(tahkot):
    return random.randint(1, tahkot)

tahkojen_maara = int(input("Tahkojen maara: "))

laskuri = 0

# pääohjelma

while True:
    laskuri = laskuri +1
    tulos = funktio_1(tahkojen_maara)
    print(f"Heitit: {tulos}")

    if tulos == tahkojen_maara:
        print(f"Sait maksimiluvun {tulos}")
        print(f"Heittojen määrä", laskuri)
        break