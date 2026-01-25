# luodaan lista kaupungit mihin tallennetaan kaupungit aka säiliö
kaupungit = []

# for looppi jonka avulla kysytään kaupunkia 5 kertaa
# range(5) varmistaa että kysymys esitetään käyttäjälle vain 5 kertaa
# lopettaa silmukan suorituksen heti viidennen syötteen jälkeen
for laskuri in range(5):
    nimi = input(f"Anna {laskuri + 1}. Kaupungin nimi: ")
    # tallentaa syötetyn kaupungin nimen listaan (tai mitä ikinä käyttäjä kirjoittaakaan)
    kaupungit.append(nimi)

# kosmeettinen merkintä tulosteessa joka jakaa "-" merkeillä syötetyt kaupungit ja vastaukset
print("-" * 20)
# tuloste
print("Syöttämäsi kaupungit:")

# for looppi listan läpikäymiseen alkio kerrallaan.
for kaupunki in kaupungit:
    print(kaupunki)