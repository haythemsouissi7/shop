$(function () {
  $("#attache").submit(function () {
    var data = new FormData(this);
    
    //alert("ajax call ...")
    $.ajax({
      
      url: '/messages/attache_image/',
      data: data,
      cache: false,
      type: 'post',
      contentType:false,
      processData:false,
      success: function (data) {
        $(".send-message").before(data);
        $("input[name='message']").val('');
        $("input[name='message']").focus();
      }
    });
    return false;
    
  });

});