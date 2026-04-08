function heita_noppaa() {
    return Math.floor(Math.random() * 6) + 1;
}

const heitot = [];
let tulos = 0;

while (tulos !== 6) {
    tulos = heita_noppaa()
    heitot.push(tulos);
}

let lista = "";

for (let i = 0; i < heitot.length; i++) {
    lista += `<li>Heitto ${i + 1}: ${heitot[i]}</li>`;
}

document.querySelector("#lista2").innerHTML = lista;