$(function () {
  function check_messages() {
    $.ajax({
      url: '/messages/check/',
      cache: false,
      success: function (data) {
        $("#unread-count").text(data);
      },
      complete: function () {
        window.setTimeout(check_messages, 1000);
      }
    });
  };
  check_messages();
});