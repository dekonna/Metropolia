class Julkaisu: # luokka
    def __init__(self, nimi): #alustus (constructor). Self luo olion ja nimi on arvo joka annetaan esim aku ankka
        self.nimi = nimi # tallentaa nimen olion sisälle

class Kirja(Julkaisu): # kirja luokka perii yliluokan julkaisu ominaisuudet
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi) # kutsuu yliluokan alustajaa
        self.kirjoittaja = kirjoittaja # tallennetaan kirjan tiedot
        self.sivumaara = sivumaara

    def tulosta_tiedot(self): # kirja luokan metodi
        print("Julkaisun nimi:", self.nimi)
        print("Kirjoittaja:", self.kirjoittaja)
        print("Sivumäärä:", self.sivumaara)

class Lehti(Julkaisu): # luokka joka perii "julkaisu"
    def __init__(self, nimi, paatoimittaja): # lehdellä on nimi (peritty) ja päätoimittaja
        super().__init__(nimi) # asettaa nimen yliluokan kautta
        self.paatoimittaja = paatoimittaja # tallentaa päätoimittajan

    def tulosta_tiedot(self):
        print("Julkaisun nimi:", self.nimi)
        print("Päätoimittaja:", self.paatoimittaja) # tulostaa lehden tiedot
# pääohjelma
lehti = Lehti("Aku Ankka", "Aki Hyyppä") # luo olion lehti luokasta -> kutsuu init ja tallentaa arvot
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200) # luo kirja olion

lehti.tulosta_tiedot() # kutsuu metodia -> tulostaa tiedot
print()
kirja.tulosta_tiedot() # tulostaa kirjan tiedot

# notes:
# super() käyttää yliluokkaa
# .self = olio