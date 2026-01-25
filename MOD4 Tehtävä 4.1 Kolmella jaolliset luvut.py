#asetetaan muuttujaan arvo 1
luvut = 1

#while silmukka pyörii niin kauan kunnes luku on enintään 1000
while luvut <= 1000:
    #tarkistetaan onko luku jaollinen kolmella
    if luvut % 3 == 0:
        #tulostetaan kolmella jaolliset luvut
        print(luvut)
    #muuttujan arvoa kasvatetaan yhdellä, jotta silmukka etenee.
    luvut += 1

#toimisi myös
#luku = 3

#while luku <= 1000:
    #print(luku)
    #luku += 3