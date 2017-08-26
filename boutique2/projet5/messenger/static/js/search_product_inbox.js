 
  $(function () {
    function get_search_results(event) {
        //var $pager = $('.pager')
        var itemID = $(event.target).val();
        
        $.ajax({
            type  : "GET",
            async : false,
            url   : '/messages/search_modal/',
            data  :{
             recherche: $("#recherche").val(),
             to: $("#to").val(),
             //page : page,
           },
            cache : false,
            success: function(html) {
                 
               $( "#modal-body3" ).html( html );
            console.log("aaa")
            }
          });

    }
        $("#recherche").on('keyup', function (e) {
          get_search_results(e);
        });
  })
