let noppia = Number(prompt("Kuinka monta noppaa?"));
let tavoite = Number(prompt("Mikä summa halutaan?"));

// muuttujat
let onnistumiset = 0;
let toistot = 10000;

// ulkosilmukka toistaa nopanheiton 10000krt
for (let i = 0; i < toistot; i++) {

    let summa = 0;
    // sisäsilmukka heittää noppaa
    for (let j = 0; j < noppia; j++) {
        // yksi heitto -> arpoo luvun 1-6
        let heitto = Math.floor(Math.random() * 6) + 1;
        // noppien summa
        summa += heitto;
    }
    // jos saatu summa on tavoite
    if (summa === tavoite) {
        // kasvatetaan laskuria 1 onnistumisella
        onnistumiset++;
    }
}
// laskee todennäköisyyden
let todennakoisyys = (onnistumiset / toistot) * 100;

// tulostus toFixed(2) = 2 desimaalia
document.querySelector("#viesti").innerHTML =
    "Todennäköisyys saada summa " + tavoite +
    " " + noppia + " nopalla on " +
    todennakoisyys.toFixed(2) + " %";

// toFixed: pyöristää luvun tiettyyn määrään desimaaleja ja palauttaa merkkijonon