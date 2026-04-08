const numerot = [];

while (true) {
    const syote = Number(prompt("Anna luku:"));

    if (numerot.includes(syote)) {
        alert("Olet jo antanut tämän numeron :( ohjelma lopetetaan.");
        break;
    }

    numerot.push(syote);
}

numerot.sort((a, b) => a - b);

console.log("Annetut luvut nousevassa järjestyksessä:")
for (let i = 0; i < numerot.length; i++) {
    console.log(numerot[i])
}