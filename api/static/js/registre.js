$(document).ready(function() {
    carregaOnClick();
    carregaOnChange();
});

function carregaOnClick() {
    $("#registre").click(function() {
        /* Si el registre és vàlid crea el perfil. En cas contrari, mostra el missatge d'error */
        let valid = validaRegistre();
        if (valid) {
            creaPerfil();
        } else {
            $("#errorusuaricamps").fadeIn().delay(5000).fadeOut();
        }
    });
    $("#selecciona-foto-perfil").click(function() {
        $("#file-input").trigger("click");
    });
    $("#elimina-foto-perfil").click(function() {
        $("#foto-perfil").attr("src", "/static/images/base.png");
        $("#file-input").html("");
        $(this).hide();
    });
}

function carregaOnChange() {
    $("#file-input").change(function() {
        carregaImatge(this);
    });
    actualitzaPerfil();
}

// Quan canvia el nom, email o telèfon, automàticament s'actualitza el perfil amb aquesta informació.

function actualitzaPerfil() {
    $("#nomillinatges").change(function() {
        $("#profile-usertitle-name").text($(this).val());
    });

    $("#email").change(function() {
        $("#profile-usertitle-job").text($(this).val());
    });

    $("#telefon").change(function() {
        $("#profile-usertitle-phone").text($(this).val());
    });
}

function validaRegistre() {
    return comprovaNoBuit() && comprovaRegex();
}

/* Comprova que els camps obligatoris no estiguin buits */
function comprovaNoBuit() {
    let valid = true;
    let missatgeError = "El camp no pot estar buit";

    // in javascript, an empty string, and null, both evaluate to false in a boolean context.

    // https://stackoverflow.com/questions/1812245/what-is-the-best-way-to-test-for-an-empty-string-with-jquery-out-of-the-box
    if (!$("#nomillinatges").val()) {
        valid = false;
        $("#errornomillinatges").html(missatgeError);
        $("#grupnomillinatges").css("border", "1px solid red");
    } else {
        $("#errornomillinatges").html("");
        $("#grupnomillinatges").css("border", "none");
    }

    if (!$("#datanaixement").val()) {
        valid = false;
        $("#errordatanaixement").html(missatgeError);
        $("#grupdatanaixement").css("border", "1px solid red");
    } else {
        $("#errordatanaixement").html("");
        $("#grupdatanaixement").css("border", "none");
    }

    if (!$("#direccio").val()) {
        valid = false;
        $("#errordireccio").html(missatgeError);
        $("#grupdireccio").css("border", "1px solid red");
    } else {
        $("#errordireccio").html("");
        $("#grupdireccio").css("border", "none");
    }

    if (!$("#password").val() || !$("#rpassword").val()) {
        valid = false;
        $("#errorpassword").html(missatgeError);
        $("#gruppassword").css("border", "1px solid red");
    } else {
        if (!comprovaPassword()) {
            valid = false;
        } else {
            $("#gruppassword").css("border", "none");
            $("#errorpassword").html("");
        }
    }

    if (!$("#email").val()) {
        valid = false;
        $("#erroremail").html(missatgeError);
        $("#grupemail").css("border", "1px solid red");
    } else {
        $("#erroremail").html("");
        $("#grupemail").css("border", "none");
    }

    if (!validaFotoPerfil()) {
        valid = false;
    } else {
        $("#errorfotoperfil").html("");
    }

    return valid;
}

// Comprova que els camps estiguin amb el format que toca
function comprovaRegex() {
    let valid = true;
    let missatgeError = "No concorda amb el format.";

    // https://stackoverflow.com/questions/16462297/regex-for-date-validation-in-javascript
    let regexDataNaixement = /^(\d{1,2})\/(\d{1,2})\/(\d{4})$/;

    let regexTelefon = /^(\+[0-9]{2,4}\s)?[0-9]{3,14}$/;

    let regexPassword = /^.{8,}$/;

    // http://emailregex.com/
    let regexEmail = /^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/;

    if (!regexDataNaixement.test($("#datanaixement").val())) {
        valid = false;
        $("#errordatanaixement").html(missatgeError);
        $("#grupdatanaixement").css("border", "1px solid red");
    }

    if (!regexPassword.test($("#password").val())) {
        valid = false;
        $("#errorpassword").html(missatgeError);
        $("#gruppassword").css("border", "1px solid red");
    }

    if (!regexEmail.test($("#email").val())) {
        valid = false;
        $("#erroremail").html(missatgeError);
        $("#grupemail").css("border", "1px solid red");
    }

    // Si el telèfon és buit, no el validis, només valida quan té un número escrit.

    if ($("#telefon").val() && !regexTelefon.test($("#telefon").val())) {
        $("#errortelefon").html(missatgeError);
        $("#gruptelefon").css("border", "1px solid red");
    }

    return valid;
}

// Comprova que les contrasenyes coincideixen
function comprovaPassword() {
    valid = true;
    let missatgeError = "Les contrasenyes no coincideixen";

    // Les contrasenyes no coincideixen
    if ($("#password").val() !== $("#rpassword").val()) {
        valid = false;
        $("#gruppassword").css("border", "1px solid red");
        $("#errorpassword").html(missatgeError);
    }

    return valid;
}

// Si no s'ha seleccionat cap foto de perfil, és vàlid. Però si n'hi ha, comprova que s'ha seleccionat un arxiu .png, .jpg i que pesi menys de 3 MB.
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
            $("#elimina-foto-perfil").show();
        } else {
            $("#errorfotoperfil").html(missatgeError);
        }
    }
    return valid;
}


// Carrega imatge de perfil a mode de previsualització (sense realitzar cap tipus de petició)

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
        //$("#file-input").val("C:\\fakepath\\base.png");
        $("#foto-perfil").attr("src", "/static/images/base.png");
    }
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// Crea el Perfil
function creaPerfil() {
    var formData = new FormData();
    formData.append("nomillinatges", $("#nomillinatges").val());
    formData.append("datanaixement", $("#datanaixement").val());
    formData.append("direccio", $("#direccio").val());
    formData.append("contrasenya", $("#password").val());
    formData.append("email", $("#email").val());
    formData.append("telefon", $("#telefon").val());
    formData.append("fotoperfil", $("#file-input").val());

    // Registra'l a la base de dades

    //var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    /*$.ajaxSetup({
        beforeSend: function(xhr, settings) {
            // if not safe, set csrftoken
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });*/

    $.ajax({
        type: "POST",
        url: "/perfil/crea/",
        dataType: "json",
        data: formData,
        processData: false,
        contentType: false,
        success: function(data) {
            console.log(data);
            if (data.error) {
                $("#missatgeerror").html("No s'ha pogut crear l'usuari: " + data.errors["__all__"][0]);
                $("#errorusuaricreat").fadeIn().delay(5000).fadeOut();
            } else {
                $("#usuaricreat").fadeIn().delay(5000).fadeOut();
                window.location.href = "/login/";
            }
        },
        error: function(data) {
            $("#errorusuaricamps").fadeIn().delay(5000).fadeOut();
        }
    });
}