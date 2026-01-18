import math

#käyttäjän syöte
kokonaisluku1 = int(input("Anna kokonaisluku: "))
kokonaisluku2 = int(input("Anna toinen kokonaisluku: "))
kokonaisluku3 = int(input("Anna kolmas kokonaisluku: "))

#laskurit
summa = kokonaisluku1 + kokonaisluku2 + kokonaisluku3
tulo = kokonaisluku1 * kokonaisluku2 * kokonaisluku3
keskiarvo = summa / 3

#tuloste
print("TULOKSET:")
print(f"Summa = {summa}")
print(f"Tulo = {tulo}")
print(f"keskiarvo = {keskiarvo}")