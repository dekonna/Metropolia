import mysql.connector

# funktio joka muodostaa yhteyden tietokantaan ja toteuttaa kyselyn käyttäjältä
def laske_lentokentat_tyypeittain():
    try:
        # muodostetaan yhteys ja yhteys asetukset
        yhteys = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Salasana1",
            database="flight_game"
        )
        # varmennetaan saatu yhteys ja luodaan kursori
        if yhteys.is_connected():
            kursori = yhteys.cursor()

            # kysytään maakoodi
            maakoodi = input("Syötä maakoodi (esim. FI): ").upper().strip()

            # sql kysely: lasketaan COUNT määrät ja ryhmitellään GROUP BY tyypin mukaan
            sql = "SELECT type, COUNT(*) FROM airports WHERE iso_country = %s GROUP BY type"
            # lähettää kyselyn tietokannalle
            kursori.execute(sql, (maakoodi,))

            # haetaan KAIKKI rivit (koska tyyppejä on useita)
            tulokset = kursori.fetchall()

            print(f"\n*** Lentokentät maassa: {maakoodi} ***")

            if tulokset:
                # käydään lista läpi rivi riviltä
                for rivi in tulokset:
                    # rivi[0] on tyyppi (esim. small_airport)
                    # rivi[1] on COUNT funktion palauttama lukumäärä
                    tyyppi = rivi[0]
                    maara = rivi[1]
                    print(f"{tyyppi}: {maara} kappaletta")
            else:
                print(f"Maakoodilla '{maakoodi}' ei löytynyt tietoja.")

            print("------------------------------\n")
    # virheilmoitus
    except mysql.connector.Error as virhe:
        print(f"Tietokantavirhe: {virhe}")
    # suljetaan yhteys
    finally:
        if 'yhteys' in locals() and yhteys.is_connected():
            yhteys.close()
            print("Yhteys suljettu.")

# kutsutaan funktiota jolla ohjelma aloitetaan
if __name__ == "__main__":
    laske_lentokentat_tyypeittain()