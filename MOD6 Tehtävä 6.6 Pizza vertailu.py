# funktio saa pizzan ympyrän halkaisijan senttimetreinä ja hinnan euroina
# funktio laskee ja palauttaa pizzan yksikköhinnan neliömetreinä
# pääohjelma kysyy käyttäjältä kahden pizzan halkaisijan ja hinnan
# ja ilmoittaa kumpi on hinta/koko suhteeltaan parempi eli kummalla on alhaisempi yksikköhinta
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

#funktio joka laskee säteen, pinta-alan ja palauttaa yksikköhinnan.
def laske_sade_ja_pintaala(halkaisija, hinta):
    # Säde metreinä:
    # halkaisija / 2 = säde (cm)
    # säde (cm) / 100 = säde (m)
    # kerrottuna: halkaisija / 200
    sade = halkaisija / 200
    #laskee ympyrän pinta-alan neliömetreinä π * r²
    pinta_ala = math.pi * sade**2
    #palauttaa yksikköhinna
    return hinta / pinta_ala

#pääohjelma
ksm_halkaisija_pizza1 = float(input("Anna pizzan 1 halkaisija senttimetreissä: "))
ksm_hinta_pizza1 = float(input("Anna pizzan 1 hinta euroina: "))

ksm_halkaisija_pizza2 = float(input("Anna pizzan 2 halkaisija senttimetreissä: "))
ksm_hinta_pizza2 = float(input("Anna pizzan 2 hinta euroina: "))

#kutsutaan funktiota ja tallennetaan yksikköhinnat muuttujiin tulos_pizza1 ja tulos_pizza2
tulos_pizza1 = laske_sade_ja_pintaala(ksm_halkaisija_pizza1, ksm_hinta_pizza1)
tulos_pizza2 = laske_sade_ja_pintaala(ksm_halkaisija_pizza2, ksm_hinta_pizza2)

#vertailu ja tulostus
if tulos_pizza1 < tulos_pizza2:
    print(f"Pizza 1 on halvempi neliömetriä kohden. \nVertailu: \nPizza 1 {tulos_pizza1:.2f} €/m2 \nPizza 2 {tulos_pizza2:.2f} €/m2")
else:
    print(f"Pizza 2 on halvempi neliömetriä kohden. \nVertailu: \nPizza 1 {tulos_pizza1:.2f} €/m2 \nPizza 2 {tulos_pizza2:.2f} €/m2")




