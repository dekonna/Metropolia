let alku = Number(prompt("Anna aloitusvuosi:"));
let loppu = Number(prompt("Anna lopetusvuosi:"));

let lista = "<ul>"; // avaa listan

// aloitetaan silmukka alkuvuodesta ; jatketaan loppuvuoteen ; lisätään 1 joka kierroksella
for (let vuosi = alku; vuosi <= loppu; vuosi++) {
    // jaollinen 4, ei jaollinen 100, jaollinen 400
    if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || vuosi % 400 === 0) {
        // jos karkausvuosi -> listaan
        lista += "<li>" + vuosi + "</li>";
    }
}

lista += "</ul>"; // sulkee listan

// tulostaa listan
document.querySelector("#viesti").innerHTML = lista;


// Number() yrittää muuttaa koko arvon numeroksi esim: 123abc -> 123
// parseFloat() lukee numeron alusta asti vaikka lopussa olisi muuta esim: 123abc -> 123abc