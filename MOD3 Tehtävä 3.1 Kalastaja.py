kalan_mitta = int(input("Minkä kokoinen kala (cm): "))
kalan_mitta_erotus = 37 - kalan_mitta

if kalan_mitta >= 37:
    print("Voit syödä kalan!")

else:
    print(f"Laita kala takaisin veteen! kala on {kalan_mitta_erotus}cm alamittainen")