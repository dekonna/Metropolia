const koirat = [];

for (let i = 0; i < 6; i++) {
    koirat.push(prompt(`Anna koiran ${i + 1} nimi:`));
}

koirat.sort().reverse();

const kahva = document.querySelector('#koiralista');

for (let koira of koirat) {
    kahva.innerHTML += `<li>${koira}</li>`;
}