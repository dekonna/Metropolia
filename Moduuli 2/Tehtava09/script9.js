function even(taulukko) {
    const uusi_taulukko = [];

    for (let i = 0; i < taulukko.length; i++) {
        if (taulukko[i] % 2 === 0) {
            uusi_taulukko.push(taulukko[i]);
        }
    }
    return uusi_taulukko;
}

const alkuperaiset_luvut = [2, 15, 666, 333, 4, 7, 99];
const parilliset_luvut = even(alkuperaiset_luvut);

console.log("Alkuperäinen taulukko:", alkuperaiset_luvut);
console.log("Parilliset luvut:", parilliset_luvut);