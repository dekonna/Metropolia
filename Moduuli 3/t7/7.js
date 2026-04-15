const trigger = document.getElementById('trigger');
const target = document.getElementById('target');

trigger.addEventListener('mouseenter', function () {
    target.src = 'img/picB.jpg';
});

trigger.addEventListener('mouseleave', function () {
    target.src = 'img/picA.jpg';
});