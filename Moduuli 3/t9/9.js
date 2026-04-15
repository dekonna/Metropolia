const button = document.getElementById('start');
const calculation = document.getElementById('calculation');
const result = document.getElementById('result');

button.addEventListener('click', function () {

    const input = calculation.value;
    let answer;

    if (input.includes('+')) {
        const parts = input.split('+');
        answer = Number(parts[0]) + Number(parts[1]);

    } else if (input.includes('-')) {
        const parts = input.split('-');
        answer = Number(parts[0]) - Number(parts[1]);

    } else if (input.includes('*')) {
        const parts = input.split('*');
        answer = Number(parts[0]) * Number(parts[1]);

    } else if (input.includes('/')) {
        const parts = input.split('/');
        answer = Number(parts[0]) / Number(parts[1]);
    }

    result.textContent = answer;
});