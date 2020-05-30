$(document).ready(function() {
    carregaMouseOver();
});

function carregaMouseOver() {
    document.getElementById("mapaRestaurants").addEventListener("click", function() {

        var rect = document.getElementById("mapaRestaurants").getBoundingClientRect();
        alert('X: ' + rect.x + '<br>' + 'Y: ' + rect.y);
    })
}

function getCursorPosition(canvas, event) {
    const rect = canvas.getBoundingClientRect()
    const x = event.clientX - rect.left
    const y = event.clientY - rect.top
    console.log("x: " + x + " y: " + y)
}

const canvas = document.querySelector('canvas')
canvas.addEventListener('mousedown', function(e) {
    getCursorPosition(canvas, e)
})