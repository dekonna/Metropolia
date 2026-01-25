# määritellään oikeat tunnukset
oikea_tunnus = "python"
oikea_salasana = "rules"

# alustetaan laskuri ja muuttujat, jotta silmukka voi alkaa
yritykset = 0
tunnus = ""
salasana = ""

# Silmukka jatkuu niin kauan kuin tunnukset ovat väärin JA yrityksiä on alle 5
while (tunnus != oikea_tunnus or salasana != oikea_salasana) and yritykset < 5:
    tunnus = input("Käyttäjätunnus: ")
    salasana = input("Salasana: ")

    # lisätään yritykset laskuriin +1 joka silmukan jälkeen aka muistiin. ts. estetään ikuinen silmukka.
    yritykset = yritykset + 1

    # jos tiedot olivat väärin ja yrityksiä on vielä jäljellä, voidaan antaa palaute
    # jos tunnus ei ole oikea_tunnus tai salasana ei ole oikea_salasana ja yritykset on pienempi kuin 5
    # tulostetaan "väärä tunnus tai....."
    if (tunnus != oikea_tunnus or salasana != oikea_salasana) and yritykset < 5:
        print("Väärä tunnus tai salasana. Yritä uudelleen.")

# Tarkistetaan silmukan päättymisen jälkeen, kumpi ehto täyttyi
# jos tunnus on sama kuin oikea_tunnus JA salasana on sama kuin oikea_salasana tulostetaan "tervetuloa"
if tunnus == oikea_tunnus and salasana == oikea_salasana:
    print("Tervetuloa")
    # jos ei tulostetaan "pääsy evätty"
else:
    print("Pääsy evätty")