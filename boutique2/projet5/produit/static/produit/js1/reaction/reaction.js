

$(function () {
  
  
   $('.reaction-button').on('click', function () {
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var productId = $this.attr('data-id');

      $.ajax({
          url: '/boutique/react/' + productId,
          data: {
              'reaction': type
          },
          success: function (data) {
              if (data.count > 0) {
                  if (data.count > 1) {
                      $this.parent().siblings('#reactions').text(data.count + ' reactions');
                      
                  } else {
                      $this.parent().siblings('#reactions').text(data.count + ' reaction');
                     
                  }
              } else {
                  $this.parent().siblings('#reactions').text('');
              }
          }
      })
    });
});