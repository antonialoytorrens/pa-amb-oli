$(document).ready(function() {
    carregaOnClick();
});

function carregaOnClick() {
    /* Si la suggerència és vàlida mostra el missatge indicant que tot ha anat bé. En cas contrari, mostra el missatge d'error */
    $("#envia").click(function(e) {
        e.preventDefault();
        let valid = validaSuggeriment();
        if (valid) {
            $("#enviasuggeriment").fadeIn().delay(5000).fadeOut();
            setTimeout(function() { $("#form-suggeriment").submit(); }, 3000);
        } else {
            $("#errorenviasuggeriment").fadeIn().delay(5000).fadeOut();
        }
    });
}

function validaSuggeriment() {
    let valid = false;
    if (comprovaNoBuit()) {
        valid = true;
    }
    return valid;
}

function comprovaNoBuit() {

    let valid = true;
    let missatgeError = "El camp no pot estar buit";

    // in javascript, an empty string, and null, both evaluate to false in a boolean context.

    if (!$("#explicacio").val()) {
        valid = false;
        $("#errorexplicacio").html(missatgeError);
        $("#explicacio").css("border", "1px solid red");
    } else {
        $("#errorexplicacio").html("");
        $("#explicacio").css("border", "1px solid #ced4da");
    }

    return valid;
}