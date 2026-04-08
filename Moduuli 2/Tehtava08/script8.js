function concat(taulukko) {
    let tulos = "";

    for (let i = 0; i < taulukko.length; i++) {
        tulos = tulos + taulukko[i];
    }
    return tulos;
}

const nimet = ["Johnny", "DeeDee", "Joey", "Marky"];
const lopputulos = concat(nimet);

document.querySelector("#viesti").innerHTML = lopputulos;