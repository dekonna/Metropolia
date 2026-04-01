console.log("I'm printing to console!"); // printtaa konsoliin

let nimi = prompt("Kuka olet?");

// arpoo tuvan ->
// math.random palauttaa aina desimaaliluvun
// math.floor pyöristää luvun alaspäin kokonaislukuun
let random = Math.floor(Math.random() * 4) + 1;
// 0,1,2,3 -> +1 = 1,2,3,4

// tuvan valinta -> tulos tallentuu muuttujaan tuvat
let tupa;

// tuvan arvonta
if (random == 1) {
    tupa = "Gryffindor";
} else if (random == 2) {
    tupa = "Slytherin";
} else if (random == 3) {
    tupa = "Hufflepuff";
} else {
    tupa = "Ravenclaw"
}

// tuloste sivulla
document.querySelector("#viesti").innerHTML =
    nimi + ", olet " + tupa + "!";
