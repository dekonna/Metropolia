console.log("I'm printing to console!"); // printtaa konsoliin

let name = prompt("What is your name?"); // kysyy käytääjän nimen, muuttuja name
// hakee html elementin jonka id on "viesti" ja kirjoittaa tervehdyksen
document.querySelector("#viesti").innerHTML = "Hello, " + name + "!";
// hakee elementin viesti                  // kirjoittaa tervehdyksen

// console.log kehittäjälle
// innerHTML käyttäjälle