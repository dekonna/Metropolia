
# funktio laskee gallonoiden tilavuuden litroina ja palauttaa tulon
def litrat_gallonat(gallonat):
    litrat = gallonat * 3.785
    return litrat

# pääohjelma
while True:
    syote = float(input("Anna gallonat: "))

    # ohjelman lopetus
    if syote < 0:
        print("Lopetit ohjelman")
        break

    # kutsutaan funktiota
    tulos = litrat_gallonat(syote)
    print(f"{syote} gallonaa on: {tulos:.2f} litraa.")


