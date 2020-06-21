function validaFotoPerfil() {
    valid = false;
    let missatgeError = "Només s'accepten imatges .png, o .jpg";

    if ($("#file-input").val() === "") {
        valid = true;
        $("#errorfotoperfil").html("");
    } else {
        let tamanyFitxer = $("#file-input")[0].files[0].size;
        let extensioImatge = $("#file-input").val().slice(this.length - 3);
        if (
            tamanyFitxer <= 3000000 && (extensioImatge === 'png' || extensioImatge === 'jpg')
        ) {
            valid = true;
            $("#errorfotoperfil").html("");
            //$("#elimina-foto-perfil").show();
        } else {
            $("#errorfotoperfil").html(missatgeError);
        }
    }
    return valid;
}

function carregaImatge(input) {
    if (validaFotoPerfil()) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function(e) {
                $('#foto-perfil').attr('src', e.target.result);
            }
            reader.readAsDataURL(input.files[0]); // convert to base64 string
        }
    } else {
        // Deixa input en blanc, i torna a posar l'imatge per defecte
        $("#file-input").val("");
        $("#foto-perfil").attr("src", "/static/images/base.png");
    }
}