import mysql.connector
# tuodaan geopy kirjastosta työkalu geodesic joka laskee kahden koordinaattipisteen etäisyyden
from geopy.distance import geodesic

# funktio jolla syötteenä icao koodi ja kursori
def hae_koordinaatit(icao, kursori):
    # haetaan leveys ja pituusasteet icao koodin perusteella
    # eli valitaan taulusta airports rivit latitude_deg ja longitude_deg ja haetaan koordinaatit missä annetut
    # koodit täsmää
    sql = "SELECT latitude_deg, longitude_deg FROM airports WHERE ident = %s"
    # execute lähettää kyselyn tietokannalle
    kursori.execute(sql, (icao,))
    # palautetaan yksi rivi vastauksena (monikko jossa kaksi numeroa)
    return kursori.fetchone()

# testaus "try" -> jos tietokantaan ei saada yhteyttä hypätään except lohkoon
def laske_etaisyys():
    try:
        # avataan yhteys tietokantaan flight_game
        yhteys = mysql.connector.connect(
            # yhteyden muodostamisen asetukset
            host="localhost",
            user="root",
            password="Salasana1",
            database="flight_game"
        )
        # varmistetaan että tietokantaan on yhteys
        if yhteys.is_connected():
            # kursori jonka avulla tietokannassa liikutaan ja annetaan komentoja
            kursori = yhteys.cursor()

            #  kysytään käyttäjältä koodit ja muutetaan kirjaimet sekä välilyönnit
            alku_icao = input("Syötä lähtökentän ICAO-koodi (esim. EFHK): ").upper().strip()
            loppu_icao = input("Syötä kohdekentän ICAO-koodi (esim. EGLL): ").upper().strip()

            # kutsutaan funktiota ja jos koodit löytyy tallennetaan arvot muuttujiin
            alku_piste = hae_koordinaatit(alku_icao, kursori)
            loppu_piste = hae_koordinaatit(loppu_icao, kursori)

            #  tarkistetaan "and" että molemmat koodit löytyivät
            if alku_piste and loppu_piste:
                # annetaan koordinaatti parit geopylle ja pyydetään vastaus kilometreinä
                etaisyys = geodesic(alku_piste, loppu_piste).kilometers

                print(f"\n--- Etäisyys laskettu ---")
                # tulostetaan laskettu etäisyys ja pyöristetään desimaali
                print(f"Lentokenttien {alku_icao} ja {loppu_icao} välinen etäisyys on {etaisyys:.2f} km.")
            else:
                print("\n Virhe: Toista tai kumpaakaan lentokenttää ei löytynyt tietokannasta.")
    # tuloste jos yhteyttä ei ole
    except mysql.connector.Error as virhe:
        print(f"Tietokantavirhe: {virhe}")
    # suljetaan tietokanta yhteys
    finally:
        if 'yhteys' in locals() and yhteys.is_connected():
            yhteys.close()

# aloitetaan ohjelma kutsumalla funktiota laske_etaisyys.
if __name__ == "__main__":
    laske_etaisyys()