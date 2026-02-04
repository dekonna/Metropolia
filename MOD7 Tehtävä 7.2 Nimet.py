# Määritellään funktio jolle luodaan toiminto joukko
# joukossa alkiot voivat olla missä tahansa järjestyksessä sekä siinä ei voi olla kahta samaa alkiota
def nimi_pankki():
    # nimet niminen joukko
    nimet = set()

    #käynnistetään silmukka ja kysytään nimeä
    while True:
        anna_nimi = input("Anna nimi: ")

        # lopettaa silmukan jos syöte on tyhjä
        if anna_nimi == "":
            break

        # jos nimi on jo listassa tulostetaan "aiemmin syötetty nimi"
        # ja kysytään uutta nimeä sekä lisätään uusi nimi joukkoon.
        if anna_nimi in nimet:
            print("Aiemmin syötetty nimi")
        else:
            print("Uusi nimi: ")
            # lisätään uusi nimi joukkoon
            nimet.add(anna_nimi)
    # tulostetaan kaikki syötetyt nimet nimet joukosta
    # (\n rivin vaihto)
    print("\nSyötetyt nimet:")
    # käydään läpi nimet joukossa
    for anna_nimi in nimet:
        print(anna_nimi)

# käynnistää ohjelman
if __name__ == "__main__":
    nimi_pankki()
