function heita_noppaa(tahkot) {
    return Math.floor(Math.random() * tahkot) + 1;
}

const nopan_koko = Number(prompt("Kuinka monta tahkoa nopassa on?"));
const heitot = [];
let tulos;

do {
    tulos = heita_noppaa(nopan_koko);
    heitot.push(tulos);
} while (tulos !== nopan_koko);

let lista = "";
for (let i = 0; i < heitot.length; i++) {
    lista += `<li>Heitto ${i + 1}: ${heitot[i]}</li>`;
}

document.querySelector("#lista").innerHTML = lista;

