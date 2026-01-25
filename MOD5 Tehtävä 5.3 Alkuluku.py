# kysytään käyttäjältä luku integer muodossa eli kokonaislukunu
luku = int(input("Anna luku: "))

# alustetaan muuttuja on_alkuluku, joka pitää kirjaa alkuluvuista
on_alkuluku = True

# 1 ei ole alkuluku eli alkuluvut ovat suurempia kuin 2 (2 on ainut parillinen alkuluku ja myös pienin)
if luku < 2:
    on_alkuluku = False
else:
    # testataan käyttäjän syöttämän luvun jaollisuus alkaen luvusta 2 -> käyttäjän syöttämään lukuun asti.
    for jakaja in range(2, luku):
        # testaa jakojäännöksen, jos jakojäännös on 0 on luku jaollinen eli se ei ole alkuluku.
        # esim luku 9 : 3 = 0 = ei ole alkuluku
        if luku % jakaja == 0:
            # break heti jos luku on jaettavissa tasan eli ei ole alkuluku (ei käydä turhaan läpi kaikkia lukuja)
            on_alkuluku = False
            break

# tulosteet 
if on_alkuluku:
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")