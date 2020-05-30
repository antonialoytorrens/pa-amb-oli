$(document).ready(function () {
    carregaOnClick();
    carregaOnChange();
    $("#banner-multimedia").simpleBanner({
        dots: 'dots-pagi',
        autoPlay: false,
    });
});

function carregaOnClick() {
    $("#envia").click(function () {
        /* Si la suggerència és vàlida mostra el missatge indicant que tot ha anat bé. En cas contrari, mostra el missatge d'error */
        let valid = validaRestaurant();
        if (valid) {
            creaRestaurant()
        } else {
            $("#error-crear-restaurant").fadeIn().delay(5000).fadeOut();
        }
    });
}

function carregaOnChange() {
    $("#file-input").change(function () {
        carregaImatge(this);
    });
}

function carregaBanner() {
    $("#banner-multimedia").simpleBanner({
        dots: 'dots-pagi',
        autoPlay: false,
    });
}

function validaRestaurant() {
    let valid = false;
    if (comprovaNoBuit() && comprovaRegex()) {
        valid = true;
    }
    return valid;
}

/* Comprova que els camps obligatoris no estiguin buits */
function comprovaNoBuit() {
    let valid = true;
    let missatgeError = "El camp no pot estar buit";

    // in javascript, an empty string, and null, both evaluate to false in a boolean context.

    // https://stackoverflow.com/questions/1812245/what-is-the-best-way-to-test-for-an-empty-string-with-jquery-out-of-the-box
    if (!$("#nomrestaurant").val()) {
        valid = false;
        $("#errornomrestaurant").html(missatgeError);
        $("#grupnomrestaurant").css("border", "1px solid red");
    } else {
        $("#errornomrestaurant").html("");
        $("#grupnomrestaurant").css("border", "none");
    }

    if (!$("#localitzacio").val()) {
        valid = false;
        $("#errorlocalitzacio").html(missatgeError);
        $("#gruplocalitzacio").css("border", "1px solid red");
    } else {
        $("#errorlocalitzacio").html("");
        $("#gruplocalitzacio").css("border", "none");
    }

    if (!$("#descripcio").val()) {
        valid = false;
        $("#errordescripcio").html(missatgeError);
        $("#grupdescripcio").css("border", "1px solid red");
    } else {
        $("#errordescripcio").html("");
        $("#grupdescripcio").css("border", "none");
    }

    if (!$("#horari").val()) {
        valid = false;
        $("#errorhorari").html(missatgeError);
        $("#gruphorari").css("border", "1px solid red");
    } else {
        $("#errorhorari").html("");
        $("#gruphorari").css("border", "none");
    }

    if (!$("#telefon").val()) {
        valid = false;
        $("#errortelefon").html(missatgeError);
        $("#gruptelefon").css("border", "1px solid red");
    } else {
        $("#errortelefon").html("");
        $("#gruptelefon").css("border", "none");
    }

    if (!$("#email").val()) {
        valid = false;
        $("#erroremail").html(missatgeError);
        $("#grupemail").css("border", "1px solid red");
    } else {
        $("#erroremail").html("");
        $("#grupemail").css("border", "none");
    }

    if (!$("#fax").val()) {
        valid = false;
        $("#errorfax").html(missatgeError);
        $("#grupfax").css("border", "1px solid red");
    } else {
        $("#errorfax").html("");
        $("#grupfax").css("border", "none");
    }

    if (!$("#responsableRestaurantSi").is(':checked') && !$("#responsableRestaurantNo").is(':checked')) {
        valid = false;
        $("#errorresponsablerestaurant").html(missatgeError);
    } else {
        $("#errorresponsablerestaurant").html("");
    }

    if (!$("#reservaTaulaSi").is(':checked') && !$("#reservaTaulaNo").is(':checked')) {
        valid = false;
        $("#errorreservataula").html(missatgeError);
    } else {
        $("#errorreservataula").html("");
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

    let regexTelefon = /^(\+[0-9]{2,4}\s)?[0-9]{3,14}$/;

    // http://emailregex.com/
    let regexEmail = /^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/;

    if (!regexEmail.test($("#email").val())) {
        valid = false;
        $("#erroremail").html(missatgeError);
        $("#grupemail").css("border", "1px solid red");
    }

    // Si el telèfon és buit, no el validis, només valida quan té un número escrit.

    if ($("#telefon").val() && !regexTelefon.test($("#telefon").val())) {
        valid = false;
        $("#errortelefon").html(missatgeError);
        $("#gruptelefon").css("border", "1px solid red");
    }

    return valid;
}

function carregaImatge(input) {
    let length = input.files.length;

    // MAX 5 FILES
    if (length > 5) {
        length = 5;
        alert("Només estan permesos cinc fitxers. Mostrant els cinc primers...");
    }
    if (input.files) {
        for (i = 0; i < length; i++) {
            // PRIMER COMPROVA QUE TOTS COMPLEIXEN LES CONDICIONS
            var valid = validaFitxers(input.files[i]);
        }
        if (valid) {
            $("#img-list").html("");
            $("#point-list").remove();
            $("#preview").show();
            for (i = 0; i < length; i++) {
                var reader = new FileReader();
                var li = $("<li></li>");
                $("#img-list").append(li);
                reader.readAsDataURL(input.files[i]); // convert to base64 string
                reader.onload = function (e) {
                    var img = $("<img src='" + e.target.result + "' class='img-responsive' alt=''>");
                    console.log(i);
                    $(li).append(img);
                }
            }
            carregaBanner();

        }
    } else {
        alert("Error inesperat");
        $("#preview").hide();
    }
}

function validaFitxers(fitxer) {
    valid = false;
    let missatgeError = "Els fitxers no són vàlids";

    if ($("#file-input").val() === "") {
        valid = true;
        $("#errorseleccionafotografies").html("");
    } else {
        let tamanyFitxer = fitxer.size;
        let extensioImatge = fitxer.name.slice(this.length - 3);
        if (
            tamanyFitxer <= 3000000 && (extensioImatge === 'png' || extensioImatge === 'jpg')
        ) {
            valid = true;
            $("#errorseleccionafotografies").html("");
        } else {
            $("#errorseleccionafotografies").html(missatgeError);
        }
    }
    return valid;
}