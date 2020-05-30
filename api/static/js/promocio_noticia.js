$(document).ready(function() {
    carregaOnClick();
    carregaOnChange();
    carregaDefaults();
});

function carregaOnClick() {
    $('#envia').click(function() {
        /* Si la suggerència és vàlida mostra el missatge indicant que tot ha anat bé. En cas contrari, mostra el missatge d'error */
        if (comprovaValidacio()) {
            $("#promocioenviada").fadeIn().delay(5000).fadeOut();
        } else {
            $("#errorpromocioenviada").fadeIn().delay(5000).fadeOut();
        }
    });
}

function carregaDefaults() {
    $("#preview_infopaginaweb").hide();
    $("#preview_infoemail").hide();
}

function carregaOnChange() {
    $('#file-input').change(function() {
        carregaImatge(this);
    });
    actualitzaNoticia();
}

function carregaBanner() {
    $('#banner-multimedia').simpleBanner({
        dots: 'dots-pagi',
        autoPlay: false,
    });

    $('#banner-previsio-total').simpleBanner({
        dots: 'dots-pagi',
        autoPlay: false,
    });
}
// Quan canvia el nom, email o telèfon, automàticament s'actualitza el perfil amb aquesta informació.

function actualitzaNoticia() {
    $('#nomproducte').change(function() {
        if (!$('#nomnegoci').val()) {
            $('.strong.pb-3.text-center').text($(this).val());
        } else {
            $('.strong.pb-3.text-center').text($(this).val() + ' promociona ' + $('#nomnegoci').val());
        }
        //$(".strong.pb-3.text-center").text($(this).val());
    });

    $('#nomnegoci').change(function() {
        $('.strong.pb-3.text-center').text($(this).val() + ' promociona ' + $('#nomproducte').val());
    });

    $('#email').change(function() {
        if (!$(this).val()) {
            $("#preview_infoemail").hide();
        } else {
            $("#preview_infoemail").show();
            $('#preview_email').text($(this).val());
        }
    });

    $("#paginaweb").change(function() {
        if (!$(this).val()) {
            $("#preview_infopaginaweb").hide();
        } else {
            $("#preview_infopaginaweb").show();
            $("#preview_paginaweb").text($(this).val());
        }
    });

    $('#telefon').change(function() {
        $('#preview_telefon').text($(this).val());
    });

    $('#promocio_descripcio').change(function() {
        $('#preview_descripcio').text($(this).val());
    });
}

function comprovaValidacio() {
    return comprovaNoBuit() && comprovaRegex();
}

/* Comprova que els camps obligatoris no estiguin buits */
function comprovaNoBuit() {
    let valid = true;
    let missatgeError = 'El camp no pot estar buit';

    // in javascript, an empty string, and null, both evaluate to false in a boolean context.

    // https://stackoverflow.com/questions/1812245/what-is-the-best-way-to-test-for-an-empty-string-with-jquery-out-of-the-box
    if (!$('#nomproducte').val()) {
        valid = false;
        $('#errornomproducte').html(missatgeError);
        $('#grupnomproducte').css('border', '1px solid red');
    } else {
        $('#errornomproducte').html('');
        $('#grupnomproducte').css('border', 'none');
    }

    if (!$('#descripcio').val()) {
        valid = false;
        $('#errordescripcio').html(missatgeError);
        $('#grupdescripcio').css('border', '1px solid red');
    } else {
        $('#errordescripcio').html('');
        $('#grupdescripcio').css('border', 'none');
    }

    if (!$('#telefon').val()) {
        valid = false;
        $('#errortelefon').html(missatgeError);
        $('#gruptelefon').css('border', '1px solid red');
    } else {
        $('#errortelefon').html('');
        $('#gruptelefon').css('border', 'none');
    }

    return valid;
}

// Comprova que els camps estiguin amb el format que toca
function comprovaRegex() {
    let valid = true;
    let missatgeError = 'No concorda amb el format.';

    // http://emailregex.com/
    let regexEmail = /^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/;

    let regexTelefon = /^(\+[0-9]{2,4}\s)?[0-9]{3,14}$/;

    // https://regexr.com/3e4a2
    let regexWeb = /^(https?:\/\/)?(www\.)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)|(https?:\/\/)?(www\.)?(?!ww)[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,4}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$/;

    if ($('#email').val() && !regexEmail.test($('#email').val())) {
        valid = false;
        $('#erroremail').html(missatgeError);
        $('#grupemail').css('border', '1px solid red');
    }

    if (!regexTelefon.test($('#telefon').val())) {
        valid = false;
        $('#errortelefon').html(missatgeError);
        $('#gruptelefon').css('border', '1px solid red');
    }

    if ($('#paginaweb').val() && !regexWeb.test($('#paginaweb').val())) {
        valid = false;
        $('#errorpaginaweb').html(missatgeError);
        $('#gruppaginaweb').css('border', '1px solid red');
    }

    return valid;
}

function carregaImatge(input) {
    let length = input.files.length;

    // MAX 5 FILES
    if (length > 5) {
        length = 5;
        alert('Només estan permesos cinc fitxers. Mostrant els cinc primers...');
    }
    if (input.files) {
        for (i = 0; i < length; i++) {
            // PRIMER COMPROVA QUE TOTS COMPLEIXEN LES CONDICIONS
            var valid = validaFitxers(input.files[i]);
        }
        if (valid) {
            $('.img-list').html('');
            $('.dots-pagi').remove();
            $('.preview').show();
            for (i = 0; i < length; i++) {
                var reader = new FileReader();
                var li = $('<li></li>');
                reader.readAsDataURL(input.files[i]); // convert to base64 string
                reader.onload = function(e) {
                    var img = $("<img src='" + e.target.result + "' class='img-responsive' alt=''>");
                    $(li).append(img);
                };
                $('#img-list-total').append(li);
            }
            carregaBanner();
        }
    } else {
        alert('Error inesperat');
        $('.preview').hide();
    }
}

function validaFitxers(fitxer) {
    valid = false;
    let missatgeError = 'Els fitxers no són vàlids';

    if ($('#file-input').val() === '') {
        valid = true;
        $('#errorseleccionafotografies').html('');
    } else {
        let tamanyFitxer = fitxer.size;
        let extensioImatge = fitxer.name.slice(this.length - 3);
        if (tamanyFitxer <= 3000000 && (extensioImatge === 'png' || extensioImatge === 'jpg')) {
            valid = true;
            $('#errorseleccionafotografies').html('');
        } else {
            $('#errorseleccionafotografies').html(missatgeError);
        }
    }
    return valid;
}