# luodaan lista tallennettaville luvuille
luvut = []

# aloitetaan ikuinen silmukka
while True:
    # ohjelma pysähtyy ja jää odottamaan käyttäjän syötettä
    anna_luku = input("Anna luku (pelkkä enter lopettaa ohjelman): ")

    # tarkistetaan mitä syöte on, jos syöte on tyhjä, silmukka lopetetaan ja hypätään riville 20 eli seuraavaan koodilohkoon
    # eli jos anna_luku == on totta eli tyhjä -> break -> rivi 20
    if anna_luku == "":
        break
    # muutetaan syöte kokonaisluvuksi (luku = (int)kokonaisluku anna_luvussa) ja lisätään listaan .append metodilla
    # input() luetaan merkkijonona, joten se täytyy muuttaa, jotta luvulla voidaan tehdä matemaattisia asioita
    luku = int(anna_luku)
    luvut.append(luku)

# lajitellaan lista suurimmasta pienimpään
# reverse=True kääntää järjestyksen. Pelkkä sort järjestäisi luvat pienimmästä suurimpaan
luvut.sort(reverse=True)
print("Viisi suurinta lukua: ")

# leikkaa listasta 5 indeksiä/alkiota 0,1,2,3,4 ja tulostaa ne
for numerot in luvut[0:5]:
    print(numerot)


