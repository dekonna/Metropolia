# importataan random moduuli. Käytetään -> "random.randint(1, 10), jossa valittuna luvut 1-10".
import random

# ohjelma arpoo luvun suuruuden muuttujaan
oikea_luku = random.randint(1, 10)

# ohjelma antaa viestin käyttäjälle
print("Olen valinnut luvun väliltä 1-10.")

# asetetaan alkuarvaus, joka ei voi olla oikea luku esim. 0
# "alustetaan luku"
arvaus = 0

# jatketaan arvailua kunnes saadaan oikea luku "while arvaus != eli ei ole samansuuruinen = oikea_luku" joka määrittää oikean arvauksen.
while arvaus != oikea_luku:
    arvaus = int(input("Anna arvauksesi: "))

    # jos luku on pienempi kuin arvaus tulostetaan "liian pieni arvaus"
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    # jos arvaus on suurempi kuin oikea luku tulostetaa "liian suuri arvaus"
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    # muussa tapauksessa tulostetaan "Oikein!"
    else:
        print("Oikein!")


# Operator	Meaning	                    Example
# ==	    equal to	                x == y
# !=	    not equal to	            x != y
# >	        greater than	            x > y
# >=	    greater than or equal to	x >= y
# <	        less than	                x < y
# <=	    less than or equal to	    x <= y