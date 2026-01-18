print("1. LUX")
print("2. A-luokka")
print("3. B-luokka")
print("4. C-luokka")
Hytti = int(input("Anna hyttiluokka (1-4): "))

if Hytti == 1:
    print("LUX on parvekkeellinen hytti yläkannella.")

elif Hytti == 2:
    print("A on ikkunallinen hytti autokannen yläpuolella.")

elif Hytti == 3:
    print("B on ikkunaton hytti autokannen yläpuolella.")

elif Hytti == 4:
    print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Annoit jotain muuta kuin vaihtoehdot 1-4")

