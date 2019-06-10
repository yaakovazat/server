$(document).ready(function () {

  $("#k_link").click(function (e) {
    e.preventDefault();
    $("#l_link").removeClass("active_link");
    $(this).addClass("active_link");

    if ($("#form_label").text() == 'Matin engiziniz:') {
      $("#form_label").text('Мәтін енгізіңіз:');
    }

    // $("#textarea").on("keyup", function(){
    //   limitInput('ru', $(this));
    // });

  });

  $("#l_link").click(function (e) {
    e.preventDefault();
    $("#k_link").removeClass("active_link");
    $(this).addClass("active_link");

    if ($("#form_label").text() == 'Мәтін енгізіңіз:') {
      $("#form_label").text('Matin engiziniz:');
    }

    // $("#textarea").on("keyup", function(){
    //   limitInput('en',  $(this));
    // });

  });

  $("#arrow_icon").click(function (e) {
    e.preventDefault();

    if ($("#k_link").hasClass("active_link")) {

      $("#k_link").removeClass("active_link");
      $("#l_link").addClass("active_link");

      // $("#textarea").on("keyup", function(){
      //   limitInput('ru', $(this));
      // });

    } else {

      $("#l_link").removeClass("active_link");
      $("#k_link").addClass("active_link");

      // $("#textarea").on("keyup", function(){
      //   limitInput('en',  $(this));
      // });

    }

    if ($("#form_label").text() == 'Мәтін енгізіңіз:') {
      $("#form_label").text('Matin engiziniz:');
    } else {
      $("#form_label").text('Мәтін енгізіңіз:');
    }
  });

  // function limitInput( k, obj ) {
  //   switch( k ){
  //     case 'ru':
  //       obj.val(obj.val().replace(/[^а-яА-ЯёЁ0-9 -]/ig, ''));
  //       break;

  //     case 'en':
  //       obj.val(obj.val().replace(/[^a-zA-Z0-9 -]/ig, ''));           
  //       break;
  //   }
  // }


  $('input.file_input').on('change', function (e) {
    var fname = e.target.files[0].name;

    $(".file_upload").css('display', 'none');
    $(".filename").css('display', 'block');

    $('.filename .fname').text(fname);
  });

  $(".x_btn").click(function () {
    $(".file_upload").css('display', 'block');
    $(".filename").css('display', 'none');
  });

  $("#x_btn_reload").click(function(){
    window.location.reload();
  });

  $("#crop_button").click(function(){
    $(this).css('display', 'none');
  });
});