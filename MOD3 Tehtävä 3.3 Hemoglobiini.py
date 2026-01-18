#kysely käyttäjältä jossa käytetään .lower() funktiota isojen ja pienten kirjainten takia joilla ei ole väliä.
Sukupuoli = str(input("Oletko mies vai nainen? ")).lower()

#nainen osio
if Sukupuoli == "nainen":
    Arvo = int(input("Anna hemoglobiiniarvo: "))
    if Arvo > 175:
        print("Hemoglobiini arvo on korkealla!")
    elif Arvo < 117:
        print("Hemoglobiini arvo on matalalla!")
    else:
        print("Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.")

#miehen osio
if Sukupuoli == "mies":
    Arvo = int(input("Anna hemoglobiiniarvo: "))
    if Arvo > 195:
        print("Hemoglobiini arvo on korkealla!")
    elif Arvo < 134:
        print("Hemoglobiini arvo on matalalla!")
    else:
        print("Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.")
#jos käyttäjä syöttää jotain muuta kuin mies tai nainen
else:
    print("kirjoitit jotain muuta kuin mies tai nainen")







