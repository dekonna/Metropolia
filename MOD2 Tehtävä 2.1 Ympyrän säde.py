import math
#Kysytään käyttäjältä säteen pituus.
sade = float(input("Anna ympyrän säde: "))
#Python laskee pinta-alan. Pii kertaa säde potenssiin 2 = A. Laskutoimitus on tallennettu muuttujaan pinta_ala.
pinta_ala = math.pi * (sade ** 2)
#Tulostetaan vastaus. Käytetään f stringiä yhdistämään teksti + muuttuja pinta_ala.
#f stringin avulla kerrotaan pythonille että tämä merkkijono sisältää myös muuttujan/muuttujia.
print(f"Ympyrän pinta-ala on: {pinta_ala}")