import math

vuosiluku = int(input("Anna vuosiluku: "))

if vuosiluku % 4 == 0:
    if vuosiluku % 100 == 0:
        if vuosiluku % 400 == 0:
            print("On karkausvuosi.")
        else:
            print("Ei ole karkausvuosi.")
    else:
        print("On karkausvuosi.")
else:
    print("Ei ole karkausvuosi.")