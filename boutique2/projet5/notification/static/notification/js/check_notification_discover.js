$(function () {
  $('#notif').popover({html: true, content: 'Loading...', trigger: 'manual'});

  $("#notif").click(function () {
    if ($(".popover").is(":visible")) {
      $("#notif").popover('hide');
    }
    else {
      $("#notif").popover('show');
      $.ajax({
        url: '/notifications/last/',
        beforeSend: function () {
          $(".popover-content").html("<div style='text-align:center'><img src='/static/img/loading.gif'></div>");
          $("#notif").removeClass("new-notifications");
        },
        success: function (data) {
          $(".popover-content").html(data);
        }
      });
    }
    return false;
  });

  function check_notifications() {
    $.ajax({
      url: '/notifications/check/',
      cache: false,
      success: function (data) {
        if (data != "0") {
          $("#notif").addClass("new-notifications");
        }
        else {
          $("#notif").removeClass("new-notifications");
        }
      },
      complete: function () {
        window.setTimeout(check_notifications, 3000);
      }
    });
  };
  check_notifications();
});



