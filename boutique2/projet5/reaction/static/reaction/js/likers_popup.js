function doPopups() {
  if (!document.getElementsByTagName) return false;
  var links=document.getElementsByTagName("a");
  for (var i=0; i < links.length; i++) {
    if (links[i].className.match("popup")) {
      links[i].onclick=function() {
        // Below - to open a full-sized window, just use: window.open(this.href);
        window.open(this.href, "", "top=40,left=40,width=600,height=400,scrollbars");
        return false;
      }
    }
  }
}
window.onload=doPopups;
