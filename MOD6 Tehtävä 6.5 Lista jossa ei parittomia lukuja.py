# funktio: tarkistetaan ehto parillisille luvuille ja lisätään tulokset parilliset listaan.
def parilliset_luvut(lista):
    parilliset = []

    for luku in lista:
        if luku % 2 == 0:  # ehto
            parilliset.append(luku)  # lisää listaan
    # palautus pääohjelmalle
    return parilliset

# pääohjelma
alkuperainen_lista = [1,2,3,4,5,6,7,8]

# kutsutaan funktiota ja tallennetaan tulos muuttujaan karsittu_lista
karsittu_lista = parilliset_luvut(alkuperainen_lista)

# tulosteet
print(f"Alkuperäinen lista: {alkuperainen_lista}")
print(f"Vain parilliset:    {karsittu_lista}")