$(document).ready(function() {
    carregaOnClick();
});

function carregaOnClick() {
    $("#bLogin").click(function() {
        /* Si el registre és vàlid mostra el missatge indicant que tot ha anat bé. En cas contrari, mostra el missatge d'error */
        let valid = comprovaNoBuit();
        if (valid) {
            // TODO
        } else {
            $("#errorusuarilogin").fadeIn().delay(5000).fadeOut();
        }
    });
}

function comprovaNoBuit() {
    let valid = true;
    let missatgeError = "El camp no pot estar buit";

    // in javascript, an empty string, and null, both evaluate to false in a boolean context.

    // https://stackoverflow.com/questions/1812245/what-is-the-best-way-to-test-for-an-empty-string-with-jquery-out-of-the-box
    if (!$("#username").val()) {
        valid = false;
        $("#errorusername").html(missatgeError);
        $("#grupusername").css("border", "1px solid red");
    } else {
        $("#errorusername").html("");
        $("#grupusername").css("border", "none");
    }

    if (!$("#password").val()) {
        valid = false;
        $("#errorpassword").html(missatgeError);
        $("#gruppassword").css("border", "1px solid red");
    } else {
        $("#errorpassword").html("");
        $("#gruppassword").css("border", "none");
    }
    return valid;
}