// kysytään halutaanko laskea neliöjuuri
let kysymys = confirm("Laskenko neliöjuuren?");

if (kysymys) {
    // kysytään numero (prompt) ja muunnetaan numeroksi (parseFloat)
    let numero = parseFloat(prompt("Anna numero:"));

    if (numero < 0) {
        // negatiivinen luku
        document.querySelector("#viesti").innerHTML =
            "Negatiivisen luvun neliöjuurta ei ole määritelty.";
    } else {
        // lasketaan neliöjuuri Math.sqrt funktiolla
        let tulos = Math.sqrt(numero);

        document.querySelector("#viesti").innerHTML =
            "Neliöjuuri luvusta " + numero + " on " + tulos;
    }

} else {
    // käyttäjä painoi Cancel
    document.querySelector("#viesti").innerHTML =
        "Neliöjuurta ei lasketa.";
}

// confirm() näyttää käyttäjälle kysymysikkunan, jossa on kaksi nappia ok ja cancel
// Math kirjaston funktioita:
// Math.random()   // satunnaisluku
// Math.floor()    // pyöristys alas
// Math.ceil()     // pyöristys ylös
// Math.round()    // normaali pyöristys
// Math.sqrt()     // neliöjuuri