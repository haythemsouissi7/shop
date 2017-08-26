
$(function () {

  var time=$('.up1').attr('data_time');
  var day=$('.up1').attr('data_day');
  alert(day.getDay())

var startDateTime = new Date(day,time); // YYYY (M-1) D H m s ms (start time and date from DB)
var startStamp = startDateTime.getTime();

var newDate = new Date();
var newStamp = newDate.getTime();

var timer;

function updateClock() {
    newDate = new Date();
    newStamp = newDate.getTime();
    var diff = Math.round((startStamp-newStamp)/1000);
    
  
    var h = Math.floor(diff/(60*60));
    diff = diff-(h*60*60);
    var m = Math.floor(diff/(60));
    diff = diff-(m*60);
    var s = diff;
    
    //document.getElementById("time-elapsed").innerHTML = h+": "+m+":"+s;
    $('.time-elapsed').text(h+": "+m+":"+s);
    
}

setInterval(updateClock, 1000);
})