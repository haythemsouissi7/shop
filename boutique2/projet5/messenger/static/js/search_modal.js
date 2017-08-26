
  $(function get_search_results(event) {
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
             
           $( "#modal-body2" ).html( html );
           //$pager.attr('data-current-page', page);
          // $(".page").val(page);
           // console.log(page)

            /*  if (html === "") {
                  $("#loader_message").html('<p>There were no results that match your search criteria</p>').show();
              } else {
                  $("#loader_message").html('Searching... Please wait <img src="http://www.example.com/monstroid/wp-content/uploads/2016/02/LoaderIcon.gif" alt="Loading">').show();
              }  
              window.busy = false; */
        }
      });



})
