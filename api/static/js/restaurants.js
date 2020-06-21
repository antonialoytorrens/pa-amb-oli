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
    $("#reservano").click(function() {
        $("#reservaalert").fadeOut();
    });
    $("#reservasi").click(function() {
        $("#reservaalert").fadeOut();
    });
    $("#bCerca").click(function(e) {
        e.preventDefault();
        if (validaCerca()) {
            $("#errorcerca").hide();
            $("#cercaRestaurant").css("border", "none");
            $("#cercaRestaurant").submit();
        } else {
            $("#errorcerca").show();
            $("#cercaRestaurant").css("border", "1px solid red");
        }
    });
}

function validaCerca() {
    return $("#cerca").val();
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


    $('.rate').on("click", function(evt) {
        // No llancis l'onclick dos cops

        //evt.stopPropagation();
        //evt.stopImmediatePropagation();
        //evt.preventDefault();
        if ($(this).find('.star').hasClass('rate-active')) {
            $(this).siblings().find('.star').addClass('far').removeClass('fas rate-active');
            $(this).find('.star').addClass('rate-active fas').removeClass('far star-over');
            $(this).prevAll().find('.star').addClass('fas').removeClass('far star-over');
        } else {
            $(this).siblings().find('.star').addClass('far').addClass('fas rate-active');
            $(this).find('.star').addClass('rate-active fas').addClass('far star-over');
            $(this).prevAll().find('.star').addClass('fas').addClass('far star-over');
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
                    $("#errorvaloracioenviada").finish();
                    $("#missatgeerror").html("No s'ha pogut enviar la valoració: " + data.errors["__all__"][0]);
                    $("#errorvaloracioenviada").fadeIn().delay(5000).fadeOut();
                } else {
                    $("#valoracioenviada").finish();
                    $("#valoracioenviada").fadeIn().delay(5000).fadeOut();
                }
            },
        });
    });
}