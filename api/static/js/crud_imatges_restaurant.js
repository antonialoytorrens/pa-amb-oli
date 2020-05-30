$(document).ready(function () {
  carregaOnClick();
  carregaOnChange();
  carregaPreview();
});

function carregaPreview() {
    if($("#img-list").children().length == 0) {
        $("#preview").hide();
        $("#errorseleccionafotografies").html("");
    }
}

function carregaOnClick() {
  $("#envia").click(function () {
  });

  $("#buida-imatges").click(function (e) { 
      $("#img-list").html("");
      $("#preview").hide();
  });
}

function carregaOnChange() {
  $("#file-input").change(function () { 
    carregaImatge(this);
  });
}

function carregaBanner() {
  $("#banner-multimedia").simpleBanner({
    dots:'dots-pagi',
    autoPlay:false,
  });
}

function carregaImatge(input) {
  let length = input.files.length;

  // MAX 5 FILES
  if(length > 5) {
    length = 5;
    alert("Només estan permesos cinc fitxers. Mostrant els cinc primers...");
  }
    if(input.files) {
      for(i=0;i<length;i++) {
      // PRIMER COMPROVA QUE TOTS COMPLEIXEN LES CONDICIONS
        var valid = validaFitxers(input.files[i]);
      }
      if(valid) {
  $("#img-list").html("");
  $("#point-list").remove();
  $("#preview").show();
      for(i=0;i<length;i++) {
      var reader = new FileReader();
      var li = $("<li></li>");
      reader.readAsDataURL(input.files[i]); // convert to base64 string
      reader.onload = function(e) {
        var img = $("<img src='"+e.target.result+"' class='img-responsive' alt=''>");
        $(li).append(img);
      }
      $("#img-list").append(li);
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