# kirjasto jolla yhdistetään mariaDB ja python
import mysql.connector

# funktio joka avaa yhteyden tietokantaan ja suorittaa haun
def etsi_lentokentta():
    # Otetaan yhteys tietokantaan
    # missä tietokanta on (localhost eli 127.0.0.1), kuka kysyy(user), salasana, mikä tietokanta(flight_game)
    # try testaa -> jos yhteys epäonnistuu siirrytään except lohkoon.
    try:
        yhteys = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Salasana1",
            database="flight_game"
        )
        # jos yhteys on auki
        if yhteys.is_connected():
            # luodaan kursori eli osoitin, jolla tietokannasta haetaan tietoa
            kursori = yhteys.cursor()

            # käyttäjän syöte, upper() muuttaa pienet kirjaimet isoiksi
            icao_koodi = input("Syötä lentoaseman ICAO-koodi (esim. EFHK): ").upper()

            # alustetaan sql kysely
            # %s on paikkamerkki johon käyttäjän syöte tallennetaan
            sql = "SELECT name, municipality FROM airports WHERE ident = %s"
            # execute lähettää kyselyn tietokannalle
            kursori.execute(sql, (icao_koodi,))
            # hakee ensimmäisenä löytyneen rivin joka sopii käyttäjän syötteeseen (fetchone)
            # arvo tallentuu tulos muuttujaan monikkona (tuple) tai on none
            tulos = kursori.fetchone()

            # tulosteet
            print("\n*** Hakutulokset ***")
            if tulos:
                # jos tulos ei ole none tulostetaan tiedot
                # tulos[0] = name ja
                # tulos[1] = municipality eli sarakkeet taulussa -> airports
                print(f"Lentoaseman nimi: {tulos[0]}")
                print(f"Sijainti: {tulos[1]}")
            else:
                print(f"Virhe: ICAO-koodilla '{icao_koodi}' ei löytynyt tietoja.")
            print("---------------------------\n")
    # jos tietokantaan ei saada saada yhteyttä
    except mysql.connector.Error as virhe:
        print(f"Tietokantavirhe: {virhe}")
    # ajetaan aina
    finally:
        # suljetaan yhteys aina lopuksi
        if 'yhteys' in locals() and yhteys.is_connected():
            yhteys.close()
            print("Yhteys suljettu.")


# käynnistetään haku -> kutsuu etsi_lentokentta() funktiota
if __name__ == "__main__":
    etsi_lentokentta()