yksi_tuuma = 2.54
tuumat = float(input("Anna tuumat: "))

while tuumat >= 0:
    print("Tuumat senttimetreissä: ", tuumat * yksi_tuuma)
    tuumat = float(input("Anna tuumat: "))

print("Negatiivinen luku lopettaa ohjelman")

