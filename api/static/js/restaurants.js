$(document).ready(function() {
    carregaOnClick();
    carregaValoracio();
});

function enviaComentari() {
    let valid = comentariValid();
    if (valid) {

        $("#comentari-pendent").hide();

        var formData = new FormData();
        formData.append("profile", $("#profile_id").val());
        formData.append("restaurant", $("#restaurant_id").val());
        formData.append("missatge", $("#missatge").val());

        $.ajax({
            type: "POST",
            url: "/restaurants/comentaris/crea/",
            dataType: "json",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data.error) {
                    $("#missatgeerror").html("No s'ha pogut enviar el comentari: " + data.errors["__all__"][0]);
                    $("#errorcomentarienviat").fadeIn().delay(5000).fadeOut();
                } else {
                    $("#comentarienviat").fadeIn().delay(5000).fadeOut();
                    $("#comentari-pendent").show();
                    $("#missatge").val("");
                }
            },
            error: function() {
                $("#errorcomentaricamps").fadeIn().delay(5000).fadeOut();
            }
        });

    }
}

function carregaOnClick() {
    $('#enviacomentari').click(function() {
        enviaComentari();
    })
    $("#reserva").click(function() {
        $("#reservaalert").fadeIn();
    });
}

function comentariValid() {
    let missatgeError = "El camp no pot estar buit";
    let valid = true;
    if (!$("#missatge").val()) {
        $("#errormissatge").html(missatgeError);
        $("#errormissatge").show();
        $("#grupmissatge").css("border", "1px solid red");
        $("#errorcomentaricamps").fadeIn().delay(5000).fadeOut();
        valid = false;
    } else {
        $("#errormissatge").html("");
        $("#errormissatge").hide();
        $("#grupmissatge").css("border", "none");
    }
    return valid;
}

function carregaValoracio() {
    $(document).on({
        mouseover: function(event) {
            $(this).find('.far').addClass('star-over');
            $(this).prevAll().find('.far').addClass('star-over');
        },
        mouseleave: function(event) {
            $(this).find('.far').removeClass('star-over');
            $(this).prevAll().find('.far').removeClass('star-over');
        }
    }, '.rate');


    $(document).on('click', '.rate', function(evt) {
        // No llancis l'onclick dos cops
        evt.stopPropagation();
        evt.preventDefault();
        evt.stopImmediatePropagation();
        if (!$(this).find('.star').hasClass('rate-active')) {
            $(this).siblings().find('.star').addClass('far').removeClass('fas rate-active');
            $(this).find('.star').addClass('rate-active fas').removeClass('far star-over');
            $(this).prevAll().find('.star').addClass('fas').removeClass('far star-over');
        }
        var formData = new FormData();
        formData.append("profile", $("#profile_id").val());
        formData.append("restaurant", $("#restaurant_id").val());
        formData.append("valoracio", $('.star.fas').length);

        $.ajax({
            type: "POST",
            url: "/restaurants/valoracio/envia/",
            dataType: "json",
            data: formData,
            processData: false,
            contentType: false,
            success: function(data) {
                if (data.error) {
                    $("#missatgeerror").html("No s'ha pogut enviar la valoració: " + data.errors["__all__"][0]);
                    $("#errorvaloracioenviada").fadeIn().delay(5000).fadeOut();
                } else {
                    $("#comentarienviat").fadeIn().delay(5000).fadeOut();
                }
            },
        });
    });
}