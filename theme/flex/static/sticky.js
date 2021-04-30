
window.onscroll = function() { onScroll(); };
var sticky = null;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function onScroll() {
  // Get the navbar
  const navbar = document.getElementById("navbar");
  if (navbar) {
    // Get the offset position of the navbar
    if (sticky === null) {
      sticky = navbar.offsetTop;
    }

    if (window.pageYOffset >= sticky) {
      navbar.classList.add("sticky");
    } else {
      navbar.classList.remove("sticky");
    }
  }
}
