const monta_osallistujaa = Number(prompt("Monta osallistujaa?:"));
const osallistujat = [];

for (let i = 0; i < monta_osallistujaa; i++) {
    osallistujat.push(prompt(`Anna osallistujan ${i + 1} nimi:`))
}

osallistujat.sort();

const lista =document.querySelector(`#lista`);

for (let i = 0; i < osallistujat.length; i++) {
    lista.innerHTML += `<li>${osallistujat[i]}</li>`;
}
