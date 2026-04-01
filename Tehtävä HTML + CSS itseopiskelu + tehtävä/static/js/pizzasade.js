document.addEventListener("DOMContentLoaded", () => {
    const positions = ["p1", "p2", "p3", "p4", "p5"];

    positions.forEach(cls => {
        const pizza = document.createElement("div");
        pizza.classList.add("pizza", cls);
        document.body.appendChild(pizza);
    });
});