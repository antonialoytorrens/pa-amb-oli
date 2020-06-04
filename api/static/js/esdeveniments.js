$(document).ready(function() {
    //carregaMapa();
});

function carregaMapa() {
    // Resize Iframe map dynamically
    $(window).on('resize', function() {
        $(".mapa-lloc").attr("width", $(".form-control.text-center").width());
        $(".mapa-lloc").attr("height", $(".form-control.text-center").width());
    })
}