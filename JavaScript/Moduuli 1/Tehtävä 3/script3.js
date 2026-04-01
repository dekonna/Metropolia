console.log("I'm printing to console!"); // printtaa konsoliin
// prompt palauttaa tekstin, parseFloat muuttaa sen numeroksi
let numero1 = parseFloat(prompt("Anna ensimmäinen numero"));
let numero2 = parseFloat(prompt("Anna toinen numero"));
let numero3 = parseFloat(prompt("Anna kolmas numero"));

// summa
let summa = numero1 + numero2 + numero3;
// tulo
let product = numero1 * numero2 * numero3;
// keskiarvo
let average = summa / 3;

// tuloste sivulla
document.querySelector("#viesti").innerHTML =
    "summa: " + summa + "<br>" +
    "product: " + product + "<br>" +
    "average: " + average;
