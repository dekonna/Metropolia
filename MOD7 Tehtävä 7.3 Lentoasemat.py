# määritellään funktio ja luodaan sanakirja
def lentoasema_ohjelma():
    # sanakirja
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1 - Syötä uusi lentoasema")
        print("2 - Hae lentoaseman tiedot")
        print("3 - Lopeta")

        valinta = input("Valinta (1, 2 tai 3): ")


        if valinta == "1":
            icao = input("Syötä lentoaseman ICAO-koodi: ") # avain = icao
            nimi = input("Syötä lentoaseman nimi: ") # nimi = nimi
            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} ({icao}) tallennettu.")

        elif valinta == "2":
            icao = input("Syötä haettava ICAO-koodi: ")
            if icao in lentoasemat: # tarkistetaan onko avain jo sanakirjassa, jos on haetaan vastaava nimi
                print(f"ICAO-koodia {icao} vastaava lentoasema on {lentoasemat[icao]}.")
            else:
                print("Lentoasemaa ei löytynyt.")

        elif valinta == "3":
            print("Lopeta")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    lentoasema_ohjelma()


