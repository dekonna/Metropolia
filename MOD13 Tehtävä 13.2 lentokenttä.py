from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def hae_lentokentta(icao):
    yhteys = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        database="flight_game",
        user="root",
        password="Salasana1",
        autocommit=True
    )

    kursori = yhteys.cursor(dictionary=True)

    sql = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()

    return tulos

@app.route('/kenttä/<icao>')
def hae_kentta(icao):
    tulos = hae_lentokentta(icao)

    if tulos is None:
        return jsonify({"error": "Kenttää ei löytynyt"}), 404

    return jsonify({
        "ICAO": tulos["ident"],
        "Name": tulos["name"],
        "Municipality": tulos["municipality"]
    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)