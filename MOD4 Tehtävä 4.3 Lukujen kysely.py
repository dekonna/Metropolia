# asetetaan muuttujien arvoksi None pitämään paikkaa luvuille.
pienin_luku = None
suurin_luku = None

# while silmukka lukujen kysymiseen.
while True:
    anna_luku = input("Anna luku (enter näyttää pienimmän ja suurimman luvun): ")

    # jos käyttäjä ei syötä mitään silmukka loppuu.
    if anna_luku == "":
        # hypätään riville 27 ja tulostetaan tulokset tai viesti.
        break

    # tyypin muunnos koska input() on merkkijono, palauttaa str sijaan -> float
    luku = float(anna_luku)

    # jos muuttujan pienen_luku arvo on vielä None tai uusi luku on pienempi kuin nykyinen pienin_luku, päivitetään pienin_luku.
    if pienin_luku is None or luku < pienin_luku:
        pienin_luku = luku

    # jos muuttujan suurin_luku arvo on vielä None tai uusi luku on suurempi kuin nykyinen suurin_luku, päivitetään suurin_luku.
    if suurin_luku is None or luku > suurin_luku:
        suurin_luku = luku

# tuloste
if pienin_luku is not None:
    print("Pienin luku:", pienin_luku)
    print("Suurin luku:", suurin_luku)
# tuloste
else:
    print("Et syöttänyt yhtään lukua.")

