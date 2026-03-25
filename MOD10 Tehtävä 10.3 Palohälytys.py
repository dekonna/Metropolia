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
    # liikuttaa hissin kohdekerrokseen kerros kerrallaan
    def siirry_kerrokseen(self, kohde):
        while self.nykyinen < kohde:
            self.kerros_ylos()
        while self.nykyinen > kohde:
            self.kerros_alas()


class Talo:

    def __init__(self, alin, ylin, hissien_lkm):
        self.alin = alin
        self.ylin = ylin
        self.hissit = [] # tyhjä lista hissiolioille
        # luodaan hissioliot
        for i in range(hissien_lkm): #
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohdekerros):
        print(f"\nAjetaan hissiä {hissin_numero} kerrokseen {kohdekerros}")
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("\nPalohälytys! Kaikki hissit siirtyvät alimpaan kerrokseen.")
        for hissi in self.hissit: # käydään kaikki hissit läpi ja siirretään ne alimpaan kerrokseen
            hissi.siirry_kerrokseen(self.alin)

# luodaan talo
talo = Talo(1, 10, 3)

# liikutellaan hissejä
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 8)
talo.aja_hissia(3, 6)
# palohälytys -> kaikki hissit alas
talo.palohalytys()