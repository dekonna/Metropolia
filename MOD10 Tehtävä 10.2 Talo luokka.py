class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.nykyinen = alin

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
            print(f"Hissi meni kerrokseen {self.nykyinen}")

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
            print(f"Hissi meni kerrokseen {self.nykyinen}")

    def siirry_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.kerros_ylos()
        while self.nykyinen > kohde:
            self.kerros_alas()


class Talo:
    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [] # lista johon hissit tallennetaan

        # luodaan hissit: pyörii hissien_lkm kertaa ja luo jokaisella kierroksella uuden hissi olion ja lisää sen listaan self.hissit
        for i in range(hissien_lkm):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohdekerros): # valitsee hissin ja ajaa sen tiettyyn kerrokseen
        print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
        hissi = self.hissit[hissin_numero - 1] # -1 koska lista indeksit alkaa 0
        hissi.siirry_kerrokseen(kohdekerros) # kutsutaan hissiolion metodia siirry_kerrokseen

# luodaan talo jossa kerrokset 1–10 ja 3 hissiä
talo = Talo(1, 10, 3)

# ajetaan eri hissejä
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 3)

# palautetaan hissi 1 takaisin alimpaan kerrokseen
talo.aja_hissia(1, 1)