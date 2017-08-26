$(function () {
  $(".send_product").submit(function () {
    
    $.ajax({

      url: '/messages/new_product/',
      data: $(this).serialize(),
      cache: false,
      type: 'post',
      success: function (data) {
        alert("message succes0000")
        $(".send-message").before(data);
        $("input[name='message']").val('');
        $("input[name='message']").focus();
      }
    });
    return false;
  });
});

         
$(function () {
  $(".send_product_inbox").submit(function () {
    
    $.ajax({

      url: '/messages/sendd/',
      data: $(this).serialize(),
      cache: false,
      type: 'post',
      success: function (data) {
        alert("message succes0000")
        $(".send-message").before(data);
        $("input[name='message']").val('');
        $("input[name='message']").focus();
      }
    });
    return false;
  });
});

