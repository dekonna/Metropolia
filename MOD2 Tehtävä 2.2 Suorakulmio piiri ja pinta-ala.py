#käyttäjä syöte
kanta = float(input("Anna suorakulmaisen kolmion kanta: "))
korkeus = float(input("Anna suorakulmaisen kolmion korkeus: "))

#laskuri pinta-ala
pinta_ala = (kanta * korkeus) / 2
print(f"Suorakulmion pinta_ala on: {pinta_ala}")

#laskuri piiri
piiri = (kanta * 2 + korkeus * 2)
print(f"Suorakulmion piiri on: {piiri}")