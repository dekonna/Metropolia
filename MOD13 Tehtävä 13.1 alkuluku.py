from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(luku):
    if luku < 2:
        return False

    for jakaja in range(2, luku):
        if luku % jakaja == 0:
            return False

    return True

@app.route('/alkuluku/<int:luku>')
def tarkista_alkuluku(luku):
    tulos = onko_alkuluku(luku)

    return jsonify({
        "Number": luku,
        "isPrime": tulos
    })

if __name__ == '__main__':
    app.run(port=3000, debug=True)