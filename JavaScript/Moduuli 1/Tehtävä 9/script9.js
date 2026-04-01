let anna_luku = Number(prompt("Anna luku: "));
// alkuluku = alkuluku
let alkuluku = true;
// jos luku on 0, 1 tai negatiivinen -> ei alkuluku
if (anna_luku < 2) {
    alkuluku = false;
}
// käydään läpi luvut
for (let i = 2; i < anna_luku; i++) {
    // löytyykö luku, joka jakaa annetun luvun -> jos löytyy se ei ole alkuluku.
    if (anna_luku % i === 0) {
        // jos jaollinen -> ei alkuluku
        alkuluku = false;
        break;
    }
}

if (alkuluku) {
    document.querySelector("#viesti").innerHTML = anna_luku + " on alkuluku";
} else {
    document.querySelector("#viesti").innerHTML = anna_luku + " ei ole alkuluku";
}

