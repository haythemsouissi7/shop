function clock(produit) {
    var $clock = produit.children('.clock'); 
    var d = new Date();
    var n = d.getTimezoneOffset();

    var year=$clock.attr('year');
    var month=$clock.attr('month');
    var day=$clock.attr('day');

    var minut=$clock.attr('minut');
    var second=$clock.attr('second');
    var x= +$clock.attr('hour')+1;
    

    //alert(year +'/'+ month+'/'+day+' '+hour+':'+minut+':'+second);

    $clock.countdown($clock.attr('year') +'/'+ $clock.attr('month')+'/'+$clock.attr('day')+' '+x+':'+$clock.attr('minut')+':'+$clock.attr('second'))
    .on('update.countdown', function(event) {
      var format = '%H:%M:%S';
     
     
      $(this).html(event.strftime(format));
    })
    .on('finish.countdown', function(event) {
      $(this).html('This offer has expired!')
        .parent().addClass('disabled');

    });
  }