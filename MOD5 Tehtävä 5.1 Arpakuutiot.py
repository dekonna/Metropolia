import random

# kysytään käyttäjältä heitto määrä
monta_arpakuutiota = int(input("monta arpakuutiota heitetään?: "))

# alustetaan summa muuttuja summan laskemista varten.
summa = 0

# toistetaan heitot eli silmukka niin monta kertaa kuin käyttäjä syötti arvoksi
for laskuri in range(monta_arpakuutiota):
    # arvotaan luku 1-6 väliltä
    heitto = random.randint(1, 6)

    # lisätään saatu luku muuttujaan eli summa + heitto = summa
    # nyt käytetty += on vain helpompi tapa tehdä sama asia kuin "summa + heitto = summa"
    # se ottaa muuttujan summa arvon ja lisää siihen muuttuja heitto arvon ja tallentaa sen muuttujaan summa.
    summa += heitto

# tuloste
print("Heitettyjen kuutioiden summa on: ", summa)
