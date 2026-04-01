let maara = prompt("Kuinka monta noppaa heitetään?");
maara = Number(maara);

// muuttuja johon tulokset kerätään, alkuarvo 0
let summa = 0;

for (let i = 0; i < maara; i++) {
    let heitto = Math.floor(Math.random() * 6) + 1;
    // kasvattaa summaa nopan heiton verran
    summa = summa + heitto;
}
// Math.random() -> 0 - 0.999...
// * 6 -> 0 - 5.999...
// Math.floor() -> 0 - 5
// +1 -> 1 - 6

// sivulle tulostaminen
document.querySelector("#viesti").innerHTML = "Noppien summa on: " + summa;
// konsoliin tulostaminen:
// console.log("Noppien summa on: " + summa);


