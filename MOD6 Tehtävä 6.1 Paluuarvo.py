import random

#funktio jossa luvut arvotaan
def heita_noppaa():
    return random.randint(1, 6)

#pääohjelma
# luodaan ikuinen silmukka
while True:
    #tulostaa arvotun luvun niin kauan kunnes tulee 6
    tulos = heita_noppaa()
    print(tulos)

    #ehto = 6 ohjelma loppuu break komentoon kun saadaan random.randint avulla tulokseksi 6
    if tulos == 6:
        print("Tulos = 6 ohjelma lopetetaan")
        #katkaistaan silmukka
        break