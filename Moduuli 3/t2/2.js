// hakee HLTM target
const target = document.getElementById("target");

// luo uuden <li> elementin
const firstItem = document.createElement("li");
firstItem.textContent = "First item";

// asettaa tekstin elementin sisälle
const secondItem = document.createElement("li");
secondItem.textContent = "Second item";
secondItem.classList.add("my-item");

const thirdItem = document.createElement("li");
thirdItem.textContent = "Third item"; // lisää css luokan

// Lisätään listaan
target.appendChild(firstItem);
target.appendChild(secondItem);
target.appendChild(thirdItem);