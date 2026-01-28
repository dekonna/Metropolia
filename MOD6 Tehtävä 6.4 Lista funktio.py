# funktio
def kirjuri(lista):
    summa = 0
    for luku in lista:
        summa = summa + luku
    return summa


# pääohjelma
lista = [1,2,3,4,5,]
tulos = kirjuri(lista)
print(f"Listan lukujen summa on: {tulos}")
