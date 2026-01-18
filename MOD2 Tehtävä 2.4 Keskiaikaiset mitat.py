import math

#käyttäjän syöte.
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luoti: "))

#laskuri luodit yhteensä.
kokonaisluodit = (leiviska * 20 * 32) + (naula * 20) + luoti

#muunnos grammoiksi.
yhteisgrammat = kokonaisluodit * 13.3

#muunnokset kiloiksi ja grammoiksi. Käytetään jakojäännöstä % grammojen ilmoittamiseen.
kilogrammat = int(yhteisgrammat / 1000)
grammat = int(yhteisgrammat % 1000)

# Tuloste.
# Käytetään taas f stringiä muuttujien upottamiseen.
# sekä käytetään myös :.2f toimintoa antamaan grammoille 2 desimaalia.
print(f"Massa nykymittojen mukaan on: {kilogrammat} kilogrammaa ja {grammat:.2f} grammaa")

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.