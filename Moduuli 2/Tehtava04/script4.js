const numerot = [];

while (true) {
    const syote = Number(prompt("Anna numero (0 lopettaa):"));

    if (syote==0) {
        break
    }

    numerot.push(syote);
}

numerot.sort((a, b) => b - a);

console.log("Numerot suurimmasta pienimpään ovat:")
for (let i = 0; i < numerot.length; i++) {
    console.log(numerot[i]);
}