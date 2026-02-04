# määritellään vuodenajat monikkoon aka tuplexiin (indeksit: 0,1,2,3)
vuoden_ajat = ("talvi", "kevät", "kesä", "syksy")

ksm = int(input("Anna kuukausi numerona (1-12): "))

# kuukaudet väliltä 1-12
if 1 <= ksm <= 12:
    # 12 % 12 jakojäännös = 0 eli talvi, "nollaus"
    # // 3 ryhmittelee luvut:
    # 0 % 3 = 0 (talvi)
    # 1 % 3 = 0
    # 2 % 3 = 0
    # 3 % 3 = 1 (kevät)
    # 4 % 3 = 1
    # 5 % 3 = 1
    # 6 % 3 = 2 (kesä) jne...
    jako = (ksm % 12) // 3
    print(f"{ksm}. kuukausi kuuluu vuodenaikaan: {vuoden_ajat[jako]}")

