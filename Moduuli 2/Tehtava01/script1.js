const luvut = []

for (let i = 0; i < 5; i++) {
    const annaluku = prompt(`Anna luku ${i + 1}. luku:`);
    luvut.push(Number(annaluku));
}

for (let i = luvut.length -1; i >= 0; i--) {
    console.log(luvut[i])
}

