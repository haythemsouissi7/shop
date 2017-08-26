$(function () {
  
  
   $('.reaction-button').on('click', function () {
      var $this = $(this);
      var type = $this.attr('data-reaction');
      var productId = $this.attr('data-id');
      var reaction = $this.parent().parent();

      $.ajax({
          url: '/react/' + productId,
          data: {
              'reaction': type
          },
          success: function (data) {
              
                  
                    reaction.children('.reactions').text('('+data.count+')');
                    reaction.children('.col-md-1').children('.reaction-button').children('.tooltiptext1').text(data.normal);
                    reaction.children('.col-md-1').children('.reaction-button').children('.tooltiptext2').text(data.smile);
                    reaction.children('.col-md-1').children('.reaction-button').children('.tooltiptext3').text(data.love);
                    reaction.children('.col-md-1').children('.reaction-button').children('.tooltiptext4').text(data.wish);
                       

                                    
                      
                      
                
             
          }
      })
    });
});