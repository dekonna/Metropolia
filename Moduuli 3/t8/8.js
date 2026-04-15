const num1 = document.getElementById('num1');
const num2 = document.getElementById('num2');
const operation = document.getElementById('operation');
const button = document.getElementById('start');
const result = document.getElementById('result');

button.addEventListener('click', function () {

    const value1 = Number(num1.value);
    const value2 = Number(num2.value);

    let answer;

    if (operation.value === 'add') {
        answer = value1 + value2;
    } else if (operation.value === 'sub') {
        answer = value1 - value2;
    } else if (operation.value === 'multi') {
        answer = value1 * value2;
    } else if (operation.value === 'div') {
        answer = value1 / value2;
    }

    result.textContent = answer;
});