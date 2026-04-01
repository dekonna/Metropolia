let year = parseInt(prompt("Enter a year:"));

let karkausvuosi;

if (year % 4 === 0) {
    if (year % 100 === 0) {
        if (year % 400 === 0) {
            karkausvuosi = true;
        } else {
            karkausvuosi = false;
        }
    } else {
        karkausvuosi = true;
    }
} else {
    karkausvuosi = false;
}

if (karkausvuosi) {
    document.querySelector("#viesti").innerHTML =
        year + " on karkausvuosi.";
} else {
    document.querySelector("#viesti").innerHTML =
        year + " ei ole karkausvuosi.";
}