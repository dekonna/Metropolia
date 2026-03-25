class Hissi: # luokka jonka sisällä metodit __init__, kerros_ylos, kerros_alas, siirry_kerrokseen

    def __init__(self, alin, ylin): # alustus: tallentaa hissin ylin/alin ja nykyinen kerros
        self.alin = alin # alin sallittu kerros 1
        self.ylin = ylin # ylin sallittu kerros 10
        self.nykyinen = alin  # hissi aloittaa aina alimmasta kerroksesta

    def kerros_ylos(self): # metodi: siirtää hissiä 1 kerroksen ylemmäs
        if self.nykyinen < self.ylin: # hissi ei mene yli ylimmän kerroksen
            self.nykyinen += 1 # hissi yhden ylös
            print(f"Hissi nousi kerrokseen {self.nykyinen}") # tulostaa missä hissi on

    def kerros_alas(self): # metodi: vie hissin yhden kerroksen alas
        if self.nykyinen > self.alin: # hissi ei mene alimman kerroksen alle
            self.nykyinen -= 1 # hissi yhden alas
            print(f"Hissi laskeutui kerrokseen {self.nykyinen}") # tulostaa missä hissi on

    def siirry_kerrokseen(self, kohde): # metodi: ottaa vastaan kohdekerroksen
        print(f"Siirrytään kerrokseen {kohde}...") # mihin mennään

        while self.nykyinen < kohde: # jos kohteen alapuolella silmukka kutsuu kerros_ylos metodia
            self.kerros_ylos()

        while self.nykyinen > kohde: # jos kohteen yläpuolella silmukka kutsuu kerros_alas metodia
            self.kerros_alas()

        print(f"Hissi on nyt kerroksessa {self.nykyinen}")

if __name__ == "__main__":
    h = Hissi(1, 10) # kerrokset 1-10 (luokka Hissi jolla parametrit alin/ylin)

    h.siirry_kerrokseen(5) # siirtää hissin kerrokseen 5
    print()
    h.siirry_kerrokseen(1) # siirtää hissin kerrokseen 1